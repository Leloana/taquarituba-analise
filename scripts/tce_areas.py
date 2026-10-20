"""Abre o gasto de Urbanismo e Cultura por ação, natureza e fornecedor, a partir da base de despesas do TCE-SP.

Entrada: arquivos desp_<ano>.csv filtrados para Taquarituba a partir de
https://transparencia.tce.sp.gov.br/conjunto-de-dados (despesas-<ano>.zip, um CSV de ~15 GB por ano com todos
os municípios; separador ';', latin-1). Para filtrar sem guardar o arquivo inteiro:
    curl -s https://transparencia.tce.sp.gov.br/sites/default/files/conjunto-dados/despesas-2025.zip \
      | python zipstream_filter.py TAQUARITUBA > desp_2025.csv
(zipstream_filter.py: descompacta o único membro do zip em fluxo e mantém o cabeçalho e as linhas com o termo.)

Uso: python scripts/tce_areas.py <pasta_com_desp_ANO.csv>
Saída: 05-financas-publicas/dados/tce_urbanismo_cultura_2019_2025.csv (função x ano x grupo de natureza)
       05-financas-publicas/dados/tce_fornecedores_urbanismo_cultura_2019_2025.csv
"""
import sys
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
FUNCOES = ["URBANISMO", "CULTURA", "ADMINISTRAÇÃO", "DESPORTO E LAZER"]


def grupo(elemento: str) -> str:
    e = str(elemento)
    if e.startswith("319") or e.startswith("3191"):
        return "Pessoal e encargos"
    if e.startswith("4490"):
        cod = e[:6]
        if cod in ("449051",):
            return "Obras"
        if cod in ("449052",):
            return "Veículos, máquinas e equipamentos"
        return "Outros investimentos"
    cod = e[:8]
    if cod == "33903943":
        return "Energia elétrica (inclui iluminação pública)"
    if cod == "33903923":
        return "Festividades e homenagens"
    if cod == "33903001":
        return "Combustível"
    if cod in ("33903978", "33903799", "33903701", "33903702"):
        return "Limpeza e terceirizados"
    if e.startswith("3390"):
        return "Outro custeio"
    return "Outros"


def carregar(pasta: Path) -> pd.DataFrame:
    partes = []
    for f in sorted(pasta.glob("desp_*.csv")):
        d = pd.read_csv(f, sep=";", encoding="latin-1", dtype=str, on_bad_lines="skip")
        d = d[d["codigo_municipio_ibge"] == "3553807"]
        d = d[d["ds_orgao"].str.contains("PREFEITURA", na=False)]
        d = d[d["tp_despesa"].isin(["Empenhado", "Reforço", "Anulação"])]
        d["v"] = d["vl_despesa"].str.replace(".", "", regex=False).str.replace(",", ".").astype(float)
        d.loc[d["tp_despesa"] == "Anulação", "v"] *= -1
        partes.append(d)
    return pd.concat(partes)


def main():
    d = carregar(Path(sys.argv[1]))
    d["ano"] = d["ano_exercicio"].astype(int)
    d["grupo"] = d["ds_elemento"].map(grupo)
    f = d[d["ds_funcao_governo"].isin(FUNCOES)]
    t = f.pivot_table(index=["ds_funcao_governo", "grupo"], columns="ano", values="v", aggfunc="sum").fillna(0)
    t = (t / 1e3).round(0)
    cab = ("# R$ mil correntes, despesa empenhada líquida de anulações, Prefeitura (sem Câmara e RPPS). "
           "Fonte: TCE-SP, conjunto de dados de despesas (https://transparencia.tce.sp.gov.br/conjunto-de-dados).\n")
    (RAIZ / "05-financas-publicas/dados/tce_urbanismo_cultura_2019_2025.csv").write_text(
        cab + t.to_csv(), encoding="utf-8")
    print(t.to_string())

    u = d[d["ds_funcao_governo"].isin(["URBANISMO", "CULTURA"])]
    g = u.groupby(["ds_funcao_governo", "ano", "ds_despesa"]).agg(
        v=("v", "sum"), modalidade=("ds_modalidade_lic", "first"), elemento=("ds_elemento", "first"),
        historico=("historico_despesa", lambda s: s.dropna().iloc[0][:160] if s.notna().any() else ""))
    g = g[g["v"].abs() >= 50000].reset_index().sort_values(["ds_funcao_governo", "ano", "v"], ascending=[True, True, False])
    g["v"] = (g["v"] / 1e3).round(0)
    g = g.rename(columns={"ds_funcao_governo": "funcao", "ds_despesa": "fornecedor", "v": "valor_mil_reais"})
    (RAIZ / "05-financas-publicas/dados/tce_fornecedores_urbanismo_cultura_2019_2025.csv").write_text(
        "# Fornecedores com R$ 50 mil ou mais no ano. " + cab, encoding="utf-8")
    with open(RAIZ / "05-financas-publicas/dados/tce_fornecedores_urbanismo_cultura_2019_2025.csv", "a",
              encoding="utf-8") as fh:
        fh.write(g.to_csv(index=False))


if __name__ == "__main__":
    main()
