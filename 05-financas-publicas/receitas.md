# Receitas (2013 a 2025)

CSV: [dados/receitas_2013_2025_siconfi_dca.csv](dados/receitas_2013_2025_siconfi_dca.csv).

Fonte de todos os valores da tabela: Tesouro Nacional, Siconfi, DCA Anexo I-C (receitas orçamentárias realizadas), consulta pela API `https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=<ANO>&no_anexo=DCA-Anexo%20I-C&id_ente=3553807` (em 2013 o anexo se chama `Anexo%20I-C`). Exemplo: [DCA 2025](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2025&no_anexo=DCA-Anexo%20I-C&id_ente=3553807), [DCA 2019](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2019&no_anexo=DCA-Anexo%20I-C&id_ente=3553807), [DCA 2013](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2013&no_anexo=Anexo%20I-C&id_ente=3553807).

Notas de método:
- O DCA é consolidado (Prefeitura, Câmara e Capstuba, o RPPS). As receitas intraorçamentárias são contribuições patronais e aportes da própria Prefeitura ao RPPS.
- "Receita total líquida" = receitas correntes + capital, menos a dedução para formação do FUNDEB (cálculo próprio).
- De 2013 a 2017 o plano de contas era outro: IPTU, ISS e ITBI aparecem sem dívida ativa e multas (que ficavam em "outras receitas"), então esses anos não são totalmente comparáveis com 2018 em diante.
- 2016: o DCA enviado ao Siconfi não trouxe ISS, ITBI nem taxas (por isso aparecem zerados). É falha da declaração, não queda real.
- Receitas de 2009 a 2012 (FINBRA) não foram baixadas.
- Percentuais e per capita: cálculo próprio. População é a usada pelo próprio Siconfi.

## Tabela por ano (R$ milhões correntes)

