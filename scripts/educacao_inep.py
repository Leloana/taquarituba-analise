"""Educação: extrai do INEP os dados de Taquarituba e vizinhos e grava os CSVs em 01-demografia/dados.

Arquivos de entrada (baixar do INEP e deixar numa pasta, passada como argumento):
  dou2026.xlsx                      resultados_preliminares_extrato_simplificado_dou_2026.xlsx (Censo Escolar 2026)
  s24/**/*.xlsx, s25/**/*.xlsx      Sinopse Estatística da Educação Básica 2024 e 2025 (zips descompactados)
  ind/**/tx_rend_municipios_AAAA.xlsx (2023 a 2025), tx_rend_brasil_regioes_ufs_2025.xlsx,
  ind/**/TDI_MUNICIPIOS_2025.xlsx, TDI_BRASIL_REGIOES_UFS_2025.xlsx
URLs completas em 01-demografia/indicadores-sociais.md (fontes S19 a S22).

Uso: pip install openpyxl && python scripts/educacao_inep.py PASTA_INEP
Atenção: download.inep.gov.br às vezes não envia o certificado intermediário (RNP ICPEdu GR46 OV TLS CA 2025);
nesse caso baixe-o de http://secure.globalsign.com/cacert/rnpicpedugr46ovtlsca2025.crt e passe ao curl com --cacert.
"""
import glob
import sys

import csv
import json
import os

import openpyxl

DL = sys.argv[1] if len(sys.argv) > 1 else "inep"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "01-demografia", "dados")

MUN = {
    "3553807": "Taquarituba",
    "3504503": "Avaré",
    "3512605": "Coronel Macedo",
    "3515400": "Fartura",
    "3521804": "Itaí",
    "3522802": "Itaporanga",
    "3553005": "Taguaí",
}
DOU_NAMES = {
    "TAQUARITUBA": "Taquarituba", "AVARÉ": "Avaré", "CORONEL MACEDO": "Coronel Macedo",
    "FARTURA": "Fartura", "ITAÍ": "Itaí", "ITAPORANGA": "Itaporanga", "TAGUAÍ": "Taguaí",
}
SRC_SIN = {
    2024: "INEP, Sinopse Estatística da Educação Básica 2024, https://download.inep.gov.br/dados_abertos/sinopses_estatisticas/sinopse_estatistica_censo_escolar_2024.zip",
    2025: "INEP, Sinopse Estatística da Educação Básica 2025 (V2), https://download.inep.gov.br/dados_abertos/sinopses_estatisticas/sinopse_estatistica_censo_escolar_2025.zip",
}
SRC_DOU = ("INEP, Censo Escolar 2026, resultados preliminares (Portaria 731/2026, DOU 24/09/2026), "
           "https://download.inep.gov.br/censo_escolar/resultados/2026/resultados_preliminares_extrato_simplificado_dou_2026.xlsx")




def extract(src, out, codes, uf=False):
    """Guarda cabeçalho (12 linhas) e linhas dos municípios (ou de SP, se uf=True) de cada aba."""
    wb = openpyxl.load_workbook(src, read_only=True)
    res = {}
    for ws in wb.worksheets:
        head, hits = [], []
        for i, row in enumerate(ws.iter_rows(values_only=True)):
            if i < 12:
                head.append(list(row))
            cells = [str(c).strip() for c in row[:8] if c is not None]
            if (uf and any(c in ("São Paulo", "SP") for c in cells[:5])) or (not uf and any(c in codes for c in cells)):
                hits.append(list(row))
        res[ws.title] = {"head": head, "rows": hits}
    if uf:
        res = list(res.values())[0]
    json.dump(res, open(out, "w"), ensure_ascii=False, default=str)


def prepare():
    """Gera os JSONs intermediários a partir dos xlsx do INEP (uma vez)."""
    codes = set(MUN)
    one = lambda pat: glob.glob(os.path.join(DL, pat), recursive=True)[0]
    jobs = [
        (one("s24/**/*.xlsx"), f"{DL}/x24.json", False),
        (one("s25/**/*.xlsx"), f"{DL}/x25.json", False),
    ]
    for y in (2023, 2024, 2025):
        jobs.append((one(f"ind/**/tx_rend_municipios_{y}.xlsx"), f"{DL}/ind/tx_rend_municipios_{y}.json", False))
    jobs += [
        (one("ind/**/tx_rend_brasil_regioes_ufs_2025.xlsx"), f"{DL}/ind/tx_rend_brasil_regioes_ufs_2025.json", True),
        (one("ind/**/TDI_MUNICIPIOS_2025.xlsx"), f"{DL}/ind/TDI_MUNICIPIOS_2025.json", False),
        (one("ind/**/TDI_BRASIL_REGIOES_UFS_2025.xlsx"), f"{DL}/ind/TDI_BRASIL_REGIOES_UFS_2025.json", True),
    ]
    for src_, out_, uf in jobs:
        if not os.path.exists(out_):
            print("extraindo", os.path.basename(src_))
            extract(src_, out_, codes, uf)


