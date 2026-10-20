# Taquarituba (SP): população

Código IBGE 3553807. Região Administrativa de Itapeva (SEADE), Região de Saúde do Vale do Jurumirim, Região Imediata de Avaré (IBGE).

Legenda usada em todo o documento:

- **[oficial]**: número publicado pela fonte citada, sem alteração.
- **[cálculo]**: conta minha feita só com números oficiais (fórmula indicada).
- **[inferência]**: interpretação ou estimativa minha, não publicada por nenhuma fonte.

## 1. Série histórica

| Ano | População | Tipo | Fonte |
|---|---:|---|---|
| 1970 | 13.964 | Censo [oficial] | [S1] |
| 1980 | 16.174 | Censo [oficial] | [S1] |
| 1991 | 18.537 | Censo [oficial] | [S1] |
| 2000 | 21.982 | Censo [oficial] | [S1] |
| 2010 | 22.291 | Censo [oficial] | [S1] |
| 2021 | 23.292 | Estimativa IBGE (base Censo 2010) [oficial] | [S5] |
| **2022** | **24.350** | **Censo [oficial]** | [S2] |
| 2024 | 24.863 | Estimativa IBGE (base Censo 2022) [oficial] | [S5] |
| 2025 | 24.932 | Estimativa IBGE [oficial] | [S5] |
| 2026 | 24.995 | Estimativa IBGE [oficial] | [S5] |

Observação: as estimativas de 2011 a 2021 vinham subestimando a população. A estimativa de 2021 (23.292) ficou mais de 1.000 pessoas abaixo do que o Censo 2022 contou (24.350) [cálculo]. Não há estimativa IBGE para 2022 e 2023 (anos de Censo e de transição) [S5].

A SEADE usa uma série própria de população, um pouco diferente: 24.335 em 2022 e 24.593 em 2024 [oficial, S8]. Neste documento a referência é sempre o IBGE, salvo quando indicado.

## 2. Cresce ou encolhe?

**Cresce, devagar.** A população nunca caiu num intervalo de censos.

| Período | Taxa geométrica anual | Tipo | Fonte |
|---|---:|---|---|
| 1970 a 1980 | 1,48% | [cálculo] | [S1] |
| 1980 a 1991 | 1,25% | [cálculo] | [S1] |
| 1991 a 2000 | 1,91% | [cálculo] | [S1] |
| 2000 a 2010 | 0,14% | [cálculo] | [S1] |
| 2010 a 2022 | **0,74%** | [oficial, IBGE] | [S2] |
| 2022 a 2025 | 0,79% | [cálculo, estimativa] | [S2], [S5] |
| 2022 a 2026 | 0,66% | [cálculo, estimativa] | [S2], [S5] |

Fórmula do cálculo: (P_final / P_inicial)^(1/anos) - 1.

Variação absoluta 2010 a 2022: +2.059 pessoas [oficial, S2].

Comparação: o Estado de SP cresceu 0,61% ao ano entre 2010 e 2022 [oficial, S2]; Taquarituba cresceu um pouco mais rápido que o estado.

### 2.1 O peso da Penitenciária no crescimento

- A Penitenciária de Taquarituba foi criada pelo Decreto estadual nº 60.927, de 28/11/2014, para presos do sexo masculino em regime fechado [oficial, S10, 2014]. Fica na Rodovia Eduardo Saigh, zona rural [S11, 2023].
- A SES-SP registra 1.241 pessoas privadas de liberdade no município (dado da SAP/SP, 2024) [oficial, S7, portfólio de dez/2024].
- O Censo 2022 conta 23.148 moradores em domicílios particulares permanentes ocupados, contra 24.350 residentes no total [oficial, S6]. A diferença, **1.202 pessoas**, mora em domicílios coletivos (presídio, ILPI) ou improvisados [cálculo].
- Em 2010, homens e mulheres estavam praticamente empatados (11.092 homens e 11.199 mulheres) [oficial, S4]. Em 2022 há 12.603 homens e 11.747 mulheres [oficial, S3]. Só na faixa de 20 a 44 anos sobram cerca de 1.000 homens [cálculo, S3].

**[inferência]** Pelo menos metade do crescimento de 2010 a 2022 (+2.059) vem da população carcerária, que é contada como residente pelo Censo. Sem o presídio, o crescimento seria de algo como 800 a 900 pessoas em 12 anos, perto de 0,3% ao ano.

**[inferência]** O saldo de nascimentos menos óbitos de 2010 a 2021 foi de +1.429 (DATASUS, ver `natalidade-mortalidade.md`). Se a população "civil" cresceu só ~850, a migração líquida foi negativa, algo na ordem de -500 pessoas no período. Ou seja: a cidade gera gente, mas perde parte dela para fora, provavelmente jovens adultos.

**[inferência]** Também é provável que o presídio explique o aumento da população rural no Censo 2022 (ver seção 3), já que ele fica em zona rural.

## 3. Urbanização

| Ano | Urbana | Rural | % urbana | Fonte |
|---|---:|---:|---:|---|
| 1970 | 6.351 | 7.613 | 45,5% | [S1] |
| 1980 | 9.658 | 6.516 | 59,7% | [S1] |
| 1991 | 13.610 | 4.927 | 73,4% | [S1] |
| 2000 | 18.328 | 3.654 | 83,4% | [S1] |
| 2010 | 19.579 | 2.712 | 87,8% | [S1] |
| 2022 | 20.421 | 3.929 | **83,86%** | [S2b] |

Números absolutos: [oficial]. Percentuais até 2010: [cálculo]. Percentual de 2022: [oficial].

