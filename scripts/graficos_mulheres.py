"""Gráficos 26 e 27: violência doméstica contra mulheres (SSP-SP), quem leva a vítima à delegacia e comparação regional.

Uso: python scripts/graficos_mulheres.py
"""
import pandas as pd
import matplotlib.pyplot as plt

from graficos import AZUL, LARANJA, AQUA, CINZA, TINTA, TINTA2, RAIZ, br, fonte, salvar, subtitulo

DADOS = RAIZ / "09-mulheres/dados"
SSP = "SSP-SP, base de violência contra a mulher (atualizada em 07/10/2026); cálculo próprio"


def quem_leva():
    d = pd.read_csv(DADOS / "ssp_violencia_domestica_mulher_2024_2026.csv", comment="#")
    d = d[d["periodo"] == "jan-ago"].set_index("ano")
    outros = d["mulheres_vitimas"] - d["apresentadas_pela_gcm"] - d["apresentadas_pela_pm"] - d["pela_propria_vitima"]
    series = [("Pela própria vítima", d["pela_propria_vitima"], AZUL),
              ("Guarda Municipal (Patrulha Maria da Penha)", d["apresentadas_pela_gcm"], LARANJA),
              ("Polícia Militar", d["apresentadas_pela_pm"], AQUA),
              ("Outros", outros.clip(lower=0), CINZA)]
    anos = [str(a) for a in d.index]
    fig, ax = plt.subplots(figsize=(8.5, 5))
    base = pd.Series(0.0, index=d.index)
    for nome, v, cor in series:
        ax.bar(anos, v.values, bottom=base.values, color=cor, width=0.55, label=nome, edgecolor="white", linewidth=1.2)
        for i, (b, x) in enumerate(zip(base.values, v.values)):
            if x >= 12:
                ax.text(i, b + x / 2, str(int(x)), ha="center", va="center", fontsize=9,
                        color="white" if cor != CINZA else TINTA)
        base += v.values
    for i, t in enumerate(d["mulheres_vitimas"]):
        ax.text(i, t + 2, f"{int(t)} mulheres", ha="center", fontsize=9.5, color=TINTA, fontweight="bold")
    ax.set_ylim(0, d["mulheres_vitimas"].max() * 1.18)
    ax.set_ylabel("mulheres vítimas (janeiro a agosto)")
    ax.set_title("Violência doméstica: vítimas com boletim e quem as levou à delegacia")
    subtitulo(ax, "+22% em 2026; a Patrulha Maria da Penha começou a levar vítimas em 2025. Mais registro pode ser menos subnotificação")
    ax.legend(loc="upper left", fontsize=8.5)
    fonte(fig, SSP)
    salvar(fig, "26-violencia-domestica-quem-leva")


def taxa_regional():
    t = pd.read_csv(DADOS / "ssp_taxa_violencia_domestica_comparada.csv", comment="#")
    t["nome"] = t["nome"].str.replace(" - SP", "", regex=False).str.replace(
        "Mediana de 99 municipios de SP com 8 a 16 mil mulheres", "Mediana de municípios do mesmo porte")
    t = t.sort_values("taxa_2026_por_mil")
    ref = t["nome"].isin(["Estado de SP", "Mediana de municípios do mesmo porte"])
    cores = [AZUL if n == "Taquarituba" else ("#d9d7cf" if r else CINZA) for n, r in zip(t["nome"], ref)]
    fig, ax = plt.subplots(figsize=(8.5, 5.2))
    ax.barh(t["nome"], t["taxa_2026_por_mil"], color=cores, height=0.62)
    for i, v in enumerate(t["taxa_2026_por_mil"]):
        ax.text(v + 0.15, i, br(v, 1), va="center", fontsize=9, color=TINTA)
    ax.grid(axis="y", visible=False); ax.grid(axis="x")
    ax.set_xlim(0, t["taxa_2026_por_mil"].max() * 1.15)
    ax.set_xlabel("mulheres vítimas de violência doméstica por mil mulheres, janeiro a agosto de 2026")
    ax.set_title("Taxa de violência doméstica registrada, 2026")
    subtitulo(ax, "Taquarituba acima do estado e da mediana do porte, mas no mesmo patamar de Avaré, Coronel Macedo e Fartura")
    fonte(fig, SSP + "; mulheres pelo Censo 2022 (IBGE 9514)")
    salvar(fig, "27-violencia-domestica-regiao")


if __name__ == "__main__":
    quem_leva()
    taxa_regional()
