# Orçamento: LOA, LDO e PPA

Valores em R$ correntes. Fontes com URL em cada tabela. CSV: [dados/orcamento_loa_execucao_2011_2026.csv](dados/orcamento_loa_execucao_2011_2026.csv) e [dados/loa_2026_por_funcao.csv](dados/loa_2026_por_funcao.csv).

## 1. Série histórica: LOA inicial x execução (2011 a 2026)

| Ano | Lei da LOA | Receita prevista na LOA | Despesa fixada na LOA | Dotação atualizada | Receita realizada | Despesa empenhada | Resultado (realizado menos empenhado) |
|---|---|---:|---:|---:|---:|---:|---:|
| 2011 | Lei 1.630/2010 | 37,82 mi | 37,82 mi | n/l | n/l | n/l | TCE: superávit 6,80% |
| 2012 | Lei 1.651/2011 | 41,88 mi | 41,88 mi | n/l | n/l | n/l | TCE: déficit 2,57% |
| 2013 | Lei 1.679/2012 | 45,93 mi | 45,93 mi | n/l | 53,71 mi | 50,74 mi | +2,97 mi |
| 2014 | Lei 1.705/2013 | 56,51 mi | 56,51 mi | n/l | 62,56 mi | 62,60 mi | -0,03 mi |
| 2015 | Lei 1.721/2014 | 71,06 mi | 71,06 mi | n/l | 65,04 mi | 64,52 mi | +0,51 mi |
| 2016 | Lei 1.742/2015 | 67,38 mi | 67,38 mi | n/l | 67,46 mi | 64,03 mi | +3,43 mi |
| 2017 | Lei 1.763/2016 | 72,50 mi | 72,50 mi | n/l | 72,35 mi | 67,15 mi | +5,20 mi |
| 2018 | Lei 1.776/2017 | 76,57 mi | 74,99 mi | 81,55 mi | 81,35 mi | 72,65 mi | +8,69 mi |
| 2019 | Lei 1.792/2018 | 83,32 mi | 83,02 mi | 90,37 mi | 86,85 mi | 81,18 mi | +5,67 mi |
| 2020 | Lei 1.809/2019 | 89,08 mi | 88,83 mi | 97,65 mi | 92,28 mi | 87,45 mi | +4,83 mi |
| 2021 | Lei 1.822/2020 | 95,11 mi | 95,11 mi | 112,31 mi | 112,30 mi | 103,22 mi | +9,08 mi |
| 2022 | Lei 1.864/2021 | 113,28 mi | 112,24 mi | 143,48 mi | 127,03 mi | 129,08 mi | -2,04 mi |
| 2023 | Lei 1.903/2022 | 139,55 mi | 139,55 mi | 167,82 mi | 151,56 mi | 152,22 mi | -0,65 mi |
| 2024 | Lei 1.937/2023 | 152,72 mi | 152,72 mi | 171,48 mi | 166,52 mi | 164,64 mi | +1,88 mi |
| 2025 | lei não localizada no portal | 160,98 mi | 160,98 mi | 203,63 mi | 196,01 mi (inclui 18 mi de empréstimo) | 181,08 mi | +14,94 mi |
| **2026** | **Lei 1.998/2025** | **192,45 mi** | **192,45 mi** | **222,01 mi (ago)** | **133,20 mi (jan-ago)** | **177,79 mi (jan-ago)** | parcial |

n/l = não localizado.

