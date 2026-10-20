"""Voto por faixa de renda em Taquarituba: estimativa ecológica por local de votação.

Cruza a votação por seção do TSE (agregada por local de votação) com a renda média do
responsável pelo domicílio dos setores censitários do IBGE 2022 no entorno de cada local.

Uso:
  python scripts/voto_por_renda.py preparar --tse DIR --malha ARQUIVO.gpkg
      Lê os brutos do TSE e a malha de setores, grava os CSVs em 04-politica/dados/
      e em seguida gera os gráficos.
  python scripts/voto_por_renda.py
      Só gera os gráficos 16 e 17 a partir dos CSVs já gravados no repo.

Brutos esperados em DIR (o CSV de dentro de cada zip; pode ser o arquivo inteiro ou já
recortado para o município, o script filtra CD_MUNICIPIO == 71773):
  https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_secao/votacao_secao_2022_BR.zip  (presidente)
  https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_secao/votacao_secao_2022_SP.zip  (governador)
  https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_secao/votacao_secao_2024_SP.zip  (prefeito)
  https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_secao/votacao_secao_2026_BR.zip  (presidente)
  https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_secao/votacao_secao_2026_SP.zip  (governador)
  https://cdn.tse.jus.br/estatistica/sead/odsele/detalhe_votacao_secao/detalhe_votacao_secao_2022.zip  (membro _SP)
  https://cdn.tse.jus.br/estatistica/sead/odsele/detalhe_votacao_secao/detalhe_votacao_secao_2024.zip  (membro _SP)
  https://cdn.tse.jus.br/estatistica/sead/odsele/eleitorado_locais_votacao/eleitorado_local_votacao_2024.zip
Os zips de votação por seção têm de 0,5 a 0,9 GB; dá para recortar em streaming, ex.:
  curl -s URL | funzip | awk 'NR==1 || /"TAQUARITUBA"/' > votacao_secao_2022_SP.csv
Malha de setores (GeoPackage de SP):
  https://ftp.ibge.gov.br/Censos/Censo_Demografico_2022/Agregados_por_Setores_Censitarios/malha_com_atributos/setores/
Precisa de pandas e matplotlib; o passo "preparar" também precisa de shapely.
"""
import argparse
import itertools
import math
import sqlite3
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from graficos import (AZUL, CINZA, LARANJA, MUDO, SUPERFICIE, TINTA, TINTA2, VERMELHO,  # noqa: E402
                      br, fonte, plt, salvar, subtitulo)

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "04-politica" / "dados"
SETORES = RAIZ / "03-bairros" / "dados" / "setores_censitarios_2022_taquarituba.csv"
CD_TSE, CD_IBGE = "71773", "3553807"
SM_2022 = 1212.0          # salário mínimo de 2022, mês de referência do Censo
RAIO_M = 500              # raio do "entorno" do local de votação

# eleição: (ano, rótulo, arquivo, turno, cargo, {número: nome curto} dos 2 principais)
ELEICOES = [
    (2022, "Presidente 2022, 2º turno", "votacao_secao_2022_BR.csv", 2, "PRESIDENTE",
     {22: "Bolsonaro (PL)", 13: "Lula (PT)"}),
    (2022, "Governador 2022, 2º turno", "votacao_secao_2022_SP.csv", 2, "GOVERNADOR",
     {10: "Tarcísio (REPUBLICANOS)", 13: "Haddad (PT)"}),
    (2024, "Prefeito 2024", "votacao_secao_2024_SP.csv", 1, "PREFEITO",
     {11: "Éder Miano (PP)", 55: "Marcelo Milla (PSD)"}),
    (2026, "Presidente 2026, 1º turno", "votacao_secao_2026_BR.csv", 1, "PRESIDENTE",
     {22: "Flávio Bolsonaro (PL)", 13: "Lula (PT)"}),
    (2026, "Governador 2026, 1º turno", "votacao_secao_2026_SP.csv", 1, "GOVERNADOR",
     {10: "Tarcísio (REPUBLICANOS)", 13: "Haddad (PT)"}),
]

