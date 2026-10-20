# Taquarituba (SP): natalidade, fecundidade e mortalidade

Legenda: **[oficial]** número publicado pela fonte; **[cálculo]** conta minha só com números oficiais; **[inferência]** interpretação minha.

Fontes de dados vitais usadas:

- **DATASUS (SINASC e SIM)**: registro de saúde, por residência da mãe ou do falecido. Dados finais até 2024; 2025 preliminar; 2026 é prévia e o ano não terminou [D1], [D2], [D3].
- **SEADE**: série própria baseada nos cartórios de registro civil [S8], [S13], [S14]. Dá números um pouco diferentes do DATASUS (ex.: 2022, 270 nascidos na SEADE contra 275 no DATASUS).
- **SES-SP, Portfólio do município (dez/2024)**: análise do SIM/SINASC 2014 a 2023 com dados preliminares [S7].

As taxas por mil habitantes usam como denominador o Censo (2000, 2010, 2022) ou a estimativa IBGE (2019 a 2021, 2024, 2025) [S2], [S5].

**Atenção [inferência]**: os ~1.200 presos (homens adultos, quase sem nascimentos e com poucos óbitos) entram no denominador. Isso puxa para baixo as taxas brutas de natalidade e mortalidade em cerca de 5% em relação à população "civil".

## 1. Nascimentos

### 1.1 Série de nascidos vivos (DATASUS, por residência da mãe) [oficial, D1]

| Ano | Nascidos vivos | Taxa bruta de natalidade (por mil) [cálculo] |
|---|---:|---:|
| 2000 | 384 | 17,5 |
| 2005 | 357 | |
| 2010 | 330 | 14,8 |
| 2015 | 338 | |
| 2019 | 331 | 14,3 |
| 2020 | 297 | 12,8 |
| 2021 | 287 | 12,3 |
| **2022** | **275** | **11,3** |
| 2023 | 286 | |
| 2024 | 300 | 12,1 |
| 2025 (preliminar) | 270 | 10,8 |

Série completa 2000 a 2026 em `dados/estatisticas_vitais_datasus_2000_2026.csv`.

- Queda de cerca de 28% no número anual de nascimentos entre 2000 (384) e 2022 (275) [cálculo, D1].
- Pela SEADE, a taxa de natalidade de 2022 foi 11,1 por mil (270 / 24.335) [cálculo, S8].
- Estado de SP, 2022: 512.520 nascidos, taxa de 11,5 por mil [cálculo, D1 e S2]. Taquarituba está praticamente igual ao estado.

### 1.2 Fecundidade

**Não encontrei taxa de fecundidade total (TFT) oficial para o município.** A SEADE publica TFT só para o estado e para as Regiões Administrativas [S8b]. Fiz uma estimativa:

| Idade da mãe | Nascidos/ano (média 2021 a 2023) [D1] | Mulheres no Censo 2022 [S3] | Taxa específica por mil [cálculo] | RA Itapeva 2022 [oficial, S8b] | Estado de SP 2022 [oficial, S8b] |
|---|---:|---:|---:|---:|---:|
| 15 a 19 (inclui 10 a 14) | 30,3 | 752 | 40,3 | 45,6 | 29,9 |
| 20 a 24 | 82,3 | 837 | 98,4 | 91,3 | 71,4 |
| 25 a 29 | 79,7 | 876 | 90,9 | 93,0 | 78,0 |
| 30 a 34 | 57,0 | 891 | 64,0 | 68,4 | 68,3 |
| 35 a 39 | 25,3 | 860 | 29,5 | 40,7 | 44,2 |
| 40 a 44 | 7,7 | 932 | 8,2 | 11,4 | 13,0 |
| 45 a 49 | 0,3 | 812 | 0,4 | 0,5 | 0,9 |
| **TFT (filhos por mulher)** | | | **≈ 1,66 [estimativa]** | **1,75** | **1,53** |

- TFT estimada de Taquarituba: **cerca de 1,6 a 1,7 filho por mulher** (1,66 com a média 2021 a 2023; 1,61 só com 2022) [cálculo, estimativa]. Abaixo do nível de reposição (2,1).
- Teste do método: a mesma conta para o estado de SP em 2022 dá 1,53, igual ao número oficial da SEADE (1,53) [cálculo e S8b].
- RA Itapeva em 2024: TFT 1,69; Estado de SP em 2024: 1,43 [oficial, S8b].
- Taxa de fecundidade geral (nascidos / mulheres de 15 a 49 anos) em 2022, série SEADE: 45,3 por mil (270 / 5.954) [cálculo, S8]; estado de SP 43,5 por mil [cálculo, S8].