| Item (R$ mi) | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Receita total líquida (exceto intra) | 50,95 | 59,98 | 61,30 | 63,62 | 67,86 | 75,92 | 80,95 | 85,92 | 104,43 | 117,33 | 138,52 | 152,22 | 185,87 |
| Receitas correntes (bruta) | 54,77 | 59,93 | 62,81 | 65,34 | 74,16 | 80,25 | 88,06 | 92,70 | 113,85 | 127,79 | 151,43 | 168,52 | 184,62 |
| Tributos próprios (impostos, taxas, contrib. melhoria) | 7,05 | 7,11 | 6,44 | 3,64 | 7,89 | 10,97 | 11,55 | 12,16 | 13,07 | 16,04 | 19,46 | 20,61 | 23,02 |
| IPTU | 2,45 | 2,49 | 2,63 | 3,01 | 3,29 | 4,35 | 4,76 | 4,82 | 4,99 | 5,88 | 6,69 | 6,66 | 7,74 |
| ISS | 2,51 | 2,48 | 2,04 | 0,00 | 2,06 | 3,23 | 3,74 | 3,92 | 4,21 | 5,51 | 6,57 | 6,65 | 7,32 |
| ITBI | 0,85 | 0,72 | 0,62 | 0,00 | 0,86 | 1,20 | 0,85 | 1,20 | 1,77 | 1,93 | 2,31 | 2,42 | 2,24 |
| IRRF retido | 0,46 | 0,40 | 0,45 | 0,62 | 0,86 | 1,11 | 1,30 | 1,48 | 1,33 | 1,85 | 2,94 | 3,86 | 4,48 |
| Contrib. iluminação pública | 0,00 | 0,00 | 0,00 | 0,00 | 1,21 | 1,21 | 1,28 | 1,31 | 1,32 | 1,45 | 1,56 | 1,39 | 1,85 |
| Transferências correntes | 42,97 | 46,54 | 48,71 | 54,38 | 57,35 | 63,55 | 69,50 | 74,32 | 93,50 | 101,98 | 117,21 | 132,79 | 148,84 |
| FPM | 12,33 | 13,21 | 13,99 | 16,24 | 15,67 | 16,69 | 18,12 | 17,31 | 23,11 | 29,00 | 32,58 | 40,80 | 45,36 |
| Cota-parte ICMS | 11,96 | 12,28 | 13,23 | 14,10 | 16,21 | 17,95 | 20,04 | 19,70 | 25,08 | 29,48 | 31,45 | 36,43 | 40,25 |
| Cota-parte IPVA | 2,78 | 3,30 | 3,34 | 3,61 | 3,94 | 4,14 | 4,39 | 4,59 | 5,02 | 6,58 | 8,85 | 8,69 | 9,23 |
| FUNDEB recebido | 8,64 | 8,99 | 9,25 | 10,07 | 10,82 | 11,94 | 12,71 | 12,22 | 15,17 | 16,62 | 16,53 | 19,26 | 21,00 |
| (-) Dedução para o FUNDEB | 5,85 | 5,74 | 6,06 | 6,68 | 7,03 | 7,62 | 8,30 | 8,12 | 10,39 | 12,64 | 14,11 | 16,62 | 18,18 |
| SUS (União) | 2,80 | 3,92 | 3,87 | 4,40 | 4,45 | 4,95 | 5,47 | 9,90 | 15,80 | 8,34 | 9,40 | 9,66 | 10,46 |
| SUS (Estado) | 0,00 | 0,00 | 0,27 | 0,43 | 0,38 | 0,90 | 0,36 | 0,45 | 2,45 | 1,16 | 1,16 | 2,62 | 5,58 |
| Transferências de capital | 1,92 | 5,61 | 3,87 | 4,10 | 0,31 | 3,23 | 1,12 | 1,34 | 0,63 | 0,58 | 0,76 | 0,00 | 0,00 |
| Operações de crédito | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 18,00 |
| Receitas intraorçamentárias (RPPS) | 2,76 | 2,58 | 3,73 | 3,84 | 4,49 | 5,42 | 5,89 | 6,35 | 7,87 | 9,70 | 13,04 | 14,29 | 10,15 |
| % tributos próprios / rec. correntes | 12,9 | 11,9 | 10,3 | 5,6 | 10,6 | 13,7 | 13,1 | 13,1 | 11,5 | 12,5 | 12,8 | 12,2 | 12,5 |
| % transferências / rec. correntes | 78,5 | 77,7 | 77,6 | 83,2 | 77,3 | 79,2 | 78,9 | 80,2 | 82,1 | 79,8 | 77,4 | 78,8 | 80,6 |
| Receita líquida per capita (R$) | 2.207 | 2.594 | 2.651 | 2.746 | 2.925 | 3.272 | 3.492 | 3.701 | 4.491 | 5.038 | 5.947 | 6.247 | 7.628 |
| População usada pelo Siconfi | 23083 | 23123 | 23123 | 23163 | 23202 | 23202 | 23180 | 23218 | 23256 | 23292 | 23292 | 24366 | 24366 |

## Receita própria x transferências

- Em 2025 os tributos próprios somaram R$ 23,02 mi, só **12,5%** das receitas correntes (R$ 184,62 mi). Transferências correntes foram R$ 148,84 mi, **80,6%** (cálculo próprio sobre [DCA 2025](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2025&no_anexo=DCA-Anexo%20I-C&id_ente=3553807)).
- Esse grau de dependência fica entre 77% e 83% em toda a série 2013 a 2025, sem tendência de queda.
- As duas maiores fontes isoladas são FPM (R$ 45,36 mi em 2025) e cota-parte do ICMS (R$ 40,25 mi). Juntas são 46,4% das receitas correntes de 2025 (cálculo próprio).
- O FPM foi a receita que mais cresceu: de R$ 18,12 mi (2019) para R$ 45,36 mi (2025), 2,5 vezes em seis anos. Parte disso vem de cotas extras de 1% (R$ 3,82 mi em 2024, [DCA 2024](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2024&no_anexo=DCA-Anexo%20I-C&id_ente=3553807)) e da mudança de faixa populacional: o Siconfi passa a usar 24.366 habitantes em 2024 (Censo 2022), contra 23.292 antes.
- IPTU em 2025: R$ 7,74 mi, cerca de R$ 318 por habitante (cálculo próprio com população 24.366). ISS: R$ 7,32 mi.
- IRRF retido (imposto de renda dos servidores, que fica com o município) quase triplicou de 2021 (R$ 1,33 mi) a 2025 (R$ 4,48 mi), reflexo do aumento da folha.