# nome curto do local para os gráficos (bairro do endereço no cadastro TSE)
APELIDO = {1015: "EMEI Julieta (Centro)", 1023: "EE José Penna (Bela Vista)",
           1031: "ETEC (Centro)", 1058: "EMEI Maria de Lourdes (V. Sta. Rita)",
           1066: "EMEI Virgínia (V. São Vicente)", 1074: "EM Célia (Aleixos)",
           1082: "EMEI Bernadete (Novo Centro)", 1112: "EMEI Maria Esther (Pedro M. Barros)"}


# deslocamento do rótulo (pontos) no gráfico 16, para não encavalar
POS_ROTULO = {1058: (10, 4, "left"), 1074: (8, 16, "left"), 1112: (8, 4, "left"), 1082: (-6, 4, "right"),
              1031: (8, -6, "left"), 1015: (0, -14, "center"), 1023: (0, -14, "center")}


# ---------------------------------------------------------------- leitura TSE
def ler_tse(caminho, colunas):
    partes = []
    for ch in pd.read_csv(caminho, sep=";", encoding="latin1", dtype=str, chunksize=500_000,
                          usecols=lambda c: c in colunas):
        partes.append(ch[ch["CD_MUNICIPIO"].str.strip() == CD_TSE])
    df = pd.concat(partes)
    for c in df.columns:
        if c.startswith(("QT_", "NR_")):
            df[c] = pd.to_numeric(df[c])
    return df


def locais_votacao(dir_tse):
    loc = ler_tse(dir_tse / "eleitorado_local_votacao_2024.csv",
                  {"CD_MUNICIPIO", "NR_LOCAL_VOTACAO", "NM_LOCAL_VOTACAO", "DS_ENDERECO",
                   "NM_BAIRRO", "NR_LATITUDE", "NR_LONGITUDE", "NR_SECAO"})
    loc = loc.groupby("NR_LOCAL_VOTACAO").agg(
        local=("NM_LOCAL_VOTACAO", "first"), endereco=("DS_ENDERECO", "first"),
        bairro_tse=("NM_BAIRRO", "first"), lat=("NR_LATITUDE", "first"),
        lon=("NR_LONGITUDE", "first")).reset_index()
    loc[["lat", "lon"]] = loc[["lat", "lon"]].astype(float)
    return loc.rename(columns={"NR_LOCAL_VOTACAO": "nr_local"})


def comparecimento(dir_tse, ano, turno):
    arq = dir_tse / f"detalhe_votacao_secao_{ano}_SP.csv"
    if not arq.exists():
        return None
    d = ler_tse(arq, {"CD_MUNICIPIO", "NR_TURNO", "DS_CARGO", "NR_SECAO", "NR_LOCAL_VOTACAO",
                      "QT_APTOS", "QT_COMPARECIMENTO"})
    d = d[d["NR_TURNO"] == turno]
    d = d[d["DS_CARGO"].str.upper() == d["DS_CARGO"].str.upper().iloc[0]]  # um cargo só
    return d.groupby("NR_LOCAL_VOTACAO")["QT_APTOS"].sum()


# ---------------------------------------------------------------- malha IBGE
def ler_malha(gpkg):
    import shapely
    con = sqlite3.connect(f"file:{gpkg}?mode=ro", uri=True)
    tab = con.execute("select table_name from gpkg_contents where data_type='features'").fetchone()[0]
    rows = con.execute(f'select CD_SETOR, geom from "{tab}" where CD_MUN = ?', (CD_IBGE,)).fetchall()
    out = {}
    for cd, blob in rows:
        flags = blob[3]
        env = {0: 0, 1: 32, 2: 48, 3: 48, 4: 64}[(flags >> 1) & 7]
        out[str(cd)] = shapely.from_wkb(bytes(blob[8 + env:]))
    return out


