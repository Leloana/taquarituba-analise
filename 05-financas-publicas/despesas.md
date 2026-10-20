# Como o orçamento é gasto (2013 a 2025, com dados de 2026)

CSVs: [dados/despesas_funcao_2013_2025_siconfi_dca.csv](dados/despesas_funcao_2013_2025_siconfi_dca.csv), [dados/despesas_natureza_2013_2025_siconfi_dca.csv](dados/despesas_natureza_2013_2025_siconfi_dca.csv), [dados/pessoal_e_divida_rgf_2018_2026.csv](dados/pessoal_e_divida_rgf_2018_2026.csv), [dados/tce_pareceres_e_indices_2009_2024.csv](dados/tce_pareceres_e_indices_2009_2024.csv).

## 1. Despesa por função (despesa empenhada, R$ milhões)

Fonte: Siconfi DCA Anexo I-E, API `https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=<ANO>&no_anexo=DCA-Anexo%20I-E&id_ente=3553807`, por exemplo [2025](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2025&no_anexo=DCA-Anexo%20I-E&id_ente=3553807) e [2013](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2013&no_anexo=Anexo%20I-E&id_ente=3553807). De 2014 a 2017 o DCA não separa as intraorçamentárias (o total inclui intra).

| Função (R$ mi) | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 00 TOTAL exceto intra | 48,07 | 62,60 | 64,52 | 64,03 | 67,15 | 67,81 | 75,57 | 81,40 | 96,68 | 120,56 | 140,48 | 151,82 | 169,95 |
| 01 Legislativa | 1,42 | 1,64 | 1,50 | 1,69 | 1,72 | 1,68 | 1,56 | 1,66 | 1,72 | 1,66 | 1,94 | 1,71 | 2,63 |
| 02 Judiciária | 0,78 | 0,09 | 0,71 | 0,61 | 0,16 | 0,14 | 0,15 | 0,15 | 0,75 | 0,00 | 0,00 | 0,00 | 0,00 |
| 04 Administração | 8,70 | 12,66 | 10,03 | 10,94 | 10,81 | 8,86 | 10,11 | 10,72 | 10,79 | 8,36 | 9,51 | 15,60 | 17,62 |
| 06 Segurança Pública | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,39 | 0,61 | 2,07 | 2,63 |
| 08 Assistência Social | 3,26 | 3,55 | 3,98 | 3,76 | 3,97 | 4,01 | 5,05 | 5,92 | 6,21 | 7,23 | 9,19 | 8,98 | 10,34 |
| 09 Previdência Social | 3,28 | 3,81 | 4,46 | 5,28 | 5,99 | 6,65 | 7,47 | 7,71 | 8,37 | 10,67 | 12,73 | 14,33 | 16,08 |
| 10 Saúde | 11,14 | 14,35 | 14,51 | 16,04 | 17,61 | 18,83 | 19,30 | 24,54 | 32,55 | 31,97 | 35,21 | 40,73 | 44,30 |
| 12 Educação | 14,40 | 17,40 | 19,22 | 18,39 | 20,36 | 19,74 | 21,51 | 18,99 | 26,80 | 36,97 | 43,62 | 45,83 | 51,11 |
| 13 Cultura | 0,35 | 0,52 | 0,68 | 0,58 | 0,59 | 0,58 | 0,80 | 0,66 | 0,80 | 1,47 | 1,86 | 1,52 | 2,98 |
| 15 Urbanismo | 1,85 | 4,43 | 7,26 | 4,24 | 3,63 | 4,94 | 7,29 | 8,75 | 6,24 | 15,71 | 19,98 | 14,96 | 15,08 |
| 16 Habitação | 0,08 | 0,02 | 0,00 | 0,18 | 0,00 | 0,02 | 0,00 | 0,02 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| 18 Gestão Ambiental | 0,49 | 0,35 | 0,30 | 0,47 | 0,35 | 0,32 | 0,19 | 0,07 | 0,07 | 0,44 | 0,73 | 0,95 | 1,43 |
| 20 Agricultura | 0,77 | 1,09 | 0,48 | 0,50 | 0,52 | 0,50 | 0,53 | 0,59 | 0,68 | 1,33 | 0,83 | 0,72 | 0,73 |
| 26 Transporte | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 1,84 | 1,24 | 1,05 | 1,33 |
| 27 Desporto e Lazer | 0,66 | 0,67 | 0,58 | 0,69 | 0,85 | 0,84 | 0,78 | 0,59 | 0,57 | 1,02 | 1,29 | 1,53 | 1,66 |
| 28 Encargos Especiais | 0,88 | 2,02 | 0,82 | 0,66 | 0,59 | 0,71 | 0,82 | 1,03 | 1,13 | 1,50 | 1,75 | 1,84 | 2,00 |
| 99 Intraorcamentarias | 2,67 | 0,00 | 0,00 | 0,00 | 0,00 | 4,84 | 5,61 | 6,05 | 6,54 | 8,51 | 11,73 | 12,82 | 11,13 |