## Composição das transferências em 2025 (R$ mi)

| Origem | Item | 2025 |
|---|---|---:|
| União | FPM | 45,36 |
| União | SUS fundo a fundo | 10,46 |
| União | FNDE (salário-educação, PNAE, PNATE etc.) | 2,54 |
| União | FNAS (assistência social) | 0,64 |
| União | Transferência especial (emendas Pix) | 1,81 |
| Estado | ICMS | 40,25 |
| Estado | IPVA | 9,23 |
| Estado | SUS estadual | 5,58 |
| Estado | Convênios (principalmente educação) | 8,53 |
| FUNDEB | Repasse do fundo | 21,00 |

Fonte: [DCA 2025](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2025&no_anexo=DCA-Anexo%20I-C&id_ente=3553807) (conta 1.7.1.9.57 Transferência Especial da União = R$ 1.807.410,00).

FUNDEB: o município entregou R$ 18,18 mi ao fundo e recebeu R$ 21,00 mi em 2025, saldo positivo de R$ 2,83 mi (cálculo próprio).

## Receitas de capital

- Transferências de capital caíram de R$ 5,61 mi (2014) para zero em 2024 e 2025 no DCA. Convênios e emendas passaram a entrar como transferências correntes ou especiais.
- 2025 teve a primeira operação de crédito relevante da série: **R$ 18,00 mi** (FINISA/Caixa, [Lei 1.974/2025](https://www.taquarituba.sp.gov.br/legislacao/download-lei/12835/)). Sem ela, a receita líquida de 2025 seria R$ 167,87 mi (cálculo próprio).
- Alienação de imóveis: R$ 1,43 mi em 2025.

## Execução parcial de 2026

Até agosto de 2026 a receita realizada (inclusive intra) foi R$ 133,20 mi, 69,2% da previsão anual de R$ 192,45 mi ([RREO 2026 4º bim](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?an_exercicio=2026&nr_periodo=4&co_tipo_demonstrativo=RREO&no_anexo=RREO-Anexo%2001&co_esfera=M&id_ente=3553807)). A RCL dos 12 meses até agosto/2026 foi R$ 169,03 mi ([RGF 2026 2º quad.](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rgf?an_exercicio=2026&in_periodicidade=Q&nr_periodo=2&co_tipo_demonstrativo=RGF&no_anexo=RGF-Anexo%2002&co_esfera=M&co_poder=E&id_ente=3553807)).

## Tendência (comentário)

- **Dado oficial:** a receita líquida passou de R$ 50,95 mi (2013) para R$ 185,87 mi (2025). Per capita, de R$ 2.207 para R$ 7.628 (com o empréstimo) ou cerca de R$ 6.889 sem ele (cálculo próprio).
- **Análise:** o crescimento é real e forte depois de 2021, mas quase todo vem de fora (FPM, ICMS, FUNDEB, SUS). A receita própria cresce no mesmo ritmo, não mais rápido, então a autonomia fiscal não melhorou. O TCE apontou em 2024 baixa eficiência na cobrança da dívida ativa, cancelamentos de 6,91% da dívida ativa e ausência de taxa de lixo ([parecer 2024](https://www.tce.sp.gov.br/jurisprudencia/exibir?proc=4288/989/24&offset=0)). Também fica como risco a reforma tributária: o ISS será substituído gradualmente pelo IBS a partir de 2029, e a cota do ICMS também migra para o IBS; para um município com base de serviços pequena o efeito líquido ainda é incerto.
