"""Gasto da Prefeitura por área em valores reais (R$ de 2025, IPCA médio anual).

Uso: python scripts/gasto_real.py
Saída: 05-financas-publicas/dados/gasto_real_por_funcao_2013_2025.csv,
       05-financas-publicas/dados/investimentos_real_2013_2025.csv,
       graficos/18-gasto-real-por-area.svg, graficos/19-investimentos-real.svg
"""
import pandas as pd
import matplotlib.pyplot as plt

from graficos import (AZUL, LARANJA, CINZA, SUPERFICIE, TINTA, TINTA2, EIXO, RAIZ, br, fonte, salvar,
                      subtitulo)

# IPCA, número-índice médio anual (IBGE SIDRA 1737, média dos 12 meses)
IPCA = {2013: 3717.85, 2014: 3953.15, 2015: 4310.12, 2016: 4686.79, 2017: 4848.31, 2018: 5025.99,
        2019: 5213.61, 2020: 5381.06, 2021: 5827.78, 2022: 6368.60, 2023: 6661.15, 2024: 6952.07,
        2025: 7300.84}
FATOR = {a: IPCA[2025] / v for a, v in IPCA.items()}
ANOS = list(range(2013, 2026))
ELEICAO_MUNICIPAL = {2016, 2020, 2024}

# População: estimativas IBGE, Censo 2022; 2023 interpolado entre 2022 e 2024
POP = {2013: 23083, 2014: 23123, 2015: 23163, 2016: 23202, 2017: 23240, 2018: 23180, 2019: 23218,
       2020: 23256, 2021: 23292, 2022: 24350, 2023: 24607, 2024: 24863, 2025: 24932}

AREAS = ["10 Saúde", "12 Educação", "04 Administração", "09 Previdência Social", "15 Urbanismo",
         "08 Assistência Social", "13 Cultura", "06 Segurança Pública", "20 Agricultura", "27 Desporto e Lazer",
         "26 Transporte", "16 Habitação", "18 Gestão Ambiental", "01 Legislativa"]


def carregar():
    df = pd.read_csv(RAIZ / "05-financas-publicas/dados/despesas_funcao_2013_2025_siconfi_dca.csv", comment="#")
    df = df.set_index("funcao")
    real = pd.DataFrame({a: df[f"{a}_rs"] * FATOR[a] for a in ANOS})
    return real


def tabela(real):
    linhas = []
    for f in ["00 TOTAL exceto intra"] + AREAS:
        if f not in real.index:
            continue
        s = real.loc[f].fillna(0)
        ini, fim = s[2013], s[2025]
        var = (fim / ini - 1) * 100 if ini else float("nan")
        cagr = ((fim / ini) ** (1 / 12) - 1) * 100 if ini else float("nan")
        linhas.append({"funcao": f, **{str(a): round(s[a] / 1e6, 2) for a in ANOS},
                       "var_real_2013_2025_pct": round(var, 1), "cresc_real_anual_pct": round(cagr, 1),
                       "per_capita_2013_reais": round(ini / POP[2013]), "per_capita_2025_reais": round(fim / POP[2025])})
    t = pd.DataFrame(linhas)
    cab = "# R$ milhões de 2025 (IPCA médio anual, IBGE SIDRA 1737). Base: Siconfi/DCA Anexo I-E, despesa empenhada.\n"
    caminho = RAIZ / "05-financas-publicas/dados/gasto_real_por_funcao_2013_2025.csv"
    caminho.write_text(cab + t.to_csv(index=False), encoding="utf-8")
    return t


