# Taquarituba (SP): eleitorado

Data de referência: 20/10/2026.

Fontes:
- Perfil do eleitorado, arquivo "ATUAL" do TSE, gerado em 01/10/2026: https://cdn.tse.jus.br/estatistica/sead/odsele/perfil_eleitorado/perfil_eleitorado_ATUAL.zip (portal: https://dadosabertos.tse.jus.br/dataset/eleitorado-atual)
- Série de eleitores aptos: TSE detalhe_votacao_munzona (1996 a 2022, https://cdn.tse.jus.br/estatistica/sead/odsele/detalhe_votacao_munzona/) e resultados oficiais 2024 e 2026 (https://resultados.tse.jus.br/oficial/ele2024/619/dados/sp/sp71773-c0011-e000619-u.json e https://resultados.tse.jus.br/oficial/ele2026/6257/dados/sp/sp71773-c0001-e006257-u.json).
- População: IBGE Censo 2022, 24.350 habitantes; estimativa 2025, 24.932 (https://www.ibge.gov.br/cidades-e-estados/sp/taquarituba.html, valores reproduzidos em https://pt.wikipedia.org/wiki/Taquarituba).
- CSVs: `dados/eleitorado_perfil_out2026.csv`, `dados/comparecimento_1996_2026.csv`.

## 1. Tamanho do eleitorado

- **18.117 eleitores** no cadastro do TSE em 01/10/2026; 17.478 com biometria (96,5%); 252 com deficiência declarada.
- Na eleição de 04/10/2026 o TSE registrou 18.080 aptos, com comparecimento de 14.294 (79,06%).
- Relação eleitores/população (inferência): cerca de 73% da população estimada de 2025.

### Evolução de eleitores aptos

| Ano | Aptos | Comparecimento | % comparecimento |
|---|---|---|---|
| 1996 | 14.399 | 12.572 | 87,3 |
| 1998 | 14.837 | 12.144 | 81,8 |
| 2000 | 15.747 | 13.698 | 87,0 |
| 2002 | 16.168 | 12.262 | 75,8 |
| 2004 | 16.951 | 14.381 | 84,8 |
| 2006 | 17.276 | 13.799 | 79,9 |
| 2008 | 17.674 | 14.957 | 84,6 |
| 2010 | 18.180 | 14.337 | 78,9 |
| 2012 | 18.440 | 15.243 | 82,7 |
| 2014 | 18.604 | 14.659 | 78,8 |
| 2016 | 18.808 | 15.310 | 81,4 |
| 2018 | 16.300 | 14.043 | 86,2 |
| 2020 | 16.998 | 13.556 | 79,8 |
| 2022 | 17.365 | 14.063 | 81,0 |
| 2024 | 18.044 | 14.761 | 81,8 |
| 2026 | 18.080 | 14.294 | 79,1 |

Inferência: a queda de 18.808 (2016) para 16.300 (2018) coincide com o período de revisão biométrica obrigatória, que cancelou títulos não recadastrados em vários municípios paulistas; não localizei documento específico do TSE sobre Taquarituba. Comparecimento em eleição municipal costuma ser maior que em eleição geral.

## 2. Perfil (TSE, 01/10/2026, total 18.117)

### Sexo
| Sexo | Eleitores | % |
|---|---|---|
| Feminino | 9.397 | 51,9 |
| Masculino | 8.720 | 48,1 |

### Faixa etária
| Faixa | Eleitores | % |
|---|---|---|
| 16 e 17 anos (voto facultativo) | 171 | 0,9 |
| 18 a 20 anos | 709 | 3,9 |
| 21 a 24 | 1.127 | 6,2 |
| 25 a 29 | 1.628 | 9,0 |
| 30 a 34 | 1.708 | 9,4 |
| 35 a 39 | 1.728 | 9,5 |
| 40 a 44 | 1.784 | 9,8 |
| 45 a 49 | 1.714 | 9,5 |
| 50 a 54 | 1.547 | 8,5 |
| 55 a 59 | 1.451 | 8,0 |
| 60 a 64 | 1.363 | 7,5 |
| 65 a 69 | 1.238 | 6,8 |
| 70 a 74 | 901 | 5,0 |
| 75 anos ou mais | 1.047 | 5,8 |

O arquivo registra 1 eleitor na faixa "15 anos" (alistamento antecipado). Eleitores com 60 anos ou mais: 4.549 (25,1%). Voto facultativo segundo o TSE (16 e 17 anos, 70 anos ou mais e analfabetos): 2.374 (13,1%).

### Escolaridade declarada
| Grau | Eleitores | % |
|---|---|---|
| Analfabeto | 433 | 2,4 |
| Lê e escreve | 550 | 3,0 |
| Fundamental incompleto | 5.756 | 31,8 |
| Fundamental completo | 1.050 | 5,8 |
| Médio incompleto | 2.704 | 14,9 |
| Médio completo | 5.149 | 28,4 |
| Superior incompleto | 762 | 4,2 |
| Superior completo | 1.713 | 9,5 |

### Estado civil
Solteiro 50,9%; casado 38,2%; divorciado 6,5%; viúvo 3,4%; separado judicialmente 1,1%.

### Cor ou raça
82,5% não informado; entre os que informaram: branca 2.410, parda 621, preta 137, amarela 9, indígena 1. Dado pouco útil pela baixa taxa de resposta.

## 3. Leitura (inferência)

- Eleitorado envelhecido e de escolaridade média baixa: 43% não passaram do fundamental (somando analfabetos, "lê e escreve" e fundamental completo ou incompleto); só 9,5% têm superior completo.
- Leve maioria feminina (51,9%).
- Esse perfil (interior, idade elevada, escolaridade média, base agrícola e de serviços) é compatível com o voto majoritariamente conservador registrado em `eleicoes-gerais-e-perfil-ideologico.md`. A correlação é inferida, não medida aqui (o TSE não cruza perfil com voto).
- Número de seções e locais: em 2022 havia 64 seções (TSE detalhe 2022). A 236ª Zona Eleitoral tem sede em Taquarituba (https://farolnoticias.com.br/nova-sede-do-cartorio-eleitoral-na-236a-zona-de-taquarituba-e-inaugurada/).
