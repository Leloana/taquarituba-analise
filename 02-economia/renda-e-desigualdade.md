# Renda e desigualdade em Taquarituba (SP)

Dados levantados em 20/10/2026. Legenda: **[oficial]**, **[cálculo]**, **[estimativa]**.

## Fontes

- Atlas do Desenvolvimento Humano no Brasil (PNUD, Ipea, FJP), Censos 1991, 2000 e 2010. Valores obtidos pela API do Ipeadata (séries ADH_RDPC, ADH_GINI, ADH_PIND, ADH_PMPOB, ADH_PREN10RICOS, ADH_PREN40, ADH_IDHM, ADH_IDHM_R): http://www.ipeadata.gov.br . Perfil do município: http://www.atlasbrasil.org.br/perfil/municipio/355380
- IBGE Censo 2022, rendimento: tabelas 10295 (média e mediana domiciliar per capita), 10289 (rendimento do trabalho), 10297 (composição da renda), 10296 (faixas de salário mínimo), 10301 (Gini, só Brasil, regiões e UF): https://sidra.ibge.gov.br/tabela/10295
- IBGE Censo 2010, tabela 3563 (média e mediana per capita dos domicílios) e 3535 (pessoas por faixa): https://sidra.ibge.gov.br/tabela/3563
- MDS, Cadastro Único e Bolsa Família (MI Social / VIS Data): https://aplicacoes.mds.gov.br/sagi/vis/data3/
- Dados: `dados/atlas_renda_desigualdade_1991_2000_2010.csv`, `dados/renda_censo_2010_2022.csv`, `dados/pessoas_por_faixa_renda_per_capita_sm.csv`, `dados/bolsa_familia_cadunico_bpc.csv`

## Renda per capita: 1991, 2000, 2010 (Atlas Brasil, oficial)

Valores em R$ de agosto de 2010.

| Indicador | 1991 | 2000 | 2010 |
|---|---|---|---|
| Renda per capita média | 364,77 | 470,77 | 624,86 |
| Índice de Gini | 0,58 | 0,58 | 0,48 |
| % extremamente pobres (renda pc menor que R$ 70) | 9,80 | 5,88 | 2,48 |
| % pobres (renda pc menor que R$ 140) | 36,63 | 22,92 | 7,73 |
| % da renda com os 10% mais ricos | 48,32 | 49,67 | 39,63 |
| % da renda com os 40% mais pobres | 10,30 | 10,41 | 13,56 |
| IDHM | 0,420 | 0,591 | 0,701 |
| IDHM Renda | 0,614 | 0,655 | 0,700 |

Leitura: a renda subiu 33% em termos reais entre 2000 e 2010 e a pobreza caiu forte (de 22,9% para 7,7%). O Gini caiu de 0,58 para 0,48. Em 2000 a desigualdade de Taquarituba era igual à do estado (0,58). Em 2010 ficou bem abaixo (0,48 contra 0,56 do estado).

## Renda em 2022 (Censo 2022, oficial)

| Indicador (R$ de julho de 2022) | Taquarituba | Estado de SP | Brasil |
|---|---|---|---|
| Renda domiciliar per capita, média | 1.515,25 | 2.093,44 | 1.638,06 |
| Renda domiciliar per capita, **mediana** | **1.102,00** | 1.250,17 | 1.000,00 |
| Rendimento de todos os trabalhos, média (ocupados) | 2.506,82 | 3.460,03 | 2.850,64 |
| Rendimento de todos os trabalhos, mediana (ocupados) | 1.600,00 | 2.000,00 | 1.700,00 |
| Parte da renda que vem do trabalho | 80,3% | 79,3% | 75,5% |
| Parte que vem de outras fontes (aposentadoria, benefícios, aluguéis) | 19,7% | 20,7% | 24,5% |

Fonte: IBGE Censo 2022, tabelas 10295, 10289 e 10297.