def load(year):
    return json.load(open(f"{DL}/x{str(year)[2:]}.json"))


def title(v):
    return " ".join(str(c) for r in v["head"][:5] for c in r if c and "–" in str(c))


def find(d, *must):
    for k, v in d.items():
        t = title(v)
        if all(m in t for m in must):
            return {str(r[3]): r[3:] for r in v["rows"] if str(r[3]) in MUN}
    raise KeyError(must)


def num(x):
    try:
        return int(x)
    except (TypeError, ValueError):
        return 0


def public_by_net(year, row, urb_rur=True):
    """(estadual, municipal) da rede pública, conforme o layout de cada ano."""
    if year == 2024 and urb_rur:  # Total, Urbana(tot, fed, est, mun, priv), Rural(tot, fed, est, mun, priv)
        return num(row[4]) + num(row[9]), num(row[5]) + num(row[10])
    # 2025: Total, Pública(tot, fed, est, mun), Privada...
    return num(row[4]), num(row[5])


def build_matriculas():
    out = []
    stages = [
        ("creche", ("Matrículas", "Creche", "Localização")),
        ("pre_escola", ("Matrículas", "Pré-Escola", "Localização")),
        ("anos_iniciais", ("Matrículas", "Anos Iniciais", "Localização")),
        ("anos_finais", ("Matrículas", "Anos Finais", "Localização")),
        ("ensino_medio", ("Matrículas", "Ensino Médio Regular", "Localização")),
        ("eja", ("Matrículas", "(EJA)", "Localização")),
    ]
    for year in (2024, 2025):
        d = load(year)
        tot = find(d, "Matrículas da Educação Básica, por Etapa")
        for code, name in MUN.items():
            rec = {"municipio": name, "codigo_ibge": code, "ano": year, "situacao": "final"}
            for st, keys in stages:
                r = find(d, *keys)[code]
                est, mun = public_by_net(year, r)
                rec[f"{st}_publica"] = est + mun
                rec[f"{st}_total_com_privada"] = num(r[1])
            t = tot[code]
            rec["educacao_basica_total_com_privada"] = num(t[1])
            rec["educacao_especial_total"] = num(t[-3])
            rec["fonte"] = SRC_SIN[year]
            out.append(rec)
    # 2026 preliminar (só redes estadual + municipal)
    wb = openpyxl.load_workbook(f"{DL}/dou2026.xlsx", read_only=True)
    rows = list(wb.worksheets[0].iter_rows(values_only=True))
    sp_state = next(i for i, r in enumerate(rows) if r[1] and str(r[1]).strip().upper() == "SÃO PAULO")
    for r in rows[sp_state:]:
        n = str(r[1] or "").strip().upper()
        if n in DOU_NAMES:
            name = DOU_NAMES[n]
            code = next(c for c, m in MUN.items() if m == name)
            out.append({
                "municipio": name, "codigo_ibge": code, "ano": 2026, "situacao": "preliminar",
                "creche_publica": r[2], "pre_escola_publica": r[3], "anos_iniciais_publica": r[4],
                "anos_finais_publica": r[5], "ensino_medio_publica": r[6], "eja_publica": num(r[7]) + num(r[8]),
                "fonte": SRC_DOU,
            })
    cols = ["municipio", "codigo_ibge", "ano", "situacao",
            "creche_publica", "pre_escola_publica", "anos_iniciais_publica", "anos_finais_publica",
            "ensino_medio_publica", "eja_publica",
            "creche_total_com_privada", "pre_escola_total_com_privada", "anos_iniciais_total_com_privada",
            "anos_finais_total_com_privada", "ensino_medio_total_com_privada", "eja_total_com_privada",
            "educacao_basica_total_com_privada", "educacao_especial_total", "fonte"]
    out.sort(key=lambda r: (r["municipio"] != "Taquarituba", r["municipio"], r["ano"]))
    write("censo_escolar_matriculas_2024_2026.csv", cols, out)
    return out