**[inferência]** Taquarituba tem fecundidade acima da média paulista e um padrão mais jovem: as mulheres de 20 a 24 anos têm mais filhos que a média do estado, e as de 35 anos ou mais têm menos.

### 1.3 Gravidez na adolescência e parto

- Mães com menos de 20 anos: 10,3% dos nascidos de 2021 a 2024 (118 de 1.148) [cálculo, D1].
- Mães com menos de 19 anos: 9,8% dos nascidos de 2014 a 2023 [oficial, S7].
- Taxa de fecundidade de 15 a 19 anos: ~40 por mil, contra 29,9 no estado (2022) [cálculo e S8b].
- Cesáreas: 61,8% dos partos de 2014 a 2023 e 67,7% de 2021 a 2023 [oficial, S7].
- Pré-natal com 7 ou mais consultas: 91,3% (2014 a 2023) [oficial, S7].
- 82,6% dos partos de mães de Taquarituba ocorreram no próprio município (2014 a 2023); 9,5% em Botucatu e 4,7% em Avaré [oficial, S7].

## 2. Mortalidade geral

### 2.1 Série de óbitos (DATASUS, por residência) [oficial, D2]

| Ano | Óbitos | Taxa bruta de mortalidade (por mil) [cálculo] | Saldo nascimentos menos óbitos [cálculo] |
|---|---:|---:|---:|
| 2000 | 142 | 6,5 | +242 |
| 2010 | 145 | 6,5 | +185 |
| 2015 | 220 | | +118 |
| 2019 | 180 | 7,8 | +151 |
| 2020 | 204 | 8,8 | +93 |
| 2021 | 298 | 12,8 | **-11** |
| **2022** | **242** | **9,9** | +33 |
| 2023 | 210 | | +76 |
| 2024 | 210 | 8,4 | +90 |
| 2025 (preliminar) | 196 | 7,9 | +74 |

- Pela SEADE, a taxa de mortalidade geral foi 10,0 por mil em 2022 e 8,6 por mil em 2024 [oficial, S13].
- Estado de SP, 2022: 354.056 óbitos, 8,0 por mil [cálculo, D2 e S2].
- O número anual de óbitos subiu de ~145 (2000 a 2010) para ~210 (2023 a 2024). É o efeito do envelhecimento [inferência].
- 2021 foi o único ano em que morreram mais pessoas do que nasceram (-11), por causa da covid-19 [cálculo, D1 e D2; atribuição à covid: S7].
- **Crescimento vegetativo de 2010 a 2021: +1.429** [cálculo, D1 e D2]. O saldo anual caiu de +150 a +185 (2010 a 2019) para +30 a +90 (2022 a 2025).

**Mortalidade de idosos (SEADE)**: em 2022, 44,3 óbitos por mil pessoas com 60 anos ou mais em Taquarituba, contra 34,7 no estado (soma dos municípios) [oficial para Taquarituba, S13; cálculo para SP]. Em 2024 a diferença sumiu: 32,4 contra 32,0 [S13 e cálculo]. **[inferência]** A taxa bruta alta de 2022 foi um pico pós-covid (38 óbitos por doenças respiratórias, o maior da série), não um patamar.

### 2.2 Esperança de vida

- Taquarituba: 69,51 anos (2000) e **73,65 anos (2010)** [oficial, S15, Atlas Brasil].
- Estado de SP: 75,69 anos (2010) [oficial, S15]. Taquarituba estava 2 anos abaixo.
- Estado de SP, série SEADE: 76,3 anos (2022) e 76,8 anos (2024); interior do estado, 76,0 (2022) [oficial, S14].
- **Não encontrei esperança de vida municipal posterior a 2010.**

### 2.3 Principais causas de óbito (DATASUS, capítulos da CID-10) [oficial, D2]

