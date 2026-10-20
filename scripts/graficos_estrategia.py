"""Gráficos 21 a 25: urbanismo e cultura por natureza, shows da FACITA, saída de jovens e Câmara 2024.

Uso: python scripts/graficos_estrategia.py   (precisa de matplotlib e pandas)
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

from graficos import (AZUL, LARANJA, AQUA, AMARELO, MAGENTA, VERDE, VIOLETA, VERMELHO, CINZA, SUPERFICIE,
                      TINTA, TINTA2, EIXO, RAIZ, br, fonte, salvar, subtitulo)

TCE = "TCE-SP, base de despesas (empenhado líquido); classificação por natureza própria"


def tce():
    t = pd.read_csv(RAIZ / "05-financas-publicas/dados/tce_urbanismo_cultura_2019_2025.csv", comment="#")
    return t


def empilhado(ax, anos, series, total_rotulo=True):
    base = pd.Series(0.0, index=anos)
    for nome, valores, cor in series:
        ax.bar([str(a) for a in anos], valores.values, bottom=base.values, color=cor, width=0.68, label=nome,
               edgecolor=SUPERFICIE, linewidth=1.2)
        base += valores.values
    if total_rotulo:
        for i, v in enumerate(base):
            ax.text(i, v + base.max() * 0.015, br(v, 1), ha="center", fontsize=9, color=TINTA, fontweight="bold")
    return base


def urbanismo():
    t = tce()
    u = t[t["ds_funcao_governo"] == "URBANISMO"].set_index("grupo")
    anos = [c for c in u.columns if c.isdigit()]
    u = u[anos].astype(float) / 1000
    pega = lambda *g: u.loc[[x for x in g if x in u.index]].sum()
    series = [
        ("Pessoal", pega("Pessoal e encargos"), AZUL),
        ("Combustível", pega("Combustível"), LARANJA),
        ("Energia (iluminação e prédios)", pega("Energia elétrica (inclui iluminação pública)"), AQUA),
        ("Obras", pega("Obras", "Outros investimentos"), AMARELO),
        ("Veículos e máquinas", pega("Veículos, máquinas e equipamentos"), MAGENTA),
        ("Limpeza terceirizada", pega("Limpeza e terceirizados"), VERDE),
        ("Outro custeio", pega("Outro custeio", "Outros"), CINZA),
    ]
    fig, ax = plt.subplots(figsize=(10, 5.4))
    tot = empilhado(ax, [int(a) for a in anos], series)
    ax.annotate("2022: ~R$ 3 mi de pessoal e\ncombustível vieram da Administração\n(reclassificação contábil)",
                xy=(3, 4.5), xytext=(0.2, 15.5), fontsize=8.5, color=TINTA2,
                arrowprops=dict(arrowstyle="-", color=TINTA2))
    ax.annotate("2023: obras (ligação de ruas,\nrecapeamento) e máquinas", xy=(4, 19), xytext=(4.6, 21.5),
                fontsize=8.5, color=TINTA2, arrowprops=dict(arrowstyle="-", color=TINTA2))
    ax.set_ylim(0, tot.max() * 1.22)
    ax.set_ylabel("R$ milhões correntes")
    ax.set_title("Urbanismo: o que está dentro do salto")
    subtitulo(ax, "Um terço do salto de 2022 é reclassificação; o resto é máquinas, garagem e asfalto; depois fica um piso fixo de ~R$ 8,5 mi")
    ax.legend(loc="upper center", ncol=4, bbox_to_anchor=(0.5, -0.07), fontsize=8.5)
    fonte(fig, TCE, y=-0.1)
    salvar(fig, "21-urbanismo-composicao")


def cultura():
    t = tce()
    c = t[t["ds_funcao_governo"] == "CULTURA"].set_index("grupo")
    anos = [x for x in c.columns if x.isdigit()]
    c = c[anos].astype(float) / 1000
    pega = lambda *g: c.loc[[x for x in g if x in c.index]].sum()
    series = [
        ("Pessoal", pega("Pessoal e encargos"), AZUL),
        ("Festividades (shows)", pega("Festividades e homenagens"), LARANJA),
        ("Locações, serviços e editais", pega("Outro custeio"), AQUA),
        ("Energia e equipamentos", pega("Energia elétrica (inclui iluminação pública)", "Veículos, máquinas e equipamentos",
                                        "Limpeza e terceirizados"), CINZA),
    ]
    fig, ax = plt.subplots(figsize=(9.5, 5))
    tot = empilhado(ax, [int(a) for a in anos], series)
    ax.annotate("FACITA assumida pela Prefeitura:\nR$ 1,93 mi em festividades,\n100% dinheiro próprio",
                xy=(6, 2.0), xytext=(3.6, 2.75), fontsize=8.5, color=TINTA2, arrowprops=dict(arrowstyle="-", color=TINTA2))
    ax.set_ylim(0, tot.max() * 1.22)
    ax.set_ylabel("R$ milhões correntes")
    ax.set_title("Cultura: o salto de 2025 é show")
    subtitulo(ax, "Biblioteca, patrimônio e oficinas seguem no mesmo patamar; o que cresceu foi festividade")
    ax.legend(loc="upper left", fontsize=8.5)
    fonte(fig, TCE)
    salvar(fig, "22-cultura-composicao")


def shows():
    s25 = [("Cobaia Produção Artística", 582), ("CER Produções", 300), ("B4 Produções", 288), ("OK Music", 250),
           ("LR Produções", 180), ("SAM Business", 175), ("MC Music", 80), ("JVS Produções", 50)]
    s26 = [("Simone Mendes", 950), ("Zezé Di Camargo & Luciano", 770), ("Murilo Huff", 705), ("Baile da rainha", 30)]
    linhas = [(n, v, 2025) for n, v in s25] + [(n, v, 2026) for n, v in s26]
    linhas = sorted(linhas, key=lambda x: (x[2], x[1]))
    fig, ax = plt.subplots(figsize=(9.5, 6))
    nomes = [f"{n} ({a})" for n, _, a in linhas]
    ax.barh(nomes, [v for _, v, _ in linhas], color=[AZUL if a == 2025 else LARANJA for _, _, a in linhas], height=0.65)
    for i, (_, v, _) in enumerate(linhas):
        ax.text(v + 12, i, f"R$ {br(v)} mil", va="center", fontsize=8.5, color=TINTA)
    ax.grid(axis="y", visible=False); ax.grid(axis="x")
    ax.set_xlim(0, 1150)
    ax.legend(handles=[Patch(color=AZUL, label="2025: R$ 1,9 mi (TCE, empenhado)"),
                       Patch(color=LARANJA, label="2026: R$ 2,46 mi (PNCP, contratado até set.)")], loc="lower right")
    ax.set_title("Shows contratados sem licitação (inexigibilidade)")
    subtitulo(ax, "Só os shows da FACITA 2026 superam o orçamento de cultura do ano inteiro (R$ 2,0 mi na LOA 2026)")
    fonte(fig, "TCE-SP (2025); PNCP, contratações 2026/118 a 121 (2026); LOA 2026")
    salvar(fig, "23-shows-facita")


def coorte():
    c = pd.read_csv(RAIZ / "08-estrategia/dados/coorte_jovens_2010_2022.csv")
    c = c[(c["idade_2022"] >= 14) & (c["idade_2022"] <= 40)]
    var = (c["mulheres_2022"] / c["mulheres_2010"] - 1) * 100
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.bar(c["idade_2022"], var, color=[LARANJA if v < 0 else AZUL for v in var], width=0.75)
    ax.axhline(0, color=EIXO, linewidth=1)
    ax.axvspan(24.5, 29.5, color=LARANJA, alpha=0.08, linewidth=0)
    ax.text(27, var.min() - 3, "13 a 17 anos em 2010:\n−17% em 12 anos", ha="center", va="top", fontsize=8.5, color=TINTA2)
    ax.set_ylim(var.min() - 12, max(var.max(), 10) + 5)
    ax.yaxis.set_major_formatter(lambda v, _: f"{int(v)}%")
    ax.set_xlabel("idade em 2022 (mesmas meninas contadas em 2010, 12 anos mais novas)")
    ax.set_title("Para onde foram as jovens? Variação de cada geração entre os Censos 2010 e 2022")
    subtitulo(ax, "Só mulheres (os homens são distorcidos pelo presídio); laranja = saíram mais do que chegaram")
    fonte(fig, "IBGE, Censos 2010 (tabela 1378) e 2022 (tabela 9514); cálculo próprio")
    salvar(fig, "24-saida-de-jovens")


def camara_2024():
    v = pd.read_csv(RAIZ / "04-politica/dados/vereadores_candidatos_1996_2024.csv")
    v = v[v["ano"] == 2024].groupby("partido")["votos"].sum().sort_values()
    quoc = 1250
    esquerda = {"PT", "PSB", "PSOL", "PCdoB", "PV", "REDE", "PDT"}
    fig, ax = plt.subplots(figsize=(9.5, 5))
    ax.barh(v.index, v.values, color=[VERMELHO if p in esquerda else CINZA for p in v.index], height=0.62)
    for i, x in enumerate(v.values):
        ax.text(x + 25, i, br(x), va="center", fontsize=9, color=TINTA)
    ax.axvline(quoc, color=TINTA2, linewidth=1)
    ax.text(quoc + 25, len(v) - 0.4, "quociente ≈ 1.250 votos", fontsize=8.5, color=TINTA2)
    ax.grid(axis="y", visible=False); ax.grid(axis="x")
    ax.set_xlim(0, v.max() * 1.18)
    ax.set_title("Votos para vereador por partido, 2024", pad=36)
    subtitulo(ax, "PT (533) e PSB (535) separados não elegeram ninguém; juntos (1.068) passariam de 80% do quociente e disputariam\nas sobras, como o PSDB, que elegeu 1 com 1.200 votos")
    fonte(fig, "TSE, votação nominal 2024; quociente aproximado (válidos / 11 cadeiras)")
    salvar(fig, "25-camara-2024-quociente")


if __name__ == "__main__":
    for f in (urbanismo, cultura, shows, coorte, camara_2024):
        f()