### Participação de cada função no total (exceto intra), % (cálculo próprio)

| Função (% do total exceto intra) | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 Saúde | 23,17 | 22,93 | 22,48 | 25,05 | 26,23 | 27,77 | 25,53 | 30,15 | 33,67 | 26,52 | 25,06 | 26,83 | 26,07 |
| 12 Educação | 29,96 | 27,79 | 29,79 | 28,73 | 30,32 | 29,1 | 28,46 | 23,33 | 27,72 | 30,67 | 31,05 | 30,19 | 30,08 |
| 04 Administração | 18,09 | 20,22 | 15,55 | 17,08 | 16,09 | 13,06 | 13,38 | 13,17 | 11,16 | 6,93 | 6,77 | 10,28 | 10,37 |
| 15 Urbanismo | 3,85 | 7,07 | 11,24 | 6,62 | 5,41 | 7,29 | 9,65 | 10,75 | 6,46 | 13,03 | 14,23 | 9,86 | 8,88 |
| 09 Previdência Social | 6,83 | 6,09 | 6,91 | 8,24 | 8,91 | 9,81 | 9,88 | 9,47 | 8,65 | 8,85 | 9,06 | 9,44 | 9,46 |
| 08 Assistência Social | 6,78 | 5,67 | 6,17 | 5,88 | 5,91 | 5,91 | 6,68 | 7,27 | 6,43 | 6,0 | 6,54 | 5,92 | 6,08 |
| 06 Segurança Pública | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,32 | 0,44 | 1,36 | 1,55 |
| 01 Legislativa | 2,96 | 2,62 | 2,33 | 2,64 | 2,56 | 2,48 | 2,07 | 2,04 | 1,78 | 1,38 | 1,38 | 1,13 | 1,55 |
| 13 Cultura | 0,74 | 0,83 | 1,05 | 0,91 | 0,88 | 0,86 | 1,06 | 0,81 | 0,83 | 1,22 | 1,32 | 1,0 | 1,75 |
| 27 Desporto e Lazer | 1,38 | 1,07 | 0,9 | 1,08 | 1,27 | 1,23 | 1,04 | 0,73 | 0,59 | 0,85 | 0,92 | 1,01 | 0,98 |
| 18 Gestão Ambiental | 1,02 | 0,56 | 0,46 | 0,73 | 0,52 | 0,47 | 0,26 | 0,08 | 0,07 | 0,37 | 0,52 | 0,62 | 0,84 |
| 20 Agricultura | 1,6 | 1,74 | 0,74 | 0,78 | 0,78 | 0,74 | 0,7 | 0,72 | 0,71 | 1,1 | 0,59 | 0,47 | 0,43 |
| 26 Transporte | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 1,53 | 0,89 | 0,69 | 0,78 |