| Capítulo CID-10 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 (prel.) | % de 2022 a 2024 [cálculo] |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| IX. Aparelho circulatório | 49 | 52 | 59 | 71 | 49 | 43 | 58 | **24,6%** |
| II. Neoplasias (câncer) | 29 | 36 | 26 | 32 | 34 | 41 | 33 | **16,2%** |
| X. Aparelho respiratório | 18 | 18 | 23 | 38 | 31 | 23 | 24 | **13,9%** |
| XX. Causas externas | 12 | 15 | 17 | 13 | 15 | 21 | 19 | 7,4% |
| IV. Endócrinas e metabólicas (inclui diabetes) | 15 | 31 | 14 | 12 | 16 | 19 | 13 | 7,1% |
| XI. Aparelho digestivo | 13 | 9 | 19 | 13 | 17 | 13 | 11 | 6,5% |
| XVIII. Mal definidas | 9 | 7 | 11 | 16 | 16 | 11 | 10 | 6,5% |
| I. Infecciosas e parasitárias (inclui covid) | 7 | 9 | **108** | 19 | 10 | 14 | 10 | 6,5% |
| XIV. Aparelho geniturinário | 11 | 10 | 10 | 11 | 10 | 12 | 6 | 5,0% |
| Outros capítulos | 17 | 17 | 11 | 17 | 12 | 13 | 12 | |
| **Total** | 180 | 204 | 298 | 242 | 210 | 210 | 196 | 662 óbitos |

Tabela completa: `dados/obitos_por_causa_cid10_2019_2025.csv`.

Destaques do portfólio da SES-SP (SIM, 2014 a 2023, dados preliminares) [oficial, S7]:

- De 20 a 39 anos, a principal causa de morte são as **causas externas** (acidentes e violência): 54 dos 133 óbitos nessa faixa.
- De 40 a 59 anos: aparelho circulatório (93), neoplasias (60) e causas externas (49).
- 60 anos ou mais: aparelho circulatório (407), neoplasias (198), respiratório (184).
- Menores de 20 anos: afecções perinatais (27) e causas externas (10).
- **34,5% dos óbitos tiveram causa básica "garbage"** (mal definida ou pouco útil para prevenção), contra meta de no máximo 10%.
- 120 óbitos codificados como covid-19 (B34.2) entre 2014 e 2023.
- Mortalidade prematura (30 a 69 anos) por doenças crônicas não transmissíveis: 304,2 por 100 mil em 2021; pico de 448,8 em 2020.
- 58,0% dos óbitos ocorreram na Santa Casa de Taquarituba; 22,2% fora de estabelecimento de saúde.

## 3. Mortalidade infantil

Com ~300 nascimentos por ano, cada óbito de bebê muda a taxa em ~3,3 pontos. A taxa anual oscila muito; a média de 5 anos é o número que importa [inferência].

### 3.1 Série (DATASUS) [oficial para óbitos e nascidos, D1 e D3; taxa = cálculo]

| Ano | Óbitos menores de 1 ano | Nascidos vivos | Taxa por mil [cálculo] |
|---|---:|---:|---:|
| 2019 | 4 | 331 | 12,1 |
| 2020 | 5 | 297 | 16,8 |
| 2021 | 2 | 287 | 7,0 |
| 2022 | 4 | 275 | 14,5 |
| 2023 | 2 | 286 | 7,0 |
| 2024 | 1 | 300 | 3,3 |
| 2025 (prel.) | 2 | 270 | 7,4 |

Médias de 5 anos [cálculo, D1 e D3]:

| Período | Taxa de mortalidade infantil (por mil) |
|---|---:|
| 2000 a 2004 | 16,3 |
| 2005 a 2009 | 15,1 |
| 2010 a 2014 | 10,8 |
| 2015 a 2019 | 10,6 |
| **2020 a 2024** | **9,7** |

- Estado de SP, 2020 a 2024: 10,8 por mil [cálculo, D1 e D3]. Taquarituba está um pouco melhor que o estado.
- SEADE (cartórios) registra 3 óbitos infantis em 2022 (taxa 11,1) e 1 em 2024 (3,4) [S13b, cálculo]. O DATASUS registra 4 em 2022.
- IBGE Cidades publica 12,3 por mil como média 2012 a 2014 [oficial, S16].
- Atlas Brasil (estimativa censitária): 24,6 por mil em 2000 e 16,9 por mil em 2010 [oficial, S15]. Método diferente, não comparável com a série do DATASUS.
- 78,1% dos 32 óbitos infantis de 2014 a 2023 eram evitáveis, todos ligados à atenção na gestação, no parto ou ao recém-nascido [oficial, S7].

## 4. Comparação regional (2022)