def dist_m(lat1, lon1, lat2, lon2):
    r = 6_371_000
    p1, p2 = np.radians(lat1), np.radians(lat2)
    a = (np.sin((p2 - p1) / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(np.radians(lon2 - lon1) / 2) ** 2)
    return 2 * r * np.arcsin(np.sqrt(a))


def media_pond(s):
    s = s[s["renda_media_resp"].notna() & (s["resp_dppo"] > 0)]
    if s.empty:
        return np.nan, 0
    return float(np.average(s["renda_media_resp"], weights=s["resp_dppo"])), int(s["resp_dppo"].sum())


def renda_locais(loc, malha):
    import shapely
    st = pd.read_csv(SETORES, dtype={"cd_setor": str})
    st["renda_media_resp"] = pd.to_numeric(st["renda_media_resp"], errors="coerce")
    st["resp_dppo"] = pd.to_numeric(st["resp_dppo"], errors="coerce").fillna(0)
    # área de influência: cada setor (com renda) vai para o local de votação mais próximo
    d_all = np.array([dist_m(st["lat"], st["lon"], r.lat, r.lon) for r in loc.itertuples()])
    st["local_mais_proximo"] = loc["nr_local"].to_numpy()[d_all.argmin(axis=0)]
    linhas = []
    for i, r in enumerate(loc.itertuples()):
        pt = shapely.Point(r.lon, r.lat)
        cd = next((k for k, g in malha.items() if g.contains(pt)), None)
        s0 = st[st["cd_setor"] == cd]
        viz = st[(d_all[i] <= RAIO_M) | (st["cd_setor"] == cd)]
        area = st[st["local_mais_proximo"] == r.nr_local]
        r_ent, resp_ent = media_pond(viz)
        r_area, resp_area = media_pond(area)
        linhas.append(dict(
            nr_local=r.nr_local, cd_setor=cd,
            bairro_reconstruido=s0["zona_atribuida"].iloc[0] if len(s0) else None,
            situacao_setor=s0["situacao"].iloc[0] if len(s0) else None,
            renda_setor=s0["renda_media_resp"].iloc[0] if len(s0) else np.nan,
            renda_entorno_500m=round(r_ent, 2), setores_entorno=len(viz), domicilios_entorno=resp_ent,
            renda_area_influencia=round(r_area, 2), setores_area=len(area),
            pop_area_influencia=int(pd.to_numeric(area["pop"], errors="coerce").sum()),
            domicilios_area=resp_area))
    return pd.DataFrame(linhas)


# ---------------------------------------------------------------- votos
def votos_por_local(dir_tse, eleicao):
    ano, rotulo, arq, turno, cargo, principais = eleicao
    d = ler_tse(dir_tse / arq, {"CD_MUNICIPIO", "NR_TURNO", "DS_CARGO", "NR_SECAO", "NR_VOTAVEL",
                                "QT_VOTOS", "NR_LOCAL_VOTACAO"})
    d = d[(d["NR_TURNO"] == turno) & (d["DS_CARGO"].str.upper() == cargo)]
    nums = list(principais)
    d["grupo"] = np.select([d["NR_VOTAVEL"] == nums[0], d["NR_VOTAVEL"] == nums[1],
                            d["NR_VOTAVEL"] == 95, d["NR_VOTAVEL"] == 96],
                           ["v1", "v2", "brancos", "nulos"], "outros")
    p = d.pivot_table(index="NR_LOCAL_VOTACAO", columns="grupo", values="QT_VOTOS", aggfunc="sum",
                      fill_value=0)
    for c in ("v1", "v2", "brancos", "nulos", "outros"):
        if c not in p:
            p[c] = 0
    p["secoes"] = d.groupby("NR_LOCAL_VOTACAO")["NR_SECAO"].nunique()
    p = p.reset_index().rename(columns={"NR_LOCAL_VOTACAO": "nr_local"})
    p["comparecimento"] = p[["v1", "v2", "brancos", "nulos", "outros"]].sum(axis=1)
    p["validos"] = p[["v1", "v2", "outros"]].sum(axis=1)
    p.insert(0, "eleicao", rotulo)
    p.insert(1, "ano", ano)
    p["cand_1"], p["cand_2"] = principais[nums[0]], principais[nums[1]]
    p = p.rename(columns={"v1": "votos_cand_1", "v2": "votos_cand_2", "outros": "votos_outros"})
    for c in ("cand_1", "cand_2", "outros"):
        p[f"pct_{c}"] = (100 * p[f"votos_{c}"] / p["validos"]).round(2)
    return p


def faixas(loc):
    """Terços aproximados de eleitorado: ordena os locais pela renda do entorno e corta o
    comparecimento acumulado em 1/3 e 2/3 (cada local inteiro vai para o terço do seu ponto médio)."""
    o = loc.sort_values("renda_entorno_500m").copy()
    acc = o["comparecimento"].cumsum() - o["comparecimento"] / 2
    frac = acc / o["comparecimento"].sum()
    o["faixa"] = np.select([frac < 1 / 3, frac < 2 / 3], ["1 baixa", "2 média"], "3 alta")
    return o.set_index("nr_local")["faixa"]


def corr(x, y, w=None):
    x, y = np.asarray(x, float), np.asarray(y, float)
    w = np.ones_like(x) if w is None else np.asarray(w, float)
    mx, my = np.average(x, weights=w), np.average(y, weights=w)
    cov = np.average((x - mx) * (y - my), weights=w)
    r = cov / math.sqrt(np.average((x - mx) ** 2, weights=w) * np.average((y - my) ** 2, weights=w))
    slope = cov / np.average((x - mx) ** 2, weights=w)
    return r, slope, my - slope * mx


def p_permutacao(x, y):
    """p bicaudal exato por permutação de y (n pequeno: n! permutações)."""
    r0 = abs(np.corrcoef(x, y)[0, 1])
    rs = [abs(np.corrcoef(x, perm)[0, 1]) >= r0 - 1e-12 for perm in itertools.permutations(y)]
    return sum(rs) / len(rs)


def preparar(dir_tse, gpkg):
    dir_tse = Path(dir_tse)
    loc = locais_votacao(dir_tse)
    loc = loc.merge(renda_locais(loc, ler_malha(gpkg)), on="nr_local")
    tabelas = []
    for e in ELEICOES:
        v = votos_por_local(dir_tse, e)
        aptos = comparecimento(dir_tse, e[0], e[3]) if e[0] in (2022, 2024) else None
        v["aptos"] = v["nr_local"].map(aptos) if aptos is not None else np.nan
        tabelas.append(loc.merge(v, on="nr_local", how="right"))
    tudo = pd.concat(tabelas, ignore_index=True)
    # faixa fixa por local, definida pelo comparecimento do 2º turno presidencial de 2022
    base = tudo[tudo["eleicao"] == ELEICOES[0][1]]
    tudo["faixa_renda"] = tudo["nr_local"].map(faixas(base))
    tudo["renda_entorno_sm"] = (tudo["renda_entorno_500m"] / SM_2022).round(2)
    cols = ["eleicao", "ano", "nr_local", "local", "endereco", "bairro_tse", "lat", "lon", "cd_setor",
            "situacao_setor", "bairro_reconstruido", "renda_setor", "renda_entorno_500m",
            "renda_entorno_sm", "setores_entorno", "domicilios_entorno", "renda_area_influencia",
            "setores_area", "pop_area_influencia", "faixa_renda", "secoes", "aptos",
            "comparecimento", "validos", "brancos", "nulos", "cand_1", "votos_cand_1", "pct_cand_1",
            "cand_2", "votos_cand_2", "pct_cand_2", "votos_outros", "pct_outros"]
    tudo = tudo[cols].sort_values(["ano", "eleicao", "renda_entorno_500m"])
    for ano, g in tudo.groupby("ano"):
        g.to_csv(DADOS / f"voto_por_local_votacao_{ano}.csv", index=False)
        print("ok", f"voto_por_local_votacao_{ano}.csv", len(g))

    # agregado por faixa (soma de votos, não média de percentuais)
    agg = []
    for (el, fx), g in tudo.groupby(["eleicao", "faixa_renda"], sort=False):
        s = g[["aptos", "comparecimento", "validos", "brancos", "nulos", "votos_cand_1",
               "votos_cand_2", "votos_outros"]].sum(min_count=1)
        renda = np.average(g["renda_entorno_500m"], weights=g["comparecimento"])
        agg.append(dict(eleicao=el, ano=g["ano"].iloc[0], faixa_renda=fx, locais=len(g),
                        locais_nomes="; ".join(APELIDO[n] for n in g["nr_local"]),
                        renda_entorno_min=g["renda_entorno_500m"].min(),
                        renda_entorno_max=g["renda_entorno_500m"].max(),
                        renda_entorno_media_pond=round(renda, 2),
                        renda_entorno_media_sm=round(renda / SM_2022, 2),
                        **{k: (int(s[k]) if pd.notna(s[k]) else None) for k in s.index},
                        cand_1=g["cand_1"].iloc[0], cand_2=g["cand_2"].iloc[0],
                        pct_cand_1=round(100 * s["votos_cand_1"] / s["validos"], 2),
                        pct_cand_2=round(100 * s["votos_cand_2"] / s["validos"], 2),
                        pct_outros=round(100 * s["votos_outros"] / s["validos"], 2)))
    agg = pd.DataFrame(agg).sort_values(["ano", "eleicao", "faixa_renda"])
    agg.to_csv(DADOS / "voto_por_faixa_renda.csv", index=False)
    print("ok voto_por_faixa_renda.csv")

    # correlações (impressas; o .md registra os valores)
    print("\neleicao | r (entorno 500 m) | r pond. | inclinação pp por R$ 1.000 | p perm. | r (área infl.) | r sem Aleixos")
    for el, g in tudo.groupby("eleicao", sort=False):
        x, y, w = g["renda_entorno_500m"] / 1000, g["pct_cand_1"], g["validos"]
        r, _, _ = corr(x, y)
        rw, sl, _ = corr(x, y, w)
        ra, _, _ = corr(g["renda_area_influencia"], y)
        u = g[g["nr_local"] != 1074]
        ru, _, _ = corr(u["renda_entorno_500m"], u["pct_cand_1"])
        print(f"{el} | {r:.2f} | {rw:.2f} | {sl:+.1f} | {p_permutacao(x.values, y.values):.3f} | {ra:.2f} | {ru:.2f}")


# ---------------------------------------------------------------- gráficos
def g16_dispersao():
    d22 = pd.read_csv(DADOS / "voto_por_local_votacao_2022.csv")
    d26 = pd.read_csv(DADOS / "voto_por_local_votacao_2026.csv")
    d22 = d22[d22["eleicao"] == ELEICOES[0][1]]
    d26 = d26[d26["eleicao"] == ELEICOES[3][1]]
    fig, ax = plt.subplots(figsize=(9.5, 6))
    for d, cor, nome in ((d22, AZUL, "Bolsonaro, 2º turno 2022"), (d26, LARANJA, "Flávio Bolsonaro, 1º turno 2026")):
        x, y = d["renda_entorno_500m"], d["pct_cand_1"]
        ax.scatter(x, y, s=d["comparecimento"] / 6, color=cor, edgecolor=SUPERFICIE, linewidth=2,
                   zorder=3, label=nome)
        _, sl, b = corr(x, y, d["validos"])
        xs = np.linspace(x.min(), x.max(), 10)
        ax.plot(xs, b + sl * xs, color=cor, linewidth=1.2, linestyle="--", zorder=2)
    for _, r in d22.iterrows():
        y2 = d26.loc[d26["nr_local"] == r["nr_local"], "pct_cand_1"].iloc[0]
        ax.plot([r["renda_entorno_500m"]] * 2, [r["pct_cand_1"], y2], color=CINZA, linewidth=1, zorder=1)
        dx, dy, ha = POS_ROTULO.get(r["nr_local"], (0, -14, "center"))
        ax.annotate(APELIDO[r["nr_local"]], (r["renda_entorno_500m"], min(r["pct_cand_1"], y2)),
                    textcoords="offset points", xytext=(dx, dy), ha=ha, va="top", fontsize=7.5,
                    color=TINTA2)
    ax.axhline(50, color=MUDO, linewidth=0.8)
    ax.xaxis.set_major_formatter(lambda v, _: f"R$ {br(v)}")
    ax.yaxis.set_major_formatter(lambda v, _: f"{int(v)}%")
    lo = min(d22["pct_cand_1"].min(), d26["pct_cand_1"].min())
    ax.set_ylim(lo - 7, max(d22["pct_cand_1"].max(), d26["pct_cand_1"].max()) + 4)
    ax.set_xlabel("Renda média do responsável no entorno de 500 m do local (Censo 2022)")
    ax.set_title("Voto no candidato Bolsonaro x renda do entorno, por local de votação")
    subtitulo(ax, "% dos votos válidos; cada ponto é um local de votação (área ∝ comparecimento); "
                  "tracejado: reta ponderada por votos. Estimativa ecológica, n = 8")
    ax.legend(loc="upper center", ncol=2, bbox_to_anchor=(0.5, -0.13))
    fonte(fig, "TSE, votação por seção 2022 e 2026; IBGE Censo 2022, setores censitários; cruzamento próprio",
          y=-0.06)
    salvar(fig, "16-voto-x-renda-dispersao")


def g17_faixas():
    df = pd.read_csv(DADOS / "voto_por_faixa_renda.csv")
    ordem = [e[1] for e in ELEICOES]
    fig, axes = plt.subplots(len(ordem), 1, figsize=(9.5, 8.6), sharex=True)
    nomes_fx = {"1 baixa": "Renda baixa", "2 média": "Renda média", "3 alta": "Renda alta"}
    for ax, el in zip(axes, ordem):
        g = df[df["eleicao"] == el].sort_values("faixa_renda", ascending=False)
        rot = [f"{nomes_fx[f]} (R$ {br(r)})" for f, r in zip(g["faixa_renda"], g["renda_entorno_media_pond"])]
        cor2 = VERMELHO if "(PT)" in g["cand_2"].iloc[0] else LARANJA
        esq = np.zeros(len(g))
        for col, cor in (("pct_cand_1", AZUL), ("pct_cand_2", cor2), ("pct_outros", CINZA)):
            v = g[col].to_numpy()
            ax.barh(rot, v, left=esq, color=cor, height=0.62, edgecolor=SUPERFICIE, linewidth=2)
            for i, (e, val) in enumerate(zip(esq, v)):
                if val >= 6:
                    ax.text(e + val / 2, i, f"{br(val, 1)}%", ha="center", va="center", fontsize=8,
                            color="white" if col != "pct_outros" else TINTA)
            esq += v
        ax.set_title(f"{el}:  {g['cand_1'].iloc[0]}  x  {g['cand_2'].iloc[0]}", fontsize=10,
                     loc="left", pad=4, fontweight="bold")
        ax.grid(False)
        ax.tick_params(axis="y", labelsize=8.5)
        ax.set_xlim(0, 100)
        for s in ("bottom",):
            ax.spines[s].set_visible(False)
        ax.tick_params(axis="x", length=0, labelbottom=False)
    fig.suptitle("Voto por faixa de renda do entorno do local de votação, Taquarituba",
                 x=0.01, ha="left", fontsize=13, fontweight="bold", color=TINTA, y=1.04)
    fig.text(0.01, 1.005, "% dos votos válidos. Azul: 1º nome do título; vermelho: PT; laranja: PSD; "
             "cinza: outros. Terços aproximados do eleitorado; estimativa ecológica",
             fontsize=9.5, color=TINTA2, ha="left")
    fig.tight_layout(h_pad=1.2)
    fonte(fig, "TSE, votação por seção 2022, 2024 e 2026; IBGE Censo 2022, setores; cruzamento próprio")
    salvar(fig, "17-voto-por-faixa-renda")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("acao", nargs="?", default="graficos", choices=["preparar", "graficos"])
    ap.add_argument("--tse", help="diretório com os CSVs brutos do TSE")
    ap.add_argument("--malha", help="GeoPackage de setores censitários 2022 de SP")
    a = ap.parse_args()
    if a.acao == "preparar":
        if not (a.tse and a.malha):
            ap.error("preparar exige --tse e --malha")
        preparar(a.tse, a.malha)
    g16_dispersao()
    g17_faixas()


if __name__ == "__main__":
    main()