def build_estrutura():
    out = []
    for year in (2024, 2025):
        d = load(year)
        esc = find(d, "Estabelecimentos da Educação Básica", "Localização")
        doc = find(d, "Docentes da Educação Básica", "Localização")
        tur = find(d, "Turmas da Educação Básica, por Etapa")
        mat = find(d, "Matrículas da Educação Básica", "Localização")
        for code, name in MUN.items():
            rec = {"municipio": name, "codigo_ibge": code, "ano": year}
            for lab, tab in (("escolas", esc), ("docentes", doc), ("matriculas", mat)):
                r = tab[code]
                est, mun = public_by_net(year, r, urb_rur=(lab != "docentes"))
                rec[f"{lab}_total"] = num(r[1])
                rec[f"{lab}_estadual"] = est
                rec[f"{lab}_municipal"] = mun
                rec[f"{lab}_privada"] = num(r[6]) if lab == "docentes" else num(r[1]) - est - mun
            rec["turmas_total"] = num(tur[code][1])
            rec["alunos_por_docente"] = round(rec["matriculas_total"] / rec["docentes_total"], 1)
            rec["fonte"] = SRC_SIN[year]
            out.append(rec)
    cols = list(out[0].keys())
    out.sort(key=lambda r: (r["municipio"] != "Taquarituba", r["municipio"], r["ano"]))
    write("censo_escolar_escolas_docentes_2024_2025.csv", cols, out)
    return out


def ind_rows(fname):
    d = json.load(open(f"{DL}/ind/{fname}"))
    return list(d.values())[0]["rows"]


def build_rendimento():
    out = []
    for year in (2023, 2024, 2025):
        src = (f"INEP, Taxas de Rendimento Escolar {year} (municípios), "
               f"https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/{year}/tx_rend_municipios_{year}.zip")
        for r in ind_rows(f"tx_rend_municipios_{year}.json"):
            if str(r[5]) != "Total" or str(r[6]) not in ("Pública", "Total"):
                continue
            # 7 = apr FUN, 8 AI, 9 AF, 19 MED ; reprov +18 ; abandono +36
            out.append({
                "territorio": r[4], "codigo_ibge": r[3], "ano": year, "rede": r[6],
                "aprovacao_ai": r[8], "aprovacao_af": r[9], "aprovacao_em": r[19],
                "reprovacao_ai": r[26], "reprovacao_af": r[27], "reprovacao_em": r[37],
                "abandono_ai": r[44], "abandono_af": r[45], "abandono_em": r[55],
                "fonte": src,
            })
    src = ("INEP, Taxas de Rendimento Escolar 2025 (Brasil, regiões e UFs), "
           "https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2025/tx_rend_brasil_regioes_ufs_2025.zip")
    for r in json.load(open(f"{DL}/ind/tx_rend_brasil_regioes_ufs_2025.json"))["rows"]:
        if r[2] == "Total" and r[3] in ("Pública", "Total"):
            out.append({
                "territorio": "Estado de SP", "codigo_ibge": "35", "ano": 2025, "rede": r[3],
                "aprovacao_ai": r[5], "aprovacao_af": r[6], "aprovacao_em": r[16],
                "reprovacao_ai": r[23], "reprovacao_af": r[24], "reprovacao_em": r[34],
                "abandono_ai": r[41], "abandono_af": r[42], "abandono_em": r[52],
                "fonte": src,
            })
    cols = list(out[0].keys())
    out.sort(key=lambda r: (r["territorio"] != "Taquarituba", r["territorio"] == "Estado de SP", r["territorio"], r["rede"], r["ano"]))
    write("rendimento_escolar_2023_2025.csv", cols, out)
    return out


def build_tdi():
    out = []
    src = ("INEP, Taxas de Distorção Idade-Série 2025, "
           "https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2025/TDI_2025_MUNICIPIOS.zip")
    for r in ind_rows("TDI_MUNICIPIOS_2025.json"):
        if str(r[5]) == "Total" and str(r[6]) in ("Pública", "Total"):
            out.append({"territorio": r[4], "codigo_ibge": r[3], "ano": 2025, "rede": r[6],
                        "tdi_anos_iniciais": r[8], "tdi_anos_finais": r[9], "tdi_ensino_medio": r[19], "fonte": src})
    src_uf = src.replace("MUNICIPIOS", "BRASIL_REGIOES_UFS")
    for r in json.load(open(f"{DL}/ind/TDI_BRASIL_REGIOES_UFS_2025.json"))["rows"]:
        if r[2] == "Total" and r[3] in ("Pública", "Total"):
            out.append({"territorio": "Estado de SP", "codigo_ibge": "35", "ano": 2025, "rede": r[3],
                        "tdi_anos_iniciais": r[5], "tdi_anos_finais": r[6], "tdi_ensino_medio": r[16], "fonte": src_uf})
    out.sort(key=lambda r: (r["territorio"] != "Taquarituba", r["territorio"] == "Estado de SP", r["territorio"], r["rede"]))
    write("distorcao_idade_serie_2025.csv", list(out[0].keys()), out)


def write(name, cols, rows):
    with open(os.path.join(OUT, name), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print("wrote", name, len(rows))


if __name__ == "__main__":
    prepare()
    build_matriculas()
    build_estrutura()
    build_rendimento()
    build_tdi()