| Território | Nascidos 2022 | Óbitos 2022 | Natalidade por mil | Mortalidade por mil | Saldo por mil | Mort. infantil média 2020 a 2024 |
|---|---:|---:|---:|---:|---:|---:|
| **Taquarituba** | 275 | 242 | 11,3 | 9,9 | +1,4 | **9,7** |
| Avaré | 1.087 | 833 | 11,7 | 9,0 | +2,7 | 12,8 |
| Itaí | 342 | 222 | 13,6 | 8,8 | +4,8 | 14,9 |
| Itaporanga | 170 | 172 | 12,1 | 12,2 | -0,1 | 6,0 |
| Coronel Macedo | 41 | 65 | 9,6 | 15,2 | -5,6 | 17,0 |
| Taguaí | 150 | 116 | 11,8 | 9,2 | +2,7 | 9,0 |
| Fartura | 179 | 177 | 10,8 | 10,6 | +0,1 | 6,6 |
| Estado de SP | 512.520 | 354.056 | 11,5 | 8,0 | +3,6 | 10,8 |

Nascidos e óbitos: [oficial, D1, D2, D3]. Taxas: [cálculo] com população do Censo 2022 [S2]. Em municípios pequenos (Coronel Macedo tem ~45 nascimentos por ano), as taxas de um ano só são muito instáveis. Arquivo: `dados/comparacao_vitais_regiao_2022.csv`.

## Fontes

- [D1] Ministério da Saúde, DATASUS TabNet, SINASC, "Nascidos vivos, São Paulo", por residência da mãe. http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sinasc/cnv/nvsp.def (consulta em 20/10/2026; dados finais até 2024, extração 02/12/2025; 2025 preliminar, extração 28/07/2026; 2026 2ª prévia, extração 01/09/2026).
- [D2] DATASUS TabNet, SIM, "Óbitos gerais, São Paulo", CID-10, por residência. http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sim/cnv/obt10sp.def (mesma consulta e mesmas datas de extração).
- [D3] DATASUS TabNet, SIM, "Óbitos infantis, São Paulo". http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sim/cnv/inf10sp.def (idem).
- [S2] IBGE, Censo 2022, SIDRA tabela 4709. https://sidra.ibge.gov.br/tabela/4709
- [S3] IBGE, Censo 2022, SIDRA tabela 9514 (população por sexo e idade). https://sidra.ibge.gov.br/tabela/9514
- [S5] IBGE, Estimativas de população, SIDRA tabela 6579. https://sidra.ibge.gov.br/tabela/6579
- [S7] SES-SP / CCD / GVE XVI Botucatu, "Portfólio do município Taquarituba", dez/2024 (SIM/SINASC 2014 a 2023, base de 22/08/2024). https://portal.saude.sp.gov.br/resources/ccd/homepage/2025/sim-sinasc/portfolios/gve-16/taquarituba.pdf
- [S8] Fundação SEADE, "Fecundidade e natalidade por municípios" (fecundidade_natalidade_municipios_serie.csv, 2000 a 2024). https://repositorio.seade.gov.br/dataset/seade-fecundidade
- [S8b] Fundação SEADE, "Fecundidade total, Estado de São Paulo e regiões" (fecundidade_total.csv, 2000 a 2024). https://repositorio.seade.gov.br/dataset/seade-fecundidade
- [S13] Fundação SEADE, "Mortalidade geral no Estado de São Paulo, 2000 a 2024" (mortalidade_geral.csv). https://repositorio.seade.gov.br/dataset/mortalidade-no-estado-de-sao-paulo
- [S13b] Fundação SEADE, "Óbitos infantis no ESP" (obitosinfantis_periodo.csv). https://repositorio.seade.gov.br/dataset/mortalidade-infantil
- [S14] Fundação SEADE, "Esperança de vida" (esperanca_vida.csv). https://repositorio.seade.gov.br/dataset/esperanca-de-vida
- [S15] Atlas do Desenvolvimento Humano no Brasil (PNUD, Ipea, FJP), perfil de Taquarituba, Censos 2000 e 2010. https://www.atlasbrasil.org.br/perfil/municipio/355380
- [S16] IBGE Cidades, Panorama de Taquarituba, indicador "Mortalidade infantil" (média 2012 a 2014). https://cidades.ibge.gov.br/brasil/sp/taquarituba/panorama

Arquivos: `dados/estatisticas_vitais_datasus_2000_2026.csv`, `dados/seade_vitais_taquarituba_2000_2024.csv`, `dados/fecundidade_estimada.csv`, `dados/obitos_por_causa_cid10_2019_2025.csv`, `dados/comparacao_vitais_regiao_2022.csv`.