A taxa de urbanização caiu de 87,8% para 83,9% entre 2010 e 2022, e a população rural subiu de 2.712 para 3.929 (+1.217). Esse salto tem tamanho quase igual ao do presídio (1.241). **[inferência]** O "aumento rural" provavelmente é carcerário, não um retorno ao campo. Mudanças de critério de classificação urbano/rural no Censo 2022 também podem pesar; não encontrei nota oficial específica do IBGE sobre Taquarituba.

O TCE-SP publica "grau de urbanização" de 91,14% para 2021 [S9], com base em estimativa SEADE; não é comparável com o Censo 2022.

Estado de SP em 2022: 96,82% urbano [oficial, S2b].

## 4. Área e densidade

- Área: 448,515 km² [oficial, S2c, 2022].
- Densidade: **54,29 hab/km²** [oficial, S2c, 2022].
- Estado de SP: 178,92 hab/km² [oficial, S2c, 2022].

## 5. Domicílios

- 8.369 domicílios particulares permanentes ocupados [oficial, S6, 2022].
- 2,77 moradores por domicílio (SP: 2,72) [oficial, S6, 2022].

## 6. Comparação regional

| Território | Pop. 2010 | Pop. 2022 | Cresc. a.a. 2010 a 2022 | Estim. 2025 | Área km² | Dens. hab/km² | % urbana 2022 |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Taquarituba** | 22.291 | 24.350 | 0,74% | 24.932 | 448,5 | 54,29 | 83,86 |
| Avaré | 82.934 | 92.805 | 0,94% | 96.450 | 1.213,1 | 76,51 | 94,96 |
| Itaí | 24.008 | 25.180 | 0,40% | 25.979 | 1.092,9 | 23,04 | 82,87 |
| Itaporanga | 14.549 | 14.085 | -0,27% | 14.245 | 508,0 | 27,73 | 74,68 |
| Coronel Macedo | 5.001 | 4.280 | -1,29% | 4.271 | 303,8 | 14,09 | 82,73 |
| Taguaí | 10.828 | 12.669 | 1,32% | 13.068 | 145,3 | 87,17 | 90,66 |
| Fartura | 15.320 | 16.641 | 0,69% | 17.029 | 429,2 | 38,77 | 80,85 |
| Estado de SP | 41.262.199 | 44.411.238 | 0,61% | 46.081.801 | 248.219,5 | 178,92 | 96,82 |

Tudo [oficial]: pop. 2010 [S1], pop. 2022 e taxa [S2], estimativa 2025 [S5], área e densidade [S2c], % urbana [S2b].

Leitura **[inferência]**:

- Taquarituba está no grupo que cresce, junto com Avaré, Taguaí e Fartura. Itaporanga e Coronel Macedo encolhem.
- Itaí e Taguaí também têm unidades prisionais, o que distorce a comparação de crescimento e de razão de sexo. Itaí tem razão de sexo 107,70, quase igual à de Taquarituba (107,29) [oficial, S12]. Não levantei a população carcerária desses municípios.

## Fontes

- [S1] IBGE, SIDRA tabela 202, "População residente por sexo e situação do domicílio" (Censos 1970, 1980, 1991, 2000, 2010). https://sidra.ibge.gov.br/tabela/202 (consulta via API em 20/10/2026).
- [S2] IBGE, SIDRA tabela 4709, Censo 2022: população, variação absoluta e taxa de crescimento geométrico 2010 a 2022. https://sidra.ibge.gov.br/tabela/4709
- [S2b] IBGE, SIDRA tabela 9923, Censo 2022: população por situação do domicílio. https://sidra.ibge.gov.br/tabela/9923
- [S2c] IBGE, SIDRA tabela 4714, Censo 2022: área e densidade demográfica. https://sidra.ibge.gov.br/tabela/4714
- [S3] IBGE, SIDRA tabela 9514, Censo 2022: população por sexo e idade. https://sidra.ibge.gov.br/tabela/9514
- [S4] IBGE, SIDRA tabela 1378, Censo 2010: população por sexo e idade. https://sidra.ibge.gov.br/tabela/1378
- [S5] IBGE, SIDRA tabela 6579, Estimativas de população (2019 a 2026), e IBGE Cidades, indicador 29171. https://sidra.ibge.gov.br/tabela/6579 e https://cidades.ibge.gov.br/brasil/sp/taquarituba/panorama
- [S6] IBGE, SIDRA tabela 4712, Censo 2022: domicílios e moradores. https://sidra.ibge.gov.br/tabela/4712
- [S7] SES-SP / CCD / GVE XVI Botucatu, "Portfólio do município Taquarituba", dez/2024. https://portal.saude.sp.gov.br/resources/ccd/homepage/2025/sim-sinasc/portfolios/gve-16/taquarituba.pdf
- [S8] Fundação SEADE, repositório de dados abertos, dataset "seade-fecundidade" (arquivo fecundidade_natalidade_municipios_serie.csv, atualizado em 06/2026). https://repositorio.seade.gov.br/dataset/seade-fecundidade
- [S9] TCE-SP, "Relatório do município Taquarituba" (dados 2021). https://www.tce.sp.gov.br/sites/default/files/rdm/taquarituba.pdf
- [S10] ALESP, Decreto nº 60.927, de 28/11/2014. https://www.al.sp.gov.br/repositorio/legislacao/decreto/2014/decreto-60927-28.11.2014.html
- [S11] ALESP, propositura de 2023 sobre denominação da Penitenciária de Taquarituba. https://www.al.sp.gov.br/spl/2023/02/Propositura/1000482812_1000619541_Propositura.pdf
- [S12] IBGE, SIDRA tabela 10097, Censo 2022: índice de envelhecimento, idade mediana e razão de sexo. https://sidra.ibge.gov.br/tabela/10097

Dados tabulares: `dados/populacao_serie_historica.csv`, `dados/taxas_crescimento.csv`, `dados/comparacao_regional_censo2022.csv`.
