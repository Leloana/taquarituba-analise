# PIB de Taquarituba (SP), 2002 a 2023

Código IBGE 3553807. Dados levantados em 20/10/2026.

Legenda: **[oficial]** = número publicado pela fonte. **[cálculo]** = conta feita aqui sobre dado oficial (método explicado). **[estimativa]** = aproximação com premissa.

## Fontes

- IBGE, PIB dos Municípios, SIDRA tabela 5938 (2010 a 2021 com valor adicionado por setor): https://sidra.ibge.gov.br/tabela/5938
- IBGE, bases de dados PIB dos Municípios 2002 a 2009 e 2010 a 2023, referência 2010 (trazem a série desde 2002 e o PIB total e per capita oficiais de 2022 e 2023): https://ftp.ibge.gov.br/Pib_Municipios/2022_2023/base/
- IBGE, IPCA número índice, SIDRA tabela 1737 (deflator): https://sidra.ibge.gov.br/tabela/1737
- Dados tabulados: `dados/pib_taquarituba_2002_2023.csv`, `dados/pib_comparativo_vizinhos.csv`, `dados/ipca_media_anual.csv`

**Limite importante:** o IBGE só divulgou o PIB total e o per capita para 2022 e 2023. A quebra por setor (agro, indústria, serviços, administração pública) **não foi publicada** para esses dois anos na base atual (aparece como "..." no SIDRA). A composição setorial mais recente é de **2021**.

## Números principais

| Indicador | Valor | Tipo | Fonte |
|---|---|---|---|
| PIB 2023 (preços correntes) | R$ 1,279 bilhão | oficial | IBGE PIB dos Municípios 2023 |
| PIB per capita 2023 | R$ 52.529,90 | oficial | IBGE PIB dos Municípios 2023 |
| PIB 2010 (preços correntes) | R$ 253,6 milhões | oficial | IBGE, tabela 5938 |
| PIB per capita 2010 | R$ 11.373,42 | oficial | IBGE, base 2010 a 2023 |
| Crescimento real do PIB 2002 a 2023 | +262% (R$ 353 milhões para R$ 1,279 bilhão, em R$ de 2023) | cálculo (deflator IPCA média anual) | IBGE PIB + IPCA |
| Crescimento real do PIB 2010 a 2023 | +135,9% | cálculo | IBGE PIB + IPCA |
| Crescimento real do PIB per capita 2010 a 2023 | +116% (R$ 24.325 para R$ 52.530, em R$ de 2023) | cálculo | idem |
| Participação no PIB do estado de SP (2023) | 0,04% | oficial | IBGE, tabela 5938 |

Sobre o "crescimento real": o IBGE não publica PIB municipal a preços constantes. O valor acima deflaciona o PIB nominal pelo IPCA (média anual). É uma aproximação de poder de compra, não a variação de volume oficial. Pelo mesmo método, o estado de SP cresceu 24,4% no período.

## Série histórica

| Ano | PIB corrente (R$ mil) | PIB em R$ mil de 2023 (IPCA) | PIB per capita corrente (R$) | Per capita em R$ de 2023 |
|---|---|---|---|---|
| 2002 | 100.598 | 353.480 | 4.379 | 15.388 |
| 2003 | 113.972 | 349.103 | 4.879 | 14.944 |
| 2004 | 123.525 | 354.946 | 5.201 | 14.946 |
| 2005 | 132.787 | 357.036 | 5.501 | 14.790 |
| 2006 | 152.884 | 394.563 | 6.233 | 16.086 |
| 2007 | 174.254 | 433.916 | 7.860 | 19.572 |
| 2008 | 203.329 | 479.109 | 8.849 | 20.851 |
| 2009 | 223.469 | 502.026 | 9.691 | 21.770 |
| 2010 | 253.559 | 542.300 | 11.373 | 24.325 |
| 2011 | 291.894 | 585.436 | 13.081 | 26.235 |
| 2012 | 358.298 | 681.780 | 16.040 | 30.521 |
| 2013 | 395.542 | 708.680 | 17.136 | 30.701 |
| 2014 | 477.700 | 804.935 | 20.659 | 34.811 |
| 2015 | 527.345 | 814.995 | 22.767 | 35.185 |
| 2016 | 646.055 | 918.213 | 27.845 | 39.575 |
| 2017 | 651.091 | 894.541 | 28.016 | 38.491 |
| 2018 | 672.483 | 891.268 | 29.011 | 38.450 |
| 2019 | 825.648 | 1.054.886 | 35.561 | 45.434 |
| 2020 | 895.749 | 1.108.836 | 38.517 | 47.680 |
| 2021 | 988.152 | 1.129.457 | 42.425 | 48.491 |
| 2022 | 1.227.811 | 1.284.211 | 50.423 | 52.740 |
| 2023 | 1.279.103 | 1.279.103 | 52.530 | 52.530 |

Colunas correntes: oficiais (IBGE). Colunas em R$ de 2023: cálculo com IPCA.