**Tendência:**
- Educação e saúde somam cerca de 56% da despesa em 2025 (30,1% e 26,1%). A saúde teve pico de 33,7% em 2021 (pandemia) e voltou ao patamar de 26%.
- Urbanismo dobrou de peso entre 2021 (6,5%) e 2023 (14,2%), ano pré-eleitoral, e caiu para 8,9% em 2025.
- Administração caiu de 18% (2013) para 6,8% (2023) e voltou a 10,4% (2025).
- Segurança pública surge em 2022 (criação da Guarda Civil Municipal) e chega a R$ 2,63 mi em 2025.
- Previdência (RPPS) cresce sem parar: de R$ 3,28 mi (2013) para R$ 16,08 mi (2025), 9,5% do gasto.
- Gestão ambiental, agricultura, cultura e esporte ficam abaixo de 2% cada.

## 2. Despesa por natureza (R$ milhões)

Fonte: Siconfi DCA Anexo I-D, por exemplo [2025](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2025&no_anexo=DCA-Anexo%20I-D&id_ente=3553807). Inclui intraorçamentárias. Percentuais: cálculo próprio.

| Natureza (R$ mi) | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Despesa empenhada total (incl. intra) | 50,74 | 62,60 | 64,52 | 64,03 | 67,15 | 72,65 | 81,18 | 87,45 | 103,22 | 129,08 | 152,22 | 164,64 | 181,08 |
| Despesas correntes | 46,01 | 51,69 | 54,41 | 60,20 | 65,48 | 67,41 | 74,86 | 77,61 | 96,75 | 115,30 | 139,15 | 159,39 | 172,63 |
| Pessoal e encargos | 23,42 | 26,02 | 28,42 | 31,61 | 35,49 | 38,89 | 41,51 | 43,03 | 44,97 | 51,96 | 63,50 | 69,69 | 77,63 |
| Outras despesas correntes | 22,59 | 25,67 | 25,99 | 28,59 | 29,99 | 28,52 | 33,35 | 34,58 | 51,78 | 63,35 | 75,65 | 89,70 | 95,00 |
| Transferências a entidades sem fins lucrativos (Santa Casa, APAE etc.) | 7,79 | 9,17 | 7,51 | 7,51 | 9,40 | 8,74 | 9,85 | 14,40 | 22,77 | 19,11 | 21,50 | 24,04 | 24,58 |
| Despesas de capital | 4,73 | 10,91 | 10,12 | 3,83 | 1,66 | 5,24 | 6,32 | 9,84 | 6,47 | 13,77 | 13,07 | 5,25 | 8,44 |
| Investimentos | 3,49 | 9,28 | 8,99 | 3,11 | 1,42 | 4,98 | 6,03 | 9,54 | 6,17 | 13,36 | 12,65 | 4,80 | 7,96 |
| Amortização da dívida | 0,56 | 0,63 | 0,53 | 0,22 | 0,24 | 0,26 | 0,29 | 0,30 | 0,30 | 0,41 | 0,41 | 0,45 | 0,49 |
| Juros da dívida | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| % pessoal / total | 46,2 | 41,6 | 44,0 | 49,4 | 52,9 | 53,5 | 51,1 | 49,2 | 43,6 | 40,3 | 41,7 | 42,3 | 42,9 |
| % investimentos / total | 6,9 | 14,8 | 13,9 | 4,9 | 2,1 | 6,9 | 7,4 | 10,9 | 6,0 | 10,4 | 8,3 | 2,9 | 4,4 |
| % terceiro setor / total | 15,4 | 14,6 | 11,6 | 11,7 | 14,0 | 12,0 | 12,1 | 16,5 | 22,1 | 14,8 | 14,1 | 14,6 | 13,6 |

