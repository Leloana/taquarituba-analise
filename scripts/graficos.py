"""Gera os gráficos do dossiê a partir dos CSVs do repo.

Uso: python scripts/graficos.py   (precisa de matplotlib e pandas)
Saída: graficos/*.svg
"""
import os
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
OUT = RAIZ / "graficos"
OUT.mkdir(exist_ok=True)

# Paleta de referência (validada para daltonismo nos pares adjacentes)
AZUL, LARANJA, AQUA, AMARELO, MAGENTA, VERDE, VIOLETA, VERMELHO = (
    "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948")
CINZA = "#b5b3ab"
SUPERFICIE, TINTA, TINTA2, MUDO, GRADE, EIXO = (
    "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7")

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "figure.facecolor": SUPERFICIE,
    "axes.facecolor": SUPERFICIE,
    "savefig.facecolor": SUPERFICIE,
    "axes.edgecolor": EIXO,
    "axes.labelcolor": TINTA2,
    "axes.titlecolor": TINTA,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "axes.titlelocation": "left",
    "axes.titlepad": 22,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.spines.left": False,
    "axes.grid": True,
    "axes.grid.axis": "y",
    "grid.color": GRADE,
    "grid.linewidth": 0.8,
    "xtick.color": MUDO,
    "ytick.color": MUDO,
    "xtick.labelcolor": TINTA2,
    "ytick.labelcolor": TINTA2,
    "ytick.left": False,
    "legend.frameon": False,
    "legend.labelcolor": TINTA2,
    "lines.linewidth": 2,
    "svg.fonttype": "none",
    "axes.axisbelow": True,
})


def br(v, casas=0):
    s = f"{v:,.{casas}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def subtitulo(ax, texto):
    ax.text(0, 1.02, texto, transform=ax.transAxes, color=TINTA2, fontsize=9.5, va="bottom")


def fonte(fig, texto, y=-0.02):
    fig.text(0.01, y, "Fonte: " + texto, color=MUDO, fontsize=8, ha="left", va="top")


