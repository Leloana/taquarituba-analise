"""Mapa da renda por setor censitário (Censo 2022) em faixas de salário mínimo.

Uso: python scripts/mapa_renda.py   (precisa de geopandas, matplotlib, pandas)
Entradas: 03-bairros/dados/setores_taquarituba_2022.geojson (malha de setores IBGE 2022, filtrada e simplificada),
          03-bairros/dados/setores_censitarios_2022_taquarituba.csv, 03-bairros/dados/bairros_agregado_censo2022.csv,
          03-bairros/dados/ruas_osm.geojson (© colaboradores do OpenStreetMap, ODbL)
Saída: graficos/20-mapa-renda-setores.svg
"""
import geopandas as gpd
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch

from graficos import CINZA, EIXO, MUDO, RAIZ, SUPERFICIE, TINTA, TINTA2, br, fonte, salvar

SM_2022 = 1212
FAIXAS = [(0, 1.5, "até 1,5 SM"), (1.5, 2, "1,5 a 2 SM"), (2, 3, "2 a 3 SM"), (3, 4, "3 a 4 SM"),
          (4, 99, "acima de 4 SM")]
RAMPA = ["#b7d3f6", "#6da7ec", "#2a78d6", "#1c5cab", "#0d366b"]
DADOS = RAIZ / "03-bairros/dados"


def faixa(renda):
    if pd.isna(renda):
        return None
    sm = renda / SM_2022
    for i, (a, b, _) in enumerate(FAIXAS):
        if a <= sm < b:
            return i


def main():
    g = gpd.read_file(DADOS / "setores_taquarituba_2022.geojson")
    s = pd.read_csv(DADOS / "setores_censitarios_2022_taquarituba.csv", dtype={"cd_setor": str})
    g["cd_setor"] = g["CD_SETOR"].str.replace(r"\D", "", regex=True)
    g = g.merge(s[["cd_setor", "renda_media_resp", "pop", "zona_atribuida"]], on="cd_setor", how="left")
    g["faixa"] = g["renda_media_resp"].map(faixa)
    g.loc[g["pop"].fillna(0) < 20, "faixa"] = None
    print(g["faixa"].value_counts(dropna=False).sort_index().to_dict())

    ruas = gpd.read_file(DADOS / "ruas_osm.geojson")
    # núcleo urbano da sede (exclui Aleixos e Porto Taquari, que são urbanos isolados)
    cen = g.geometry.representative_point()
    sede = g[(g["SITUACAO"] == "Urbana") & cen.x.between(-49.27, -49.22) & cen.y.between(-23.56, -23.51)]
    x0, y0, x1, y1 = sede.total_bounds
    mx, my = (x1 - x0) * 0.06, (y1 - y0) * 0.06

    fig, ax = plt.subplots(figsize=(10, 10))
    sem = g[g["faixa"].isna()]
    sem.plot(ax=ax, color="#ecebe6", edgecolor=SUPERFICIE, linewidth=0.8, hatch="////")
    for i, cor in enumerate(RAMPA):
        sel = g[g["faixa"] == i]
        sel[sel["SITUACAO"] == "Urbana"].plot(ax=ax, color=cor, edgecolor=SUPERFICIE, linewidth=0.8)
        # setores rurais esmaecidos para não roubar a atenção da área urbana
        sel[sel["SITUACAO"] != "Urbana"].plot(ax=ax, color=cor, alpha=0.35, edgecolor=SUPERFICIE, linewidth=0.8)
    pesos = {"trunk": 1.6, "primary": 1.3, "secondary": 1.1, "tertiary": 0.9}
    ruas.plot(ax=ax, color="white", alpha=0.55, linewidth=[pesos.get(h, 0.35) for h in ruas["highway"]])

    b = pd.read_csv(DADOS / "bairros_agregado_censo2022.csv")
    b = b.dropna(subset=["lat", "lon"])
    b = b[(b["lon"].between(x0 - mx, x1 + mx)) & (b["lat"].between(y0 - my, y1 + my))]
    for _, r in b.iterrows():
        nome = str(r["zona"]).split(" (")[0].split(" / ")[0]
        if nome.startswith(("Setores sem", "Rural", "Distrito Industrial", "Bairro do")):
            continue
        nome = (nome.replace("Residencial ", "Res. ").replace("Loteamento ", "Lot. ").replace("Conj. Hab. ", "")
                .replace(" Firmo de Melo", "").replace("Jardim ", "Jd. "))
        dy = 0.0012 if nome.startswith("Dona Amélia") else 0
        ax.text(r["lon"], r["lat"] + dy, nome, fontsize=7.6, ha="center", va="center", color=TINTA,
                path_effects=[pe.withStroke(linewidth=2.6, foreground=SUPERFICIE)])

    ax.set_xlim(x0 - mx, x1 + mx)
    ax.set_ylim(y0 - my, y1 + my)
    ax.set_aspect(1 / 0.917)  # correção de latitude (cos 23,5°)
    ax.set_axis_off()
    ax.grid(False)

    alcas = [Patch(facecolor=c, label=FAIXAS[i][2]) for i, c in enumerate(RAMPA)]
    alcas.append(Patch(facecolor="#ecebe6", hatch="////", edgecolor=MUDO, label="sem moradores ou sem dado"))
    ax.legend(handles=alcas, loc="lower left", title="Renda média do responsável\n(salários mínimos de 2022)",
              title_fontsize=8.5, fontsize=8.5, frameon=True, facecolor=SUPERFICIE, edgecolor=EIXO)
    ax.set_title("Taquarituba: renda por setor censitário, área urbana (2022)", pad=24)
    ax.text(0, 1.01, "Mais escuro = mais renda; salário mínimo de 2022 = R$ 1.212; valores por bairro no gráfico 09", transform=ax.transAxes, fontsize=9.5, color=TINTA2)

    ins = fig.add_axes([0.74, 0.12, 0.2, 0.2])
    g.plot(ax=ins, color=[RAMPA[int(f)] if pd.notna(f) else "#ecebe6" for f in g["faixa"]],
           edgecolor=SUPERFICIE, linewidth=0.3)
    ins.add_patch(plt.Rectangle((x0 - mx, y0 - my), x1 - x0 + 2 * mx, y1 - y0 + 2 * my, fill=False,
                                edgecolor=TINTA, linewidth=1))
    ins.set_aspect(1 / 0.917)
    ins.set_axis_off()
    ins.set_title("município inteiro", fontsize=8, color=TINTA2, pad=2, loc="center", fontweight="normal")
    fonte(fig, "IBGE Censo 2022 (agregados e malha de setores); ruas © colaboradores do OpenStreetMap", y=0.06)
    salvar(fig, "20-mapa-renda-setores")


if __name__ == "__main__":
    main()