Leitura por fases:
- **2002 a 2005: estagnação** (PIB real parado perto de R$ 350 milhões de 2023).
- **2006 a 2016: crescimento contínuo**, inclusive durante a recessão nacional de 2015 e 2016, quando a soja ganhou área.
- **2017 e 2018: pausa.**
- **2019 a 2022: novo salto**, com preço alto de grãos.
- **2023: estável** (dado mais recente do IBGE; 2024 ainda não divulgado).

No detalhe, o PIB cresce em termos reais em quase todo o período. Há estagnação em 2017 e 2018 (queda real de 2,6% em 2017) e estabilidade entre 2022 e 2023 (variação real de -0,4%). O salto maior vem em 2019 e em 2022.

Observação: o TCE-SP cita PIB per capita 2019 de R$ 35.061,88 (https://www.tce.sp.gov.br/sites/default/files/rdm/taquarituba.pdf). A base IBGE atual traz R$ 35.560,68 para 2019. A diferença vem provavelmente da revisão da população usada pelo IBGE. Este documento usa a base IBGE mais recente.

## Composição setorial do valor adicionado (oficial, IBGE tabela 5938)

| Ano | Agropecuária | Indústria | Serviços (exceto adm. pública) | Administração pública |
|---|---|---|---|---|
| 2002 | 17,6% | 7,7% | 51,5% | 23,2% |
| 2006 | 18,2% | 8,9% | 50,2% | 22,7% |
| 2010 | 16,6% | 9,0% | 53,5% | 21,0% |
| 2015 | 10,2% | 11,7% | 61,9% | 16,2% |
| 2019 | 9,0% | 8,1% | 70,3% | 12,6% |
| 2020 | 16,2% | 8,3% | 63,4% | 12,1% |
| 2021 | 15,2% | 7,6% | 65,7% | 11,5% |

Valores de 2021 em R$ mil: VA total 873.778; agro 132.340; indústria 66.621; serviços 574.067; administração pública 100.749; impostos 114.374.

Três atividades com maior valor adicionado em 2021, segundo o IBGE: "Demais serviços", "Comércio e reparação de veículos" e "Agricultura, inclusive apoio à agricultura e pós colheita". Em 2010 a ordem era "Demais serviços", "Administração pública" e "Agricultura".

Leitura:
- Serviços dominam e ganharam peso (51% em 2002, 53% em 2010, 66% em 2021). Série anual completa no CSV. O comércio subiu para a segunda posição desde 2014. Os dados do Caravela citam o "comércio atacadista de matérias primas agrícolas" como setor característico da cidade (https://www.caravela.info/municipios/sp/taquarituba-sp, acesso em 20/10/2026). Isso é coerente com cidade polo de comercialização de grãos, mas o IBGE não detalha qual empresa ou ramo puxa o "Demais serviços".
- A agropecuária voltou a pesar 15% a 16% em 2020 e 2021, puxada pela soja (ver `agropecuaria.md`).
- A indústria é pequena (7,6%) e perdeu espaço.
- A administração pública caiu de 21% para 11,5% do VA. Não porque encolheu (cresceu em reais), mas porque o resto cresceu mais rápido.

## Comparação com vizinhos e com SP

PIB per capita oficial (IBGE) e crescimento real do PIB total 2010 a 2023 (cálculo com IPCA):

| Local | PIB per capita 2023 (R$) | Crescimento real PIB 2010 a 2023 | Agro / Ind. / Serv. / Adm. em 2021 |
|---|---|---|---|
| **Taquarituba** | **52.530** | **+135,9%** | 15,2 / 7,6 / 65,7 / 11,5 |
| Avaré | 47.503 | +66,5% | 5,3 / 16,4 / 63,8 / 14,6 |
| Itaí | 43.001 | +64,3% | 35,7 / 8,1 / 41,1 / 15,0 |
| Coronel Macedo | 38.750 | +101,8% | 48,2 / 7,9 / 23,0 / 20,9 |
| Fartura | 34.036 | +62,9% | 22,0 / 12,2 / 48,3 / 17,5 |
| Taguaí | 32.310 | +65,7% | 17,9 / 6,5 / 55,2 / 20,5 |
| Itaporanga | 28.989 | +77,3% | 22,4 / 4,5 / 49,0 / 24,1 |
| Estado de SP | 77.566 (cálculo: PIB / pop. Censo 2022) | +24,4% | 2,1 / 23,1 / 65,7 / 9,2 |

Fontes: IBGE PIB dos Municípios (tabela 5938 e base 2010 a 2023). O per capita do estado foi calculado aqui com a população do Censo 2022 (44.411.238), mesmo critério que o IBGE usou para os municípios em 2023.

Leitura: Taquarituba tem o maior PIB per capita e o maior crescimento real entre os sete municípios da comparação. Mesmo assim, o per capita fica em cerca de 68% do estadual.

## Ressalva sobre PIB per capita e renda

PIB per capita alto não significa renda alta da população. O PIB inclui lucro de empresas, comercialização de grãos e impostos, que não ficam necessariamente com os moradores. A renda domiciliar per capita do Censo 2022 foi R$ 1.515 por mês (ver `renda-e-desigualdade.md`), cerca de R$ 18 mil por ano, um terço do PIB per capita.