def salvar(fig, nome):
    fig.savefig(OUT / f"{nome}.svg", bbox_inches="tight", pad_inches=0.25)
    if os.environ.get("PNG_DIR"):
        fig.savefig(Path(os.environ["PNG_DIR"]) / f"{nome}.png", dpi=90, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print("ok", nome)


def ler(caminho):
    return pd.read_csv(RAIZ / caminho, comment="#")


# 1. População 1970 a 2026 ------------------------------------------------------
def populacao():
    df = ler("01-demografia/dados/populacao_serie_historica.csv")
    df = df.drop_duplicates("ano", keep="first").sort_values("ano")
    censo = df[df["tipo"].str.contains("censo", case=False)]
    est = df[~df["tipo"].str.contains("censo", case=False)]
    fig, ax = plt.subplots(figsize=(9, 4.6))
    ax.plot(censo["ano"], censo["populacao"], color=AZUL, marker="o", ms=7,
            markeredgecolor=SUPERFICIE, markeredgewidth=2, label="Censo")
    ax.plot(est["ano"], est["populacao"], color=AZUL, alpha=0.45, marker="o", ms=4,
            linestyle="none", label="Estimativa IBGE")
    for _, r in censo.iterrows():
        ax.annotate(br(r["populacao"]), (r["ano"], r["populacao"]), textcoords="offset points",
                    xytext=(0, 10), ha="center", fontsize=9, color=TINTA)
    ult = df.iloc[-1]
    ax.annotate(f"{br(ult['populacao'])}\n({int(ult['ano'])})", (ult["ano"], ult["populacao"]),
                textcoords="offset points", xytext=(0, 10), ha="center", fontsize=9, color=TINTA2)
    ax.axvline(2014, color=EIXO, linewidth=1)
    ax.text(2014.4, 15000, "Penitenciária\n(2014, ~1.200 presos)", fontsize=8.5, color=TINTA2)
    ax.set_ylim(12000, 27500)
    ax.yaxis.set_major_formatter(lambda v, _: br(v))
    ax.set_title("População de Taquarituba, 1970 a 2026")
    subtitulo(ax, "Cresce devagar: +0,74% ao ano entre 2010 e 2022, cerca de 0,3% sem o presídio")
    ax.legend(loc="upper left")
    fonte(fig, "IBGE, Censos 1970 a 2022 e estimativas populacionais")
    salvar(fig, "01-populacao")


# 2. Pirâmide etária 2010 x 2022 ------------------------------------------------
def piramide():
    p22 = ler("01-demografia/dados/piramide_etaria_2022.csv")
    p10 = ler("01-demografia/dados/piramide_etaria_2010.csv")
    p22 = p22[p22["faixa"].str.contains("anos")].reset_index(drop=True)
    p10 = p10[p10["faixa"].str.contains("anos")].reset_index(drop=True)
    tot22, tot10 = p22["total"].sum(), p10["total"].sum()
    y = range(len(p22))
    fig, ax = plt.subplots(figsize=(9, 6.5))
    h22 = -p22["homens"] / tot22 * 100
    m22 = p22["mulheres"] / tot22 * 100
    ax.barh(y, h22, color=AZUL, height=0.8, label="Homens 2022", edgecolor=SUPERFICIE, linewidth=1)
    ax.barh(y, m22, color=LARANJA, height=0.8, label="Mulheres 2022", edgecolor=SUPERFICIE, linewidth=1)
    ax.step(-p10["homens"] / tot10 * 100, y, where="mid", color=TINTA, linewidth=1.4, label="2010 (contorno)")
    ax.step(p10["mulheres"] / tot10 * 100, y, where="mid", color=TINTA, linewidth=1.4)
    ax.set_yticks(list(y))
    ax.set_yticklabels([f.replace(" anos", "").replace(" ou mais", "+") for f in p22["faixa"]])
    ax.xaxis.set_major_formatter(lambda v, _: f"{br(abs(v), 0)}%")
    ax.grid(axis="x"); ax.grid(axis="y", visible=False)
    ax.axvline(0, color=EIXO, linewidth=1)
    ax.annotate("Excesso de homens\nde 20 a 44 anos:\npenitenciária", xy=(-4.6, 6), xytext=(-5.2, 15.5),
                fontsize=8.5, color=TINTA2, arrowprops=dict(arrowstyle="-", color=MUDO))
    ax.set_title("Pirâmide etária, 2022 com contorno de 2010")
    subtitulo(ax, "Base encolhe e topo engorda: idade mediana 36 anos, índice de envelhecimento 93,6 (era 53)")
    ax.legend(loc="upper right")
    ax.set_xlabel("% da população")
    fonte(fig, "IBGE, Censos 2010 e 2022")
    salvar(fig, "02-piramide-etaria")


# 3. Nascimentos e óbitos ---------------------------------------------------------
def vitais():
    df = ler("01-demografia/dados/estatisticas_vitais_datasus_2000_2026.csv")
    df = df[(df["municipio"] == "Taquarituba") & (df["ano"] <= 2025)]
    fig, ax = plt.subplots(figsize=(9, 4.6))
    ax.plot(df["ano"], df["nascidos_vivos_residencia"], color=AZUL, label="Nascidos vivos")
    ax.plot(df["ano"], df["obitos_residencia"], color=LARANJA, label="Óbitos")
    for col, cor in (("nascidos_vivos_residencia", AZUL), ("obitos_residencia", LARANJA)):
        for ano in (2000, 2025):
            r = df[df["ano"] == ano].iloc[0]
            ax.plot(ano, r[col], "o", color=cor, ms=8, markeredgecolor=SUPERFICIE, markeredgewidth=2)
            ax.annotate(str(int(r[col])), (ano, r[col]), textcoords="offset points",
                        xytext=(-14 if ano == 2000 else 14, 0), ha="center", va="center", fontsize=9, color=TINTA)
    r21 = df[df["ano"] == 2021].iloc[0]
    ax.annotate("2021, covid:\nmais mortes (298)\nque nascimentos (287)", (2021, 298), xytext=(2006.2, 432), va="top",
                fontsize=8.5, color=TINTA2, arrowprops=dict(arrowstyle="-", color=MUDO))
    ax.set_ylim(80, 440)
    ax.set_title("Nascimentos e óbitos por ano, 2000 a 2025")
    subtitulo(ax, "A distância entre as curvas, que sustenta o crescimento natural, quase sumiu")
    ax.legend(loc="lower left")
    fonte(fig, "DATASUS SINASC/SIM, por residência; 2025 preliminar")
    salvar(fig, "03-nascimentos-obitos")


# 4. Causas de óbito ---------------------------------------------------------------
def causas():
    df = ler("01-demografia/dados/obitos_por_causa_cid10_2019_2025.csv")
    df = df[df["capitulo_cid10"].str.match(r"^[IVX]+\.")].copy()
    df["n"] = df[["2022", "2023", "2024"]].sum(axis=1)
    nomes = {
        "IX": "Aparelho circulatório", "II": "Câncer", "X": "Aparelho respiratório",
        "XVIII": "Mal definidas", "XX": "Causas externas", "IV": "Endócrinas e metabólicas",
        "XI": "Aparelho digestivo", "I": "Infecciosas", "VI": "Sistema nervoso", "XIV": "Aparelho geniturinário",
    }
    df["cap"] = df["capitulo_cid10"].str.extract(r"^([IVX]+)\.")[0]
    df["nome"] = df["cap"].map(nomes)
    top = df.dropna(subset=["nome"]).sort_values("n").tail(8)
    total = df["n"].sum()
    fig, ax = plt.subplots(figsize=(9, 4.6))
    cores = [AZUL] * len(top)
    ax.barh(top["nome"], top["n"], color=cores, height=0.62)
    for i, (n, nome) in enumerate(zip(top["n"], top["nome"])):
        ax.text(n + 4, i, f"{int(n)}  ({br(n / total * 100, 1)}%)", va="center", fontsize=9, color=TINTA)
    ax.grid(axis="y", visible=False); ax.grid(axis="x")
    ax.set_xlim(0, top["n"].max() * 1.25)
    ax.set_title("Principais causas de óbito, 2022 a 2024 somados")
    subtitulo(ax, f"{int(total)} óbitos de residentes; causas externas lideram entre 20 e 39 anos")
    fonte(fig, "DATASUS SIM, capítulos da CID-10")
    salvar(fig, "04-causas-obito")


# 5. PIB real ---------------------------------------------------------------------
def pib():
    df = ler("02-economia/dados/pib_taquarituba_2002_2023.csv")
    fig, ax = plt.subplots(figsize=(9, 4.6))
    y = df["pib_real_mil_reais_de_2023_ipca"] / 1000
    ax.fill_between(df["ano"], y, color=AZUL, alpha=0.12, linewidth=0)
    ax.plot(df["ano"], y, color=AZUL)
    for ano in (2002, 2010, 2023):
        v = y[df["ano"] == ano].iloc[0]
        ax.plot(ano, v, "o", color=AZUL, ms=8, markeredgecolor=SUPERFICIE, markeredgewidth=2)
        ax.annotate(f"R$ {br(v)} mi", (ano, v), textcoords="offset points", xytext=(0, 11), ha="center",
                    fontsize=9, color=TINTA)
    ax.set_ylim(0, y.max() * 1.18)
    ax.yaxis.set_major_formatter(lambda v, _: br(v))
    ax.set_ylabel("R$ milhões de 2023 (IPCA)")
    ax.set_title("PIB real de Taquarituba, 2002 a 2023")
    subtitulo(ax, "+136% acima da inflação desde 2010, contra +24% do estado de SP")
    fonte(fig, "IBGE, PIB dos Municípios; deflator IPCA (cálculo próprio)")
    salvar(fig, "05-pib-real")


# 6. PIB per capita vizinhos -------------------------------------------------------
def pib_vizinhos():
    df = ler("02-economia/dados/pib_comparativo_vizinhos.csv")
    df = df[df["ano"] == df["ano"].max()].sort_values("pib_per_capita_reais")
    df["nome"] = df["localidade"].str.replace(" (SP)", "", regex=False)
    cores = [AZUL if "Taquarituba" in n else CINZA for n in df["nome"]]
    fig, ax = plt.subplots(figsize=(9, 4.4))
    ax.barh(df["nome"], df["pib_per_capita_reais"], color=cores, height=0.62)
    for i, v in enumerate(df["pib_per_capita_reais"]):
        ax.text(v + 800, i, f"R$ {br(v / 1000, 1)} mil", va="center", fontsize=9, color=TINTA)
    ax.grid(axis="y", visible=False); ax.grid(axis="x")
    ax.xaxis.set_major_formatter(lambda v, _: br(v / 1000) + " mil")
    ax.set_xlim(0, df["pib_per_capita_reais"].max() * 1.2)
    ax.set_title(f"PIB per capita, {int(df['ano'].max())}")
    subtitulo(ax, "Taquarituba lidera a vizinhança, mas a renda das famílias não acompanha")
    fonte(fig, "IBGE, PIB dos Municípios")
    salvar(fig, "06-pib-per-capita-vizinhos")


# 7. Composição setorial -----------------------------------------------------------
def setores():
    df = ler("02-economia/dados/pib_taquarituba_2002_2023.csv")
    for c in ("pct_agro_va", "pct_industria_va", "pct_servicos_va", "pct_adm_publica_va"):
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.dropna(subset=["pct_agro_va"]).reset_index(drop=True)
    cols =[("pct_servicos_va", "Serviços", AZUL), ("pct_agro_va", "Agropecuária", LARANJA),
            ("pct_adm_publica_va", "Adm. pública", AQUA), ("pct_industria_va", "Indústria", AMARELO)]
    fig, ax = plt.subplots(figsize=(9, 4.6))
    base = pd.Series(0.0, index=df.index)
    for col, nome, cor in cols:
        ax.bar(df["ano"], df[col], bottom=base, color=cor, width=0.82, label=nome,
               edgecolor=SUPERFICIE, linewidth=1)
        base += df[col]
    ult = df.iloc[-1]
    acc = 0
    for col, nome, cor in cols:
        ax.text(ult["ano"] + 0.7, acc + ult[col] / 2, f"{nome} {br(ult[col], 1)}%", va="center",
                fontsize=8.5, color=TINTA)
        acc += ult[col]
    ax.set_ylim(0, 100)
    ax.set_xlim(df["ano"].min() - 0.7, ult["ano"] + 4.2)
    ax.set_xticks(range(2002, int(ult["ano"]) + 1, 3))
    ax.yaxis.set_major_formatter(lambda v, _: f"{int(v)}%")
    ax.set_title("Composição do valor adicionado por setor")
    subtitulo(ax, f"Serviços ganham peso; agro oscila com a safra (último ano com divisão: {int(ult['ano'])})")
    ax.legend(loc="upper center", ncol=4, bbox_to_anchor=(0.4, -0.08))
    fonte(fig, "IBGE, PIB dos Municípios", y=-0.1)
    salvar(fig, "07-setores-economia")


# 8. Classes sociais ---------------------------------------------------------------
def classes():
    df = ler("02-economia/dados/classes_estimadas_renda_per_capita.csv")
    r = df[(df["ano"] == 2022) & (df["localidade"] == "Taquarituba")].iloc[0]
    nomes = ["E\naté ½ SM", "D\n½ a 1 SM", "C\n1 a 3 SM", "B\n3 a 10 SM", "A\n10+ SM"]
    vals = [float(r[c]) for c in ("E_ate_meio_sm_pc_inclui_sem_renda", "D_meio_a_1_sm_pc", "C_1_a_3_sm_pc",
                                  "B_3_a_10_sm_pc", "A_mais_10_sm_pc")]
    ramp = ["#86b6ef", "#5598e7", "#2a78d6", "#1c5cab", "#104281"]
    fig, ax = plt.subplots(figsize=(9, 4.4))
    ax.bar(nomes, vals, color=ramp, width=0.62)
    for i, v in enumerate(vals):
        ax.text(i, v + 0.8, f"{br(v, 1)}%", ha="center", fontsize=10, color=TINTA, fontweight="bold")
    ax.set_ylim(0, 42)
    ax.yaxis.set_major_formatter(lambda v, _: f"{int(v)}%")
    ax.set_title("Classe social estimada pela renda per capita, 2022")
    subtitulo(ax, "D e C somam 70% da população; 59,5% vive com até 1 salário mínimo por pessoa (estimativa)")
    fonte(fig, "IBGE Censo 2022, tabela 10296; faixas por salário mínimo per capita (classificação própria)", y=-0.06)
    salvar(fig, "08-classes-sociais")


# 9. Renda por bairro --------------------------------------------------------------
def bairros():
    df = ler("03-bairros/dados/bairros_agregado_censo2022.csv")
    df = df[pd.to_numeric(df["renda_media_resp_pond"], errors="coerce").notna()].copy()
    df["renda"] = df["renda_media_resp_pond"].astype(float)
    df["pop"] = pd.to_numeric(df["pop"], errors="coerce")
    df = df[df["pop"] >= 150]
    df["nome"] = df["zona"].str.replace(r"\s*\(.*$", "", regex=True).str.split(" / ").str[0]
    df = df.sort_values("renda")
    media = 2397
    cores = [AZUL if v >= media else LARANJA for v in df["renda"]]
    fig, ax = plt.subplots(figsize=(9, 7.4))
    ax.barh(df["nome"], df["renda"], color=cores, height=0.66)
    for i, v in enumerate(df["renda"]):
        ax.text(v + 60, i, f"R$ {br(v)}", va="center", fontsize=8.5, color=TINTA)
    ax.axvline(media, color=TINTA2, linewidth=1)
    ax.text(media + 60, len(df) - 0.4, f"média do município R$ {br(media)}", fontsize=8.5, color=TINTA2)
    ax.grid(axis="y", visible=False); ax.grid(axis="x")
    ax.tick_params(axis="y", labelsize=8.5)
    ax.set_xlim(0, df["renda"].max() * 1.18)
    ax.set_title("Renda média do responsável pelo domicílio, por bairro (2022)")
    subtitulo(ax, "Azul acima da média do município, laranja abaixo; bairros reconstruídos a partir dos setores censitários")
    fonte(fig, "IBGE Censo 2022, agregados por setor; recorte de bairro próprio (ver 03-bairros)")
    salvar(fig, "09-renda-por-bairro")


# 10. Presidente: PT x principal adversário ---------------------------------------
def presidente():
    df = ler("04-politica/dados/eleicoes_gerais_1998_2026.csv")
    df = df[df["cargo"] == "Presidente"]
    linhas = []
    for ano, g in df.groupby("ano"):
        g = g[g["turno"] == g["turno"].max()]
        pt = g[g["partido"] == "PT"].iloc[0]
        adv = g[g["partido"] != "PT"].sort_values("votos").iloc[-1]
        linhas.append((ano, int(g["turno"].iloc[0]), pt["pct_votos_nominais_validos"],
                       adv["pct_votos_nominais_validos"], adv["nome_urna"].title(), adv["partido"]))
    t = pd.DataFrame(linhas, columns=["ano", "turno", "pt", "adv", "nome", "partido"])
    fig, ax = plt.subplots(figsize=(9.5, 5))
    ax.plot(t["ano"], t["adv"], color=AZUL, marker="o", ms=8, markeredgecolor=SUPERFICIE,
            markeredgewidth=2, label="Principal adversário do PT")
    ax.plot(t["ano"], t["pt"], color=VERMELHO, marker="o", ms=8, markeredgecolor=SUPERFICIE,
            markeredgewidth=2, label="PT")
    for _, r in t.iterrows():
        nome = r["nome"].replace("Fernando Henrique", "FHC")
        adv_cima = r["adv"] >= r["pt"]
        ax.annotate(f"{nome} ({r['partido']})\n{br(r['adv'], 1)}%", (r["ano"], r["adv"]),
                    textcoords="offset points", xytext=(0, 10 if adv_cima else -12), ha="center",
                    va="bottom" if adv_cima else "top", fontsize=7.8, color=TINTA)
        ax.annotate(f"{br(r['pt'], 1)}%", (r["ano"], r["pt"]), textcoords="offset points",
                    xytext=(0, -12 if adv_cima else 10), ha="center", va="top" if adv_cima else "bottom",
                    fontsize=7.8, color=TINTA2)
    ax.axhline(50, color=EIXO, linewidth=1)
    ax.set_ylim(10, 88)
    ax.set_xticks(t["ano"])
    ax.set_xticklabels([f"{a}\n{tu}º t." for a, tu in zip(t["ano"], t["turno"])])
    ax.yaxis.set_major_formatter(lambda v, _: f"{int(v)}%")
    ax.set_title("Presidente em Taquarituba, 1998 a 2026 (votos válidos)")
    subtitulo(ax, "Tucano até 2014, bolsonarista desde 2018; Lula só venceu no município em 2002 e Dilma em 2010")
    ax.legend(loc="upper center", ncol=2, bbox_to_anchor=(0.5, -0.12))
    fonte(fig, "TSE, votação por município; último turno disponível de cada eleição (2026: 1º turno)", y=-0.13)
    salvar(fig, "10-presidente")


# 11. Câmara por partido -----------------------------------------------------------
def camara():
    df = ler("04-politica/dados/bancada_por_partido_1996_2024.csv")
    df["partido"] = df["partido"].replace({"PPB": "PP", "PMDB": "MDB", "PFL": "DEM"})
    principais = [("PSDB", AZUL), ("PP", LARANJA), ("PV", AQUA), ("PL", AMARELO),
                  ("PSD", MAGENTA), ("PT", VERMELHO), ("DEM", VIOLETA)]
    nomes = [p for p, _ in principais]
    df["grupo"] = df["partido"].where(df["partido"].isin(nomes), "Outros")
    pv = df.pivot_table(index="ano", columns="grupo", values="cadeiras", aggfunc="sum").fillna(0)
    anos = [str(a) for a in pv.index]
    fig, ax = plt.subplots(figsize=(9.5, 5))
    base = pd.Series(0.0, index=pv.index)
    for p, cor in principais + [("Outros", CINZA)]:
        if p not in pv:
            continue
        ax.bar(anos, pv[p], bottom=base, color=cor, width=0.66, label=p, edgecolor=SUPERFICIE, linewidth=1.5)
        for i, (b, v) in enumerate(zip(base, pv[p])):
            if v >= 2:
                ax.text(i, b + v / 2, f"{p} {int(v)}", ha="center", va="center", fontsize=7.5,
                        color="white" if p not in ("PL", "PV", "PSD", "Outros") else TINTA)
        base += pv[p]
    ax.set_ylabel("cadeiras")
    ax.set_title("Vereadores eleitos por partido, 1996 a 2024")
    subtitulo(ax, "Câmara caiu de 15 para 9 e depois 11 cadeiras; PSDB some e PP, PL e PSD dividem a Casa")
    ax.legend(loc="center left", bbox_to_anchor=(1.0, 0.5))
    fonte(fig, "TSE; PPB contado como PP, PMDB como MDB, PFL como DEM")
    salvar(fig, "11-camara-partidos")


# 12. Receita: transferências x próprias ----------------------------------------
def receitas():
    df = ler("05-financas-publicas/dados/receitas_2013_2025_siconfi_dca.csv").set_index("item")
    anos = [c for c in df.columns if c.isdigit()]
    df = df[anos].astype(float)
    corr = df.loc["Receitas_correntes"]
    proprio = df.loc["Impostos_taxas_contrib_melhoria"] / corr * 100
    transf = df.loc["Transferencias_correntes"] / corr * 100
    outros = 100 - proprio - transf
    x = [int(a) for a in anos]
    fig, ax = plt.subplots(figsize=(9, 4.6))
    ax.bar(x, transf, color=AZUL, width=0.75, label="Transferências (FPM, ICMS, FUNDEB, SUS)",
           edgecolor=SUPERFICIE, linewidth=1)
    ax.bar(x, proprio, bottom=transf, color=LARANJA, width=0.75, label="Impostos e taxas próprios",
           edgecolor=SUPERFICIE, linewidth=1)
    ax.bar(x, outros, bottom=transf + proprio, color=CINZA, width=0.75, label="Outras", edgecolor=SUPERFICIE,
           linewidth=1)
    for xi, v in zip(x, transf):
        ax.text(xi, v / 2, f"{br(v)}%", ha="center", va="center", fontsize=8, color="white")
    ax.set_ylim(0, 100)
    ax.set_xticks(x)
    ax.yaxis.set_major_formatter(lambda v, _: f"{int(v)}%")
    ax.set_title("De onde vem a receita corrente da Prefeitura")
    subtitulo(ax, "4 de cada 5 reais vêm de repasses da União e do Estado, sem tendência de queda")
    ax.legend(loc="upper center", ncol=3, bbox_to_anchor=(0.5, -0.08), fontsize=8.5)
    fonte(fig, "Tesouro Nacional, Siconfi/DCA (2016 declarado sem ISS e ITBI)", y=-0.1)
    salvar(fig, "12-receitas-dependencia")


# 13. Despesa por função 2025 ------------------------------------------------------
def despesas():
    df = ler("05-financas-publicas/dados/despesas_funcao_2013_2025_siconfi_dca.csv")
    df = df[~df["funcao"].str.startswith(("00", "99"))].copy()
    df["nome"] = df["funcao"].str[3:]
    df = df.sort_values("2025_rs").tail(10)
    fig, ax = plt.subplots(figsize=(9, 4.8))
    ax.barh(df["nome"], df["2025_rs"] / 1e6, color=AZUL, height=0.62)
    for i, (v, p) in enumerate(zip(df["2025_rs"] / 1e6, df["2025_pct"])):
        ax.text(v + 0.6, i, f"R$ {br(v, 1)} mi  ({br(p, 1)}%)", va="center", fontsize=9, color=TINTA)
    ax.grid(axis="y", visible=False); ax.grid(axis="x")
    ax.set_xlim(0, df["2025_rs"].max() / 1e6 * 1.32)
    ax.set_xlabel("R$ milhões empenhados")
    ax.set_title("Como a Prefeitura gastou em 2025, por função")
    subtitulo(ax, "Educação e saúde levam mais da metade; total de R$ 169,9 milhões")
    fonte(fig, "Tesouro Nacional, Siconfi/DCA Anexo I-E, despesa empenhada")
    salvar(fig, "13-despesas-funcao-2025")


# 14. Pessoal / RCL -------------------------------------------------------------------
def pessoal():
    # a coluna obs tem vírgulas sem aspas; só as primeiras colunas interessam
    linhas = [l.split(",")[:5] for l in (RAIZ / "05-financas-publicas/dados/pessoal_e_divida_rgf_2018_2026.csv")
              .read_text(encoding="utf-8").splitlines() if l and not l.startswith("#")]
    df = pd.DataFrame(linhas[1:], columns=linhas[0])
    df["ano"] = df["ano"].astype(int)
    df["pct_pessoal_RCL"] = df["pct_pessoal_RCL"].astype(float)
    rot = [str(a) if a < 2026 else "2026\n(ago)" for a in df["ano"]]
    fig, ax = plt.subplots(figsize=(9, 4.4))
    ax.plot(rot, df["pct_pessoal_RCL"], color=AZUL, marker="o", ms=8, markeredgecolor=SUPERFICIE,
            markeredgewidth=2)
    for i, v in enumerate(df["pct_pessoal_RCL"]):
        ax.annotate(f"{br(v, 1)}%", (i, v), textcoords="offset points", xytext=(0, 10), ha="center",
                    fontsize=9, color=TINTA)
    for lim, nome in ((54, "limite máximo LRF 54%"), (51.3, "prudencial 51,3%"), (48.6, "alerta 48,6%")):
        ax.axhline(lim, color=EIXO, linewidth=1)
        ax.text(len(df) - 0.6, lim + 0.3, nome, fontsize=8, color=TINTA2, ha="right")
    ax.set_ylim(30, 57)
    ax.yaxis.set_major_formatter(lambda v, _: f"{int(v)}%")
    ax.set_title("Despesa com pessoal sobre a receita corrente líquida")
    subtitulo(ax, "Folgada em relação à LRF desde 2020; 2019 declarado em 52,9% (TCE recalculou 43,7%)")
    fonte(fig, "Tesouro Nacional, Siconfi RGF, Poder Executivo")
    salvar(fig, "14-pessoal-lrf")


# 15. Emendas federais por autor -----------------------------------------------------
def emendas():
    df = pd.read_csv(RAIZ / "05-financas-publicas/dados/emendas_federais_resumo_por_autor.csv", skiprows=1)
    df = df.sort_values("valor_recebido_total_rs").tail(12)
    df["nome"] = (df["autor"].str.title().str.replace("Com. Da Saude", "Comissão de Saúde")
                  .str.replace(" De ", " de ").str.replace("Capitao", "Capitão"))
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.barh(df["nome"], df["valor_recebido_total_rs"] / 1000, color=AZUL, height=0.62)
    for i, v in enumerate(df["valor_recebido_total_rs"] / 1000):
        ax.text(v + 12, i, f"R$ {br(v)} mil", va="center", fontsize=9, color=TINTA)
    ax.grid(axis="y", visible=False); ax.grid(axis="x")
    ax.set_xlim(0, df["valor_recebido_total_rs"].max() / 1000 * 1.25)
    ax.set_title("Emendas federais pagas a Taquarituba, 2016 a 2026 (12 maiores autores)")
    subtitulo(ax, "R$ 11,2 milhões no total, metade só em 2025 e 2026")
    fonte(fig, "CGU, Portal da Transparência, emendas por favorecido (base de 09/10/2026)")
    salvar(fig, "15-emendas-federais")


if __name__ == "__main__":
    for f in (populacao, piramide, vitais, causas, pib, pib_vizinhos, setores, classes, bairros,
              presidente, camara, receitas, despesas, pessoal, emendas):
        f()