Fontes:
- LOAs 2011 a 2017: texto das leis no portal da Prefeitura, [2011](https://www.taquarituba.sp.gov.br/legislacao/download-lei/1850/), [2012](https://www.taquarituba.sp.gov.br/legislacao/download-lei/1768/), [2013](https://www.taquarituba.sp.gov.br/legislacao/download-lei/1727/), [2014](https://www.taquarituba.sp.gov.br/legislacao/download-lei/1663/), [2015](https://www.taquarituba.sp.gov.br/legislacao/download-lei/1878/), [2016](https://www.taquarituba.sp.gov.br/legislacao/download-lei/2601/), [2017](https://www.taquarituba.sp.gov.br/legislacao/download-lei/2888/). Os PDFs são digitalizados; os totais foram lidos do art. 2º.
- LOAs 2018 a 2026 e dotação atualizada: Siconfi RREO Anexo 01, 6º bimestre, por exemplo [2025](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?an_exercicio=2025&nr_periodo=6&co_tipo_demonstrativo=RREO&no_anexo=RREO-Anexo%2001&co_esfera=M&id_ente=3553807) e [2026, 4º bim](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?an_exercicio=2026&nr_periodo=4&co_tipo_demonstrativo=RREO&no_anexo=RREO-Anexo%2001&co_esfera=M&id_ente=3553807); 2019 veio do RREO Simplificado ([API](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?an_exercicio=2019&nr_periodo=6&co_tipo_demonstrativo=RREO%20Simplificado&co_esfera=M&id_ente=3553807)).
- Execução 2013 a 2025: Siconfi DCA, Anexo I-C (receita, total realizado menos dedução para o FUNDEB, incluindo intraorçamentárias) e Anexo I-D (despesa empenhada total), por exemplo [DCA 2025 receitas](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2025&no_anexo=DCA-Anexo%20I-C&id_ente=3553807). O resultado é cálculo próprio e pode diferir do apurado pelo TCE (ver [contas-e-tce.md](contas-e-tce.md)).

**Tendência (cálculo próprio):** a LOA passou de R$ 37,82 mi (2011) para R$ 192,45 mi (2026), alta nominal de 5,1 vezes. De 2021 em diante o orçamento cresce em degraus de 10% a 20% ao ano. A diferença entre dotação inicial e atualizada também cresce: em 2025 a dotação final ficou 26% acima da LOA (203,63 mi contra 160,98 mi), puxada por excesso de arrecadação, superávit de anos anteriores e pelo empréstimo.

**Análise:** a LOA vem sendo sistematicamente subestimada. Em 2025 a receita realizada ficou 22% acima da previsão (196,01 contra 160,98 mi, com o empréstimo). Na prática o orçamento aprovado pela Câmara vira piso, e boa parte da alocação real é feita depois, por créditos adicionais. O TCE já apontou isso em 2021: a LOA permitia abrir créditos por decreto até 15% e a LDO permitia remanejar 15%, contra IPCA de 2,13% ([RDM TCE-SP](https://www.tce.sp.gov.br/sites/default/files/rdm/taquarituba.pdf)). A LOA 2026 subiu o limite para 20% (art. 3º da [Lei 1.998/2025](https://www.taquarituba.sp.gov.br/legislacao/download-lei/13497/)).

## 2. LOA 2026 (Lei 1.998, de 23/12/2025)

Fonte de toda a seção: [Lei 1.998/2025](https://www.taquarituba.sp.gov.br/legislacao/download-lei/13497/).

- Receita total estimada: **R$ 192.450.000,00**, sendo orçamento fiscal R$ 153.960.111,70 e seguridade social R$ 38.489.888,30.
- Administração direta R$ 169.425.008,51; administração indireta (Capstuba, o RPPS) R$ 23.024.991,49.

### Receita da administração direta

| Item | Valor |
|---|---:|
| Impostos, taxas e contribuição de melhoria | 25.366.092,51 |
| Contribuições | 2.200.000,00 |
| Receita patrimonial | 1.057.000,00 |
| Receita de serviços | 35.000,00 |
| Transferências correntes | 155.508.416,00 |
| Outras receitas correntes | 1.491.000,00 |
| (-) Deduções para o FUNDEB | -18.910.000,00 |
| Operação de crédito | 2.277.500,00 |
| Alienação de bens | 350.000,00 |
| Transferência de capital | 50.000,00 |
| **Total** | **169.425.008,51** |

### Despesa da administração direta por categoria

| Item | Valor |
|---|---:|
| Pessoal e encargos | 60.517.145,81 |
| Juros da dívida | 5.000,00 |
| Outras despesas correntes | 96.583.716,26 |
| Investimentos | 9.121.418,35 |
| Amortização da dívida | 1.480.000,00 |
| Reserva de contingência | 1.717.728,09 |

### Despesa por função (total do município)

| Função | R$ | % |
|---|---:|---:|
| 12 Educação | 59.260.666,90 | 30,79 |
| 10 Saúde | 45.666.849,41 | 23,73 |
| 09 Previdência Social | 21.873.741,92 | 11,37 |
| 04 Administração | 18.531.163,60 | 9,63 |
| 15 Urbanismo | 12.801.000,00 | 6,65 |
| 08 Assistência Social | 11.483.832,90 | 5,97 |
| 06 Segurança Pública | 4.020.500,00 | 2,09 |
| 01 Legislativa | 3.865.000,00 | 2,01 |
| 17 Saneamento | 3.355.000,00 | 1,74 |
| 99 Reserva de Contingência | 2.868.977,66 | 1,49 |
| 27 Desporto e Lazer | 2.282.433,80 | 1,19 |
| 13 Cultura | 2.005.000,00 | 1,04 |
| 26 Transporte | 1.771.000,00 | 0,92 |
| 18 Gestão Ambiental | 1.023.633,81 | 0,53 |
| 20 Agricultura | 916.200,00 | 0,48 |
| 28 Encargos Especiais | 480.000,00 | 0,25 |
| 22 Indústria (inclui turismo) | 245.000,00 | 0,13 |
| **Total** | **192.450.000,00** | 100 |

Percentuais: cálculo próprio.

### Maiores programas da LOA 2026

| Programa | R$ |
|---|---:|
| 0029 Sistema Municipal de Saúde Pública | 35.853.186,69 |
| 0037 FUNDEB na Construção de uma Educação Transformadora | 25.100.000,00 |
| 0027 Fundo de Aposentadoria e Pensão | 21.873.741,92 |
| 0025 Infraestrutura Urbana | 12.801.000,00 |
| 0034 Transporte para Frequência Escolar | 12.000.000,00 |
| 0033 Alimentação Escolar Saudável | 11.000.000,00 |
| 0001 Gestão Financeira Eficiente | 10.804.774,79 |
| 0021 Rede de Proteção Social, Cidadania e Inclusão | 10.139.366,90 |
| 0030 Estratégia Saúde da Família | 8.093.666,91 |
| 0035 Aprendizagem com Equidade no Ensino Fundamental | 5.943.200,00 |
| 0036 Primeira Infância com Equidade e Proteção | 5.217.466,90 |
| 0018 GCM em Ação | 1.820.000,00 |
| 0024 Descubra Taquarituba (turismo) | 245.000,00 |
| 0002 Desenvolvimento Econômico | 355.966,90 |

**Análise:** a LOA 2026 dá R$ 245 mil ao turismo e R$ 356 mil a desenvolvimento econômico, contra R$ 12 mi só em transporte escolar. O discurso de emprego e turismo dos planos de governo (ver [../06-futuro/planos-de-governo.md](../06-futuro/planos-de-governo.md)) não aparece com peso no orçamento.

### Execução de 2026 até agosto (RREO 4º bimestre)

- Receita realizada: R$ 133,20 mi (69,2% da previsão anual de R$ 192,45 mi).
- Superávit financeiro de 2025 usado para créditos adicionais: R$ 19,40 mi.
- Dotação atualizada: R$ 222,01 mi (15,4% acima da LOA; cálculo próprio).
- Despesa empenhada: R$ 177,79 mi; liquidada: R$ 129,50 mi; paga: R$ 122,69 mi.

Fonte: [Siconfi RREO 2026, 4º bimestre](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?an_exercicio=2026&nr_periodo=4&co_tipo_demonstrativo=RREO&no_anexo=RREO-Anexo%2001&co_esfera=M&id_ente=3553807).

## 3. LDO

| Exercício | Lei | Data | Link |
|---|---|---|---|
| 2019 | Lei 1.789/2018 | 24/07/2018 | [detalhe](https://www.taquarituba.sp.gov.br/legislacao/detalhe/4783/x) |
| 2020 | Lei 1.800/2019 | 24/06/2019 | [detalhe](https://www.taquarituba.sp.gov.br/legislacao/detalhe/5760/x) |
| 2021 | Lei 1.818/2020 | 05/08/2020 | [detalhe](https://www.taquarituba.sp.gov.br/legislacao/detalhe/6834/x) |
| 2025 | Lei 1.949/2024 | 15/07/2024 | [detalhe](https://www.taquarituba.sp.gov.br/legislacao/detalhe/10971/x) |
| 2026 | Lei 1.997/2025 | 15/10/2025 | [texto](https://www.taquarituba.sp.gov.br/legislacao/download-lei/13343/) |
| 2027 | Lei 2.016/2026 | 03/09/2026 | [texto](https://www.taquarituba.sp.gov.br/legislacao/download-lei/14229/) |

LDOs de 2022 a 2024 não apareceram na busca do portal (a Lei 1.841/2021, LDO 2022, é citada pela [Lei 1.862/2021](https://www.taquarituba.sp.gov.br/legislacao/detalhe/8987/x)).

As LDOs 2026 e 2027 seguem o mesmo modelo: organização do orçamento, diretrizes de elaboração e execução, dívida e precatórios, mudanças tributárias e despesas com pessoal, com metas fiscais conforme a Portaria STN 699/2023. Observação: a LDO 2026 foi sancionada em 15/10/2025, junto com o PPA, ou seja, depois do prazo usual (a LDO costuma ser votada antes do recesso de julho). Fonte: [Lei 1.997/2025](https://www.taquarituba.sp.gov.br/legislacao/download-lei/13343/).

## 4. PPA 2026-2029 (Lei 1.996, de 15/10/2025)

Fonte: [Lei 1.996/2025](https://www.taquarituba.sp.gov.br/legislacao/download-lei/13342/). Anexos: I (evolução da receita), II (programas) e III (programas, eixos, ações, metas).

### Receita projetada no PPA (Anexo I, consolidado)

| Item | 2026 | 2027 | 2028 | 2029 |
|---|---:|---:|---:|---:|
| Receitas correntes | 223.558.950,75 | 241.671.694,05 | 255.794.598,98 | 266.151.775,03 |
| Impostos, taxas e contrib. melhoria | 27.777.541,20 | 30.020.034,60 | 31.959.096,36 | 33.243.620,34 |
| IPTU | 7.509.014,47 | 8.179.208,41 | 8.607.000,00 | 8.960.000,00 |
| ITBI | 2.738.400,34 | 3.204.373,02 | 3.506.000,00 | 3.607.000,00 |
| FPM | 64.685.623,78 | 67.000.000,00 | 68.100.000,00 | 68.100.000,00 |
| ICMS | 46.953.845,03 | 47.000.000,00 | 51.050.000,00 | 52.000.000,00 |
| IPVA | 8.669.567,91 | 9.000.000,00 | 10.000.000,00 | 11.765.163,77 |
| FUNDEB | 24.000.000,00 | 30.000.000,00 | 31.000.000,00 | 31.250.000,00 |
| SUS (União) | 15.355.884,42 | 20.584.217,13 | 22.417.632,94 | 24.956.694,91 |
| Receitas de capital | 603.276,17 | 947.897,10 | 1.507.339,83 | 2.415.354,23 |
| (-) Deduções FUNDEB | -22.936.085,43 | -25.000.000,00 | -27.000.000,00 | -35.380.194,78 |
| **Total** | **201.226.141,49** | **217.619.591,15** | **230.301.938,81** | **233.186.934,48** |

**Análise:** o PPA projeta 2026 em R$ 201,2 mi, mas a LOA 2026 aprovada dois meses depois ficou em R$ 192,45 mi. O FPM de R$ 64,7 mi previsto no PPA para 2026 é muito maior que o realizado em 2025 (R$ 45,36 mi, [DCA 2025](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2025&no_anexo=DCA-Anexo%20I-C&id_ente=3553807)); o número parece inconsistente e deve ser lido com cautela.

### Ações de investimento identificadas no PPA (Anexo III)

| Ação | Custo previsto | Cronograma físico |
|---|---:|---|
| 0015 Pavimentação e recapeamento urbano | R$ 1,3 mi por ano, R$ 5,2 mi no total | 10.000 m² por ano |
| 0019 Construção de usina fotovoltaica | R$ 4,8 mi (1,2 mi em 2026 e 3,6 mi em 2027) | 25% em 2026, 75% em 2027 |
| 0004 Construção do Estádio Municipal no Pedro Barros | R$ 1,0 mi (2027 e 2028) | 50% + 50% |
| 0009 Casa do Cidadão no Bairro Barreiro | sem valor extraído | construção |
| 0010 Núcleo de Apoio do CRAS Parque São Roque | sem valor extraído | construção |
| 0018 Escadaria da Rua Mário Marcolino Neto | sem valor extraído | construção |
| 0031 Reforma/construção de prédios de ESF | sem valor extraído | unidades |
| 0032 Sede própria do CAPS | sem valor extraído | construção |
| 0033 Reforma/construção de escolas | sem valor extraído | unidades |
| Indicadores: criação do Fundo Municipal do Turismo; substituição de pontes rurais | | |

Fonte: [Lei 1.996/2025, Anexo III](https://www.taquarituba.sp.gov.br/legislacao/download-lei/13342/).

## 5. Operação de crédito FINISA (Lei 1.974/2025)

- Autoriza contratar com a Caixa, com garantia da União, até **R$ 25.000.000,00** no programa FINISA, para "obras de infraestrutura urbana, energia fotovoltaica, aquisição de máquinas, veículos e equipamentos". Sancionada em 12/03/2025. Fonte: [Lei 1.974/2025](https://www.taquarituba.sp.gov.br/legislacao/download-lei/12835/).
- Ingressaram R$ 18,00 mi em 2025 ([DCA 2025](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2025&no_anexo=DCA-Anexo%20I-C&id_ente=3553807)); a dívida contratual registra R$ 25 mi de empréstimos internos ([RGF 2025 Anexo 02](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rgf?an_exercicio=2025&in_periodicidade=Q&nr_periodo=3&co_tipo_demonstrativo=RGF&no_anexo=RGF-Anexo%2002&co_esfera=M&co_poder=E&id_ente=3553807)). A operação de 2025 equivaleu a 11,48% da RCL ajustada, perto do limite anual de 16% ([RGF Anexo 04](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rgf?an_exercicio=2025&in_periodicidade=Q&nr_periodo=3&co_tipo_demonstrativo=RGF&no_anexo=RGF-Anexo%2004&co_esfera=M&co_poder=E&id_ente=3553807)).
- A LOA 2026 prevê mais R$ 2.277.500,00 de operação de crédito ([Lei 1.998/2025](https://www.taquarituba.sp.gov.br/legislacao/download-lei/13497/)).