- A mediana (R$ 1.102) ficou **abaixo do salário mínimo de 2022** (R$ 1.212). Metade da população vivia com menos de 0,91 salário mínimo por pessoa.
- A média é 28% menor que a do estado. A mediana é só 12% menor. A diferença indica que falta topo de renda na cidade, mais do que a base ser muito pobre.
- A renda depende do trabalho um pouco mais que a média do estado. Aposentadorias e benefícios pesam menos que nos vizinhos menores (Fartura 29%, Coronel Macedo 30%, Itaporanga 28%).

### Censo 2010 (comparação, oficial)

Média da renda per capita **dos domicílios** em 2010: R$ 721,89; mediana R$ 500,00 (tabela 3563). Atenção: esse indicador é por domicílio, não por pessoa. Não é diretamente comparável com a tabela 10295 de 2022.

## Evolução real 2000, 2010, 2022 [estimativa]

Para comparar, os valores do Atlas (agosto de 2010) foram corrigidos pelo IPCA até julho de 2022 (fator 2,0602, IBGE tabela 1737).

| Local | 2000 (em R$ de 2022) | 2010 (em R$ de 2022) | 2022 (Censo) | Variação real 2010 a 2022 |
|---|---|---|---|---|
| **Taquarituba** | 970 | 1.287 | 1.515 | **+17,7%** |
| Avaré | 1.516 | 1.760 | 1.770 | +0,5% |
| Itaí | 826 | 1.225 | 1.401 | +14,3% |
| Fartura | 999 | 1.275 | 1.482 | +16,3% |
| Itaporanga | 738 | 1.139 | 1.284 | +12,7% |
| Coronel Macedo | 723 | 959 | 1.282 | +33,7% |
| Taguaí | 899 | 1.210 | 1.290 | +6,6% |
| Estado de SP | 1.818 | 2.234 | 2.093 | -6,3% |
| Brasil | 1.221 | 1.636 | 1.638 | +0,2% |

Por que é estimativa: o Atlas e o Censo 2022 usam questionários e tratamentos de renda diferentes. A ordem de grandeza é confiável; a casa decimal, não. Mesmo com essa ressalva, o sinal é claro: Taquarituba **ganhou renda real** entre 2010 e 2022, enquanto o estado ficou parado ou perdeu.

## Desigualdade

- Gini 2010: **0,48** (Atlas, oficial). Estado de SP 0,56; Brasil 0,60.
- Gini 2022 municipal: **não publicado**. O IBGE divulgou o Gini do Censo 2022 só para Brasil (0,542), grandes regiões e UFs (SP: 0,525) na tabela 10301 (https://sidra.ibge.gov.br/tabela/10301). Não encontrei Gini 2022 de Taquarituba em nenhuma fonte.
- Proxy [cálculo]: razão média sobre mediana da renda per capita em 2022. Quanto maior, mais concentrada no topo. Taquarituba 1,37; estado de SP 1,67; Brasil 1,64. Sugere desigualdade **menor** que a do estado, como em 2010. Não substitui o Gini.

Comparação do Gini 2010 (Atlas): Taguaí 0,37; Fartura 0,43; Coronel Macedo 0,45; Itaí 0,45; Avaré 0,47; **Taquarituba 0,48**; Itaporanga 0,53.

## Pobreza atual (Cadastro Único, oficial, junho de 2026)

| Indicador | Valor |
|---|---|
| Famílias no Cadastro Único | 3.568 (8.900 pessoas) |
| Famílias em extrema pobreza no CadÚnico | 584 |
| Famílias em pobreza no CadÚnico | 391 |
| Famílias com renda per capita até meio SM | 2.044 |
| Famílias no Bolsa Família | 1.174 (3.045 pessoas) |

Fonte: MDS, MI Social, referência 06/2026. As 8.900 pessoas do CadÚnico equivalem a cerca de 36% da população do Censo 2022 (24.350) [cálculo, mistura anos diferentes].

Mais detalhe sobre Bolsa Família e transferências em `emprego-e-atividades.md`.