def grafico_areas(real):
    areas = AREAS[:9]
    fig, axs = plt.subplots(3, 3, figsize=(10.5, 8), sharex=True)
    for ax, f in zip(axs.flat, areas):
        s = real.loc[f].fillna(0) / 1e6
        ax.fill_between(ANOS, s, color=AZUL, alpha=0.12, linewidth=0)
        ax.plot(ANOS, s, color=AZUL)
        ax.plot([2013, 2025], [s[2013], s[2025]], "o", color=AZUL, ms=6, markeredgecolor=SUPERFICIE,
                markeredgewidth=1.5)
        var = (s[2025] / s[2013] - 1) * 100 if s[2013] else float("nan")
        ax.set_title(f[3:], fontsize=10.5, pad=6)
        cor = TINTA if not var < 0 else LARANJA
        rotulo = "nova (zero em 2013)" if var != var else f"{'+' if var >= 0 else ''}{br(var)}% real"
        ax.text(0.02, 0.97, rotulo, transform=ax.transAxes, fontsize=9,
                fontweight="bold", color=cor, va="top")
        ax.text(1, s[2025], f" {br(s[2025], 1)}", fontsize=8, color=TINTA2, va="center",
                transform=ax.get_yaxis_transform())
        ax.set_ylim(0, s.max() * 1.3)
        casas = 0 if s.max() > 8 else 1
        ax.yaxis.set_major_formatter(lambda v, _, c=casas: br(v, c))
        ax.tick_params(labelsize=8)
        ax.set_xticks([2013, 2017, 2021, 2025])
    fig.suptitle("Gasto por área, em R$ milhões de 2025 (acima da inflação)", x=0.06, ha="left",
                 fontsize=13, fontweight="bold", color=TINTA, y=1.0)
    fig.text(0.06, 0.965, "Despesa empenhada por função, 2013 a 2025, corrigida pelo IPCA; variação real de 2013 para 2025",
             fontsize=9.5, color=TINTA2)
    fig.tight_layout(rect=(0, 0.02, 1, 0.95))
    fonte(fig, "Tesouro Nacional, Siconfi/DCA Anexo I-E; IBGE, IPCA (cálculo próprio)", y=0.0)
    salvar(fig, "18-gasto-real-por-area")


def investimentos():
    df = pd.read_csv(RAIZ / "05-financas-publicas/dados/despesas_natureza_2013_2025_siconfi_dca.csv",
                     comment="#").set_index("natureza")
    inv = pd.Series({a: df.loc["Investimentos", str(a)] * FATOR[a] for a in ANOS})
    tot = pd.Series({a: df.loc["Total_geral", str(a)] for a in ANOS})
    pct = pd.Series({a: df.loc["Investimentos", str(a)] / tot[a] * 100 for a in ANOS})
    out = pd.DataFrame({"ano": ANOS, "investimentos_rs_2025": inv.round(0).values,
                        "pct_despesa_total": pct.round(1).values,
                        "per_capita_rs_2025": (inv / pd.Series(POP)).round(0).values})
    (RAIZ / "05-financas-publicas/dados/investimentos_real_2013_2025.csv").write_text(
        "# Investimentos (obras e equipamentos, GND 4) em R$ de 2025 pelo IPCA médio anual. Base: Siconfi/DCA Anexo I-D.\n"
        + out.to_csv(index=False), encoding="utf-8")

    fig, ax = plt.subplots(figsize=(9, 4.6))
    cores = [LARANJA if a in ELEICAO_MUNICIPAL else AZUL for a in ANOS]
    ax.bar(ANOS, inv / 1e6, color=cores, width=0.72)
    for a, v, p in zip(ANOS, inv / 1e6, pct):
        ax.text(a, v + 0.25, f"{br(v, 1)}\n{br(p, 1)}%", ha="center", fontsize=7.8, color=TINTA)
    ax.set_xticks(ANOS)
    ax.tick_params(axis="x", labelsize=8.5)
    ax.set_ylim(0, (inv / 1e6).max() * 1.28)
    ax.set_ylabel("R$ milhões de 2025")
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=AZUL, label="Ano comum"), Patch(color=LARANJA, label="Ano de eleição municipal")],
              loc="upper right")
    ax.set_title("Investimento em obras e equipamentos, acima da inflação")
    subtitulo(ax, "R$ milhões de 2025 e % da despesa total; picos em 2014/15, 2020 e 2022/23, vales em 2017 e 2024")
    fonte(fig, "Tesouro Nacional, Siconfi/DCA Anexo I-D (GND 4); IBGE, IPCA (cálculo próprio)")
    salvar(fig, "19-investimentos-real")
    return out


if __name__ == "__main__":
    real = carregar()
    t = tabela(real)
    print(t[["funcao", "2013", "2025", "var_real_2013_2025_pct", "cresc_real_anual_pct",
             "per_capita_2013_reais", "per_capita_2025_reais"]].to_string(index=False))
    grafico_areas(real)
    print(investimentos().to_string(index=False))