**Tendência e leitura:**
- **Investimento é baixo e oscilante.** Picos em 2014 e 2015 (cerca de 14%) e em 2020 e 2022 (cerca de 10% a 11%), anos de fim de mandato ou pré-eleitorais; vales em 2017 (2,1%) e 2024 (2,9%). Em 2025, mesmo com R$ 18 mi do empréstimo FINISA, o investimento empenhado foi só R$ 7,96 mi (4,4%). Ou seja, boa parte do empréstimo ficou em caixa para 2026 (o superávit financeiro usado em 2026 foi R$ 19,40 mi, [RREO 2026](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?an_exercicio=2026&nr_periodo=4&co_tipo_demonstrativo=RREO&no_anexo=RREO-Anexo%2001&co_esfera=M&id_ente=3553807)). A LOA 2026 prevê R$ 9,12 mi de investimentos na administração direta ([Lei 1.998/2025](https://www.taquarituba.sp.gov.br/legislacao/download-lei/13497/)).
- **Terceiro setor pesa muito.** Transferências a entidades sem fins lucrativos somaram R$ 24,58 mi em 2025 (13,6% do gasto). O TCE registrou que a Santa Casa recebeu o equivalente a 43,75% do empenhado em saúde em 2021 ([parecer 2021](https://www.tce.sp.gov.br/jurisprudencia/exibir?proc=7015/989/20&offset=0)).
- **Pessoal**: de R$ 23,42 mi (2013) para R$ 77,63 mi (2025), 3,3 vezes. A participação caiu de 53,5% (2018) para cerca de 42% (2022 a 2025) porque a receita cresceu ainda mais rápido.

## 3. Saúde e educação x mínimos constitucionais (apuração do TCE-SP)

Mínimos: 25% da receita de impostos e transferências em ensino (CF art. 212) e 15% em saúde (ADCT art. 77 / LC 141). Fonte de cada linha: parecer do TCE-SP do exercício (links em [contas-e-tce.md](contas-e-tce.md)).

| Exercício | Ensino (mín. 25%) | FUNDEB magistério/profissionais | Saúde (mín. 15%) |
|---|---:|---:|---:|
| 2009 | 28,52% | 61,53% | 21,18% |
| 2010 | 26,99% | 60,46% | 24,99% |
| 2011 | 26,73% | 60,85% | 24,09% |
| 2012 | 25,10% | 64,06% | 26,04% |
| 2013 | 25,33% | 63,48% | 26,03% |
| 2014 | 25,91% | 62,45% | 28,85% |
| 2015 | 28,02% | 62,72% | 30,73% |
| 2016 | 25,70% | 66,26% | 30,25% |
| 2017 | 26,21% | 64,36% | 32,56% |
| 2018 | 25,70% | 66,46% | 32,74% |
| **2019** | **24,76% (abaixo do mínimo)** | 62,09% | 32,25% |
| 2020 | 28,74% | 69,19% | 30,30% |
| 2021 | 27,65% | 70,50% | 28,19% |
| 2022 | 28,44% | 70,34% | 32,58% |
| 2023 | 31,52% | 80,32% | 29,13% |
| 2024 | 28,74% | 83,75% | 23,76% |
| 2025 | não apurado pelo TCE até 20/10/2026 | | |

**Tendência:**
- Educação: até 2019 o município ficou colado no piso de 25% (entre 25,1% e 25,9% em cinco dos onze anos de 2009 a 2019), e em 2019 ficou abaixo (24,76%), o que gerou parecer desfavorável. Depois de 2020 a aplicação ficou com folga (27,65% a 31,52%).
- Saúde: sempre acima do mínimo, com média perto de 31% entre 2014 e 2023 (cálculo próprio). Em 2024 caiu para 23,76%, menor valor desde 2011. Ainda assim o gasto em saúde em reais subiu (R$ 40,73 mi em 2024 contra R$ 35,21 mi em 2023, [DCA](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2024&no_anexo=DCA-Anexo%20I-E&id_ente=3553807)), porque a base de impostos cresceu e mais recurso federal e estadual entrou na saúde.
- Gasto por aluno e por habitante (TCE, dado de 2021): R$ 12.800,53 por aluno (média dos 644 municípios: R$ 12.281,72) e R$ 1.444,65 por habitante em saúde (média: R$ 1.153,24). Fonte: [RDM TCE-SP](https://www.tce.sp.gov.br/sites/default/files/rdm/taquarituba.pdf).

## 4. Despesa com pessoal x limite da LRF

### Apuração do TCE (pessoal / RCL, limite 54%)

| 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 37,29% | 38,13% | 38,65% | 40,80% | 41,78% | 42,07% | 42,76% | 41,97% | 45,51% | 44,95% | 43,72% | 42,55% | 36,70% | 35,87% | 38,89% | 39,13% |

Fonte: pareceres do TCE-SP por exercício (ver [contas-e-tce.md](contas-e-tce.md)).

### RGF declarado ao Tesouro (Poder Executivo)

| Ano | Período | RCL ajustada | Despesa total com pessoal | % RCL |
|---|---|---:|---:|---:|
| 2018 | 3º quadrimestre | 69,01 mi | 30,87 mi | 44,73% |
| 2019 | 2º semestre (simplificado) | 74,17 mi | 39,24 mi | 52,91% |
| 2020 | 3º quad. | 80,68 mi | 34,23 mi | 42,42% |
| 2021 | 3º quad. | 95,41 mi | 35,02 mi | 36,70% |
| 2022 | 3º quad. | 109,88 mi | 39,41 mi | 35,87% |
| 2023 | 3º quad. | 128,76 mi | 50,07 mi | 38,89% |
| 2024 | 3º quad. | 140,33 mi | 53,20 mi | 37,91% |
| 2025 | 3º quad. | 156,55 mi | 58,83 mi | 37,58% |
| 2026 | 2º quad. (12 meses até ago) | 166,41 mi | 64,86 mi | 38,98% |

Fonte: Siconfi RGF Anexo 01, por exemplo [2025](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rgf?an_exercicio=2025&in_periodicidade=Q&nr_periodo=3&co_tipo_demonstrativo=RGF&no_anexo=RGF-Anexo%2001&co_esfera=M&co_poder=E&id_ente=3553807), [2026](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rgf?an_exercicio=2026&in_periodicidade=Q&nr_periodo=2&co_tipo_demonstrativo=RGF&no_anexo=RGF-Anexo%2001&co_esfera=M&co_poder=E&id_ente=3553807) e [2019 simplificado](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rgf?an_exercicio=2019&in_periodicidade=S&nr_periodo=2&co_tipo_demonstrativo=RGF%20Simplificado&co_esfera=M&co_poder=E&id_ente=3553807). Limites: alerta 48,6%, prudencial 51,3%, máximo 54%.

**Leitura:** o RGF de 2019 declarou 52,91%, acima do limite prudencial, mas o TCE recalculou 43,72% para o mesmo ano; a diferença deve vir do tratamento de inativos com recursos vinculados. Depois de 2021 o índice ficou estável perto de 37% a 39%, com folga de cerca de R$ 25 mi até o limite máximo em 2026 (cálculo próprio: 54% de R$ 166,41 mi menos R$ 64,86 mi). Em valores, porém, a despesa com pessoal subiu de R$ 35,02 mi (2021) para R$ 64,86 mi (12 meses até ago/2026), alta de 85%.

## 5. Dívida, empréstimo e previdência

| Data | Dívida consolidada | Dívida consolidada líquida | % DCL / RCL | Passivo atuarial RPPS |
|---|---:|---:|---:|---:|
| dez/2019 | 4,19 mi | 4,12 mi | n/d | n/d |
| dez/2020 | 4,30 mi | 4,30 mi | n/d | n/d |
| dez/2022 | 4,72 mi | -22,89 mi (caixa maior que a dívida) | negativa | n/d |
| dez/2024 | 4,79 mi | -1,08 mi | negativa | n/d |
| dez/2025 | 29,52 mi | 8,07 mi | 5,15% | 152,67 mi |
| ago/2026 | 24,68 mi | 5,53 mi | 3,32% | 151,39 mi |

Fonte: Siconfi RGF Anexo 02, por exemplo [2025](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rgf?an_exercicio=2025&in_periodicidade=Q&nr_periodo=3&co_tipo_demonstrativo=RGF&no_anexo=RGF-Anexo%2002&co_esfera=M&co_poder=E&id_ente=3553807) e [2026](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rgf?an_exercicio=2026&in_periodicidade=Q&nr_periodo=2&co_tipo_demonstrativo=RGF&no_anexo=RGF-Anexo%2002&co_esfera=M&co_poder=E&id_ente=3553807).

- Até 2024 a dívida era só parcelamento previdenciário com o RPPS (cerca de R$ 4,5 mi) e a Prefeitura tinha caixa líquido.
- Em 2025 entraram R$ 25 mi de empréstimos internos (FINISA/Caixa, [Lei 1.974/2025](https://www.taquarituba.sp.gov.br/legislacao/download-lei/12835/)). O limite do Senado para DCL é 120% da RCL; a dívida está muito longe disso.
- O ponto sensível é o **RPPS**: passivo atuarial de R$ 152,67 mi em dez/2025, quase uma RCL inteira. O TCE registrou em 2023 que o déficit atuarial equivalia a 79,51% da RCL e que o índice de cobertura era 39,42%, "denotando possível comprometimento de sua viabilidade financeira" ([parecer 2023](https://www.tce.sp.gov.br/jurisprudencia/exibir?proc=4281/989/23&offset=0)). A Prefeitura já paga aportes para amortizar o déficit (R$ 6,46 mi em 2024, conta 7.9.9.9.01 do [DCA 2024](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2024&no_anexo=DCA-Anexo%20I-C&id_ente=3553807)).
- Juros: praticamente zero até 2025; com o FINISA passam a pesar a partir de 2026 (LOA 2026 prevê R$ 1,48 mi de amortização).

## 6. Resultado orçamentário e primário

| Ano | Resultado da execução orçamentária (TCE) | Resultado primário acima da linha (RREO) |
|---|---|---|
| 2013 | déficit 2,00% | n/d |
| 2014 | déficit 3,40% | n/d |
| 2015 | déficit 6,06% | n/d |
| 2016 | superávit 7,82% | n/d |
| 2017 | superávit 2,21% | n/d |
| 2018 | superávit 4,32% | n/d |
| 2019 | superávit 2,75% | n/d |
| 2020 | superávit 2,50% | +13,26 mi |
| 2021 | superávit 5,39% | +10,73 mi |
| 2022 | déficit 5,10% | +2,30 mi |
| 2023 | déficit 5,66% | -10,93 mi (com RPPS) |
| 2024 | déficit 5,36% (coberto por superávit financeiro) | -3,15 mi (com RPPS) |
| 2025 | n/d (TCE) | +3,21 mi (com RPPS) |

Fontes: pareceres do TCE (ver [contas-e-tce.md](contas-e-tce.md)) e Siconfi RREO Anexo 06, por exemplo [2025](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?an_exercicio=2025&nr_periodo=6&co_tipo_demonstrativo=RREO&no_anexo=RREO-Anexo%2006&co_esfera=M&id_ente=3553807) e [2023](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?an_exercicio=2023&nr_periodo=6&co_tipo_demonstrativo=RREO&no_anexo=RREO-Anexo%2006&co_esfera=M&id_ente=3553807).

**Análise:** o padrão do mandato 2021-2024 foi acumular caixa em 2021 e gastar esse caixa em 2022 a 2024 (três déficits seguidos, todos cobertos por superávit financeiro). Em 2025 o resultado volta a positivo, mas inflado pelo empréstimo de R$ 18 mi. O caixa bruto caiu de R$ 28,02 mi (dez/2025) para R$ 20,47 mi (ago/2026) ([RGF Anexo 02](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rgf?an_exercicio=2026&in_periodicidade=Q&nr_periodo=2&co_tipo_demonstrativo=RGF&no_anexo=RGF-Anexo%2002&co_esfera=M&co_poder=E&id_ente=3553807)), coerente com a execução das obras financiadas.
