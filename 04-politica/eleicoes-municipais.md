# Taquarituba (SP): eleições municipais 1996 a 2024

Data de referência: 20/10/2026. Município TSE nº 71773, IBGE 3553807, 236ª Zona Eleitoral.

Convenções deste arquivo:
- **Fato**: número ou informação tirada direto da fonte citada.
- **Inferência**: leitura minha a partir dos fatos, marcada como tal.
- Percentuais de 1996 a 2020 calculados sobre os votos nominais válidos do cargo, a partir dos microdados do TSE. Em 2024, percentual oficial do TSE.

Fontes principais:
- Microdados TSE, votação por candidato, município e zona: `https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_candidato_munzona/votacao_candidato_munzona_{ANO}.zip` (portal: https://dadosabertos.tse.jus.br/dataset/)
- Microdados TSE, detalhe de comparecimento: `https://cdn.tse.jus.br/estatistica/sead/odsele/detalhe_votacao_munzona/detalhe_votacao_munzona_{ANO}.zip`
- Resultado oficial 2024, prefeito: https://resultados.tse.jus.br/oficial/ele2024/619/dados/sp/sp71773-c0011-e000619-u.json
- Resultado oficial 2024, vereador: https://resultados.tse.jus.br/oficial/ele2024/619/dados/sp/sp71773-c0013-e000619-u.json
- CSVs gerados: `dados/prefeito_1996_2024.csv`, `dados/vereadores_eleitos_1996_2024.csv`, `dados/vereadores_candidatos_1996_2024.csv`, `dados/bancada_por_partido_1996_2024.csv`, `dados/comparecimento_1996_2026.csv`

---

## 1. Prefeitos eleitos desde 1996

Os dados abertos do TSE por município começam em 1996. A história do município (instalado em 14/03/1926, como Taquary; nome Taquarituba desde 30/11/1944) está em https://www.taquarituba.sp.gov.br/cidade. Não localizei lista oficial de prefeitos anteriores a 1997: a "Galeria dos Presidentes" da Câmara retornou vazia em 20/10/2026 (https://camarataquarituba.sp.gov.br/index1.php?pag=T1RjPU9EZz1PVFU9T0dVPU9HST1PVEE9T0dFPU9HRT0=&idmenu=8).

| Mandato | Prefeito eleito (nome de urna) | Partido | Votos | % válidos | Principal adversário | Fonte |
|---|---|---|---|---|---|---|
| 1997 a 2000 | Miderson Zanello Milleo | PMDB | 6.850 | 56,53% | Lourenço Custódio (PPB), 5.268 (43,47%) | TSE munzona 1996 |
| 2001 a 2004 | Dr. Miderson | PSDB | 8.112 | 64,27% | Dr. Arnon (PMDB), 4.510 (35,73%) | TSE munzona 2000 |
| 2005 a 2008 | Itavico Dognani | PSDB | 6.859 | 50,86% | Dr. Arnon (PMDB) 4.114 (30,51%); Rogério Pereira (PT) 2.513 (18,63%) | TSE munzona 2004 |
| 2009 a 2012 | Dr. Miderson | PSDB | 7.560 | 53,62% | Anísio Gobbo (PPS), 6.538 (46,38%) | TSE munzona 2008 |
| 2013 a 2016 | Dr. Miderson | PSDB | 7.566 | 93,99% (ver nota 2012) | Dr. Arnon (PCdoB), 484 | TSE munzona 2012 |
| 2017 a 2020 | Bola (José Clóvis de Almeida) | PSDB | 7.434 | 52,21% | Vardinho Soldera (PMDB), 6.806 (47,79%) | TSE munzona 2016 |
| 2021 a 2024 | Éder Miano (Éder Miano Pereira) | PP | 6.602 | 52,35% | Bola (PSDB) 5.657 (44,86%); Pedro da Força (PT) 352 (2,79%) | TSE munzona 2020 |
| 2025 a 2028 | Éder Miano | PP | 8.224 | 58,02% | Dr. Marcelo Milla (PSD), 5.951 (41,98%) | resultados.tse.jus.br 2024 |

Coligações dos eleitos (fato, TSE):
- 2000: PSDB / PV / PSB / PPS / PDT / PL. Adversário: PMDB / PTB.
- 2004: PP / PDT / PTB / PL / PFL / PSB / PV / PSDB ("Seguindo em Frente").
- 2008: PDT / PTB / PMDB / PRP / DEM / PSB / PSDB / PP / PV ("Taquarituba no Caminho Certo"). Adversário: PR / PSC / PPS / PT ("Mudança Já!").
- 2012: PDT / PTB / DEM / PV / PSDB ("O Presente Garantindo o Futuro").
- 2016: PPS / DEM / PSB / PV / PSDB / SD / PTB ("Pra Frente com Todos"). Adversário: PMDB / PSD / PRB / PP / PDT / PT / PR ("Rumo Novo, Agora é a Vez do Povo").
- 2020: REPUBLICANOS / PP / PSL / PODE / MDB ("Nova Semente"). Adversário: PTB / PV / PSDB / DEM ("Juntos no Caminho Certo").
- 2024: PP / MDB / PL / REPUBLICANOS / AVANTE ("Gerando Frutos"), vice Waldemar Soldera, "Vardinho" (MDB). Adversário: PODE / UNIÃO / PSB / PSD / CIDADANIA / PSDB ("Liberdade e Transparência para Todos"), vice Marli Antonia da Silva, "Dra Marli" (PSB).

**Nota sobre 2012 (fato)**: o candidato Vardinho Soldera (PMDB, coligação PT / PMDB / PSC / PR / PPS / PSB / PSD) consta no TSE como "INAPTO / INDEFERIDO", com 0 voto válido. No detalhe de votação de 2012, o cargo de prefeito teve 6.778 votos nulos sobre 15.243 comparecimentos, contra 222 nulos para vereador na mesma eleição (TSE detalhe_votacao_munzona_2012). **Inferência**: a maior parte desses nulos corresponde a votos dados a Vardinho e anulados pelo indeferimento; por isso o percentual de 93,99% de Miderson é sobre válidos e não reflete a disputa real. Não localizei a decisão judicial do indeferimento.

Fonte do 2º mandato de Éder e da autodescrição ("vereador de 2017 a 2020", "reeleito em 2024"): https://edermiano.com.br/ (site do próprio prefeito). Pelo TSE 2016, Éder foi eleito vereador pelo **PT** ("Eder Miano da Farmácia", 712 votos, 3º mais votado).

### Comparecimento nas eleições municipais (1º turno, prefeito)

| Ano | Aptos | Comparecimento | Abstenção | Brancos | Nulos |
|---|---|---|---|---|---|
| 1996 | 14.399 | 12.572 | 1.827 | 168 | 0 (campo zerado no arquivo do TSE) |
| 2000 | 15.747 | 13.698 | 2.049 | 265 | 808 |
| 2004 | 16.951 | 14.381 | 2.570 | 262 | 630 |
| 2008 | 17.674 | 14.957 | 2.717 | 276 | 580 |
| 2012 | 18.440 | 15.243 | 3.197 | 415 | 6.778 |
| 2016 | 18.808 | 15.310 | 3.498 | 456 | 614 |
| 2020 | 16.998 | 13.556 | 3.442 | 464 | 481 |
| 2024 | 18.044 | 14.761 (81,81%) | 3.283 (18,19%) | 280 | 306 |

Fonte: TSE detalhe_votacao_munzona (1996 a 2020) e resultados.tse.jus.br (2024).

---

## 2. Câmara Municipal: composição eleita

A Câmara teve 15 cadeiras em 1996 e 2000, 9 em 2004 e 2008, e 11 de 2012 em diante (contagem de eleitos nos microdados do TSE).

### 2.1 Bancadas por partido (cadeiras)

| Partido | 1996 | 2000 | 2004 | 2008 | 2012 | 2016 | 2020 | 2024 |
|---|---|---|---|---|---|---|---|---|
| PPB/PP | 6 | 1 | 0 | 1 | 1 | 1 | 3 | 3 |
| PMDB/MDB | 4 | 2 | 1 | 0 | 0 | 0 | 0 | 0 |
| PSDB | 2 | 2 | 2 | 1 | 3 | 1 | 3 | 1 |
| PV | 2 | 3 | 0 | 0 | 1 | 2 | 3 | 0 |
| PDT | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| PFL/DEM | 0 | 2 | 1 | 1 | 2 | 2 | 0 | 0 |
| PPS | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 |
| PSB | 0 | 2 | 1 | 1 | 0 | 0 | 0 | 0 |
| PTB | 0 | 0 | 1 | 2 | 1 | 1 | 0 | 0 |
| PT | 0 | 0 | 1 | 1 | 1 | 2 | 0 | 0 |
| PL/PR | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 3 (PL) |
| PSD | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 3 |
| PODE | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| UNIÃO | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| **Total** | 15 | 15 | 9 | 9 | 11 | 11 | 11 | 11 |

Fonte: `dados/bancada_por_partido_1996_2024.csv` (TSE). Atenção: PL de 2004 e PR de 2008 a 2016 são a mesma sigla em fases distintas (PL virou PR em 2006 e voltou a PL em 2019); PFL virou DEM em 2007 e se fundiu ao PSL formando o UNIÃO em 2022. Essas trajetórias de sigla são conhecimento público geral, não tiradas do TSE municipal.

**Comentário de tendência (inferência)**:
- 1996 a 2008: Câmara fragmentada, com PPB e PMDB fortes em 1996 e pulverização depois.
- 2012 a 2020: PSDB, PV e DEM formam o núcleo do grupo dos prefeitos Miderson e Bola; PT chega a 2 cadeiras em 2016.
- 2020: fim das coligações proporcionais concentra as cadeiras em 4 partidos (PSDB, PV, PP, PODE).
- 2024: PSDB e PV praticamente somem; PL (3) e PSD (3) aparecem com força ao lado do PP (3). PT, MDB e Republicanos não elegem ninguém. A Câmara passa a ser dominada por partidos de centro-direita e direita.

### 2.2 Vereadores eleitos em 2024 (legislatura 2025 a 2028)

| Vereador (urna) | Nome | Partido | Votos | % | Situação |
|---|---|---|---|---|---|
| Rodrigo Politori | Michael Rodrigo Politori | PSD | 645 | 4,60 | Eleito por QP |
| Sérgio Piranha | Sergio Gleison de Sá | PP | 614 | 4,38 | Eleito por QP |
| Gabriel Rodrigues | Gabriel Aparecido Almeida Rodrigues | PL | 550 | 3,92 | Eleito por QP |
| Rolandro Benini | Rolandro Augusto Benini | PL | 547 | 3,90 | Eleito por média |
| Dr Ricardo Almeida | Ricardo Alexandre Rodrigues de Almeida | PSD | 481 | 3,43 | Eleito por média |
| Dr Cleber Machado | Cleber Antonio Machado | UNIÃO | 480 | 3,42 | Eleito por QP |
| Mauricio Pascucci | Mauricio Reginaldo Pascucci | PSD | 417 | 2,97 | Eleito por média |
| Virgilio Leiloeiro | Virgilio Eugenio de Almeida | PSDB | 360 | 2,57 | Eleito por média |
| Bruno BBC | Bruno Vieira de Oliveira | PP | 360 | 2,57 | Eleito por média |
| Bruno Costa | Bruno Giovane da Costa | PP | 324 | 2,31 | Eleito por média |
| Oreia Barbeiro | Carlos Toniel Loureiro | PL | 307 | 2,19 | Eleito por média |

Mais votado não eleito: Tio da Vila (Claudio Vaz Pedroso, PT), 407 votos, porque a federação PT/PCdoB/PV não atingiu o quociente. Fonte: https://resultados.tse.jus.br/oficial/ele2024/619/dados/sp/sp71773-c0013-e000619-u.json

Votos nominais por partido para vereador em 2024 (fato, TSE): PSD 2.423; PL 2.420; PP 2.016; UNIÃO 1.284; PSDB 1.200; REPUBLICANOS 1.006; AVANTE 862; MDB 856; PSB 535; PT 533; PODE 524. Total de válidos para vereador: 14.030.

Mudanças na composição depois da posse (fato, site da Câmara, https://camarataquarituba.sp.gov.br/index1.php?pag=T0dRPU9EZz1PR0U9T0dVPU9UZz1PVE09T0RnPU9XUT1PV1U9T1dRPU9HTT1ZVEE9&view=DET-LEG&idleg=22):
- Ednalva Pereira de Jesus, "Nalva do Posto" (PP, suplente) substituiu Bruno Costa de 09/01/2025 a 26/04/2026, por "licença para investidura no cargo de Coordenador Municipal da Cultura".
- Em 20/10/2026 a lista de vereadores do site mostra **Glauber Gilio (PSD, 244 votos)**, suplente, no lugar de Rodrigo Politori. O site não traz o motivo; não localizei fonte que explique a troca.
- Ricardo Almeida aparece hoje como PSD; foi eleito em 2016 e 2020 pelo PV.

### 2.3 Vereadores eleitos em 2020 (legislatura 2021 a 2024)

| Vereador | Partido | Votos |
|---|---|---|
| Dr Ricardo Almeida | PV | 851 |
| Bruno BBC | PODE | 679 |
| Sergio Piranha | PP | 674 |
| Mauricio Pascucci | PP | 608 |
| Professora Flor (Florenice Brais) | PV | 529 |
| Thiago do Zote | PV | 517 |
| Rodrigo Politori | PODE | 448 |
| Virgilio Leiloeiro | PSDB | 410 |
| Toninho do Ônibus | PSDB | 397 |
| Dona Lena (Leni Terezinha de Godoi) | PSDB | 372 |
| Zé Botina | PP | 370 |

Fonte: TSE munzona 2020. Votos de partido para vereador em 2020 (nominais + legenda): PSDB 3.512 (28,5%), PV 3.319 (26,9%), PP 2.925 (23,7%), PODE 1.902 (15,4%), PT 573 (4,6%), REPUBLICANOS 101 (TSE votacao_partido_munzona_2020).

### 2.4 Vereadores eleitos em 2016 e 2012

2016 (TSE munzona 2016): Thiago do Zote (PV) 797; Dona Lena (PSDB) 728; Éder Miano da Farmácia (PT) 712; Helinho da Onória (DEM) 678; Dr. Ricardo Almeida (PV) 570; Pedro Rodrigues (PT) 543; Sérgio Piranha (PSD) 510; Carlinhos da Ambulância (PTB) 509; Paulo Turmeiro (PR) 480; Maurício Pascucci (PP) 400; Rederson (DEM) 381.

2012 (TSE munzona 2012): Dona Lena (PSDB) 1.388; Pedro da Delegacia (PT) 629; Dra Marli (PSDB) 605; Ximbica (PSDB) 580; Valdir Rodrigues (DEM) 527; Carlinhos da Ambulância (PTB) 488; Michelin Belé Belé (PP) 484; Professor Odair (PV) 460; Piranha (PSD) 427; Pedro Prestes (DEM) 384; Paulo Turmeiro (PR) 341.

Listas completas de 1996 a 2008 em `dados/vereadores_eleitos_1996_2024.csv`.

---

## 3. Leitura histórica (inferência, com base nos fatos acima)

1. **Hegemonia do grupo PSDB de 2000 a 2016**: o PSDB venceu cinco eleições seguidas (2000, 2004, 2008, 2012, 2016), com Miderson Zanello Milleo como figura central (eleito em 1996 pelo PMDB e depois três vezes pelo PSDB) e com Itavico Dognani e Bola (José Clóvis de Almeida) como sucessores dentro do mesmo arco de alianças. Em dezembro de 2021 a Câmara aprovou, por iniciativa dos 11 vereadores, a Lei 1.860 que denomina a sede da Prefeitura "Paço Municipal Doutor Miderson Zanello Milléo" (lista de leis da Câmara, ano 2021: https://camarataquarituba.sp.gov.br/index1.php?pag=T0dRPU9EZz1PR009T1RnPQ==&idtipolei=1&ano=2021).
2. **Oposição histórica ligada ao PMDB**: Dr. Arnon (PMDB em 2000 e 2004, PCdoB em 2012) e Vardinho Soldera (PMDB, barrado em 2012 e derrotado por 628 votos em 2016) lideraram a oposição. Em 2024 Vardinho passa a ser vice de Éder Miano, o que indica fusão da antiga oposição peemedebista com o grupo do PP.
3. **Virada de 2020**: Éder Miano, ex-vereador do PT (2016), vence pelo PP com coligação de centro-direita e encerra 16 anos de PSDB. Em 2024 amplia a votação (de 52,35% para 58,02%).
4. **Rearranjo de 2024**: a oposição a Éder migra para PSD, UNIÃO e PSB, com o PSDB como sócio menor. O PL, ausente da Câmara antes, elege 3 vereadores dentro da coligação do prefeito.
5. A política local é personalista (apelidos, profissões e bairros na urna; mesmos nomes reaparecem por décadas, como Paulo Turmeiro, Carlinhos da Ambulância, Dona Lena, Piranha, Zé Botina, Ronaldo Benini). Os partidos funcionam mais como veículos de grupos locais do que como marcas ideológicas.
