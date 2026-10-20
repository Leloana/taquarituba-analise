# Taquarituba (SP): eleições gerais 1998 a 2026 e perfil ideológico

Data de referência: 20/10/2026. A eleição geral de 2026 teve 1º turno em 04/10/2026; o 2º turno presidencial (Flávio Bolsonaro x Lula) ainda não ocorreu nesta data.

Fontes:
- 1998 a 2022: microdados TSE `votacao_candidato_munzona_{ANO}.zip` (https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_candidato_munzona/), recortados para o município 71773. Percentuais calculados sobre votos nominais válidos.
- Votos por partido (nominal + legenda): `votacao_partido_munzona_{ANO}.zip` (https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_partido_munzona/).
- 2026, resultados oficiais por município (percentual do TSE):
  - Presidente: https://resultados.tse.jus.br/oficial/ele2026/6257/dados/sp/sp71773-c0001-e006257-u.json
  - Governador: https://resultados.tse.jus.br/oficial/ele2026/6259/dados/sp/sp71773-c0003-e006259-u.json
  - Senador: https://resultados.tse.jus.br/oficial/ele2026/6259/dados/sp/sp71773-c0005-e006259-u.json
  - Deputado federal: https://resultados.tse.jus.br/oficial/ele2026/6259/dados/sp/sp71773-c0006-e006259-u.json
  - Deputado estadual: https://resultados.tse.jus.br/oficial/ele2026/6259/dados/sp/sp71773-c0007-e006259-u.json
  - Presidente, total Brasil: https://resultados.tse.jus.br/oficial/ele2026/6257/dados/br/br-c0001-e006257-u.json
- CSVs: `dados/eleicoes_gerais_1998_2026.csv` (todos os candidatos majoritários e os 15 mais votados para deputado em cada ano) e `dados/votos_partido_deputados_2018_2026.csv`.

---

## 1. Presidente

| Ano | Turno | 1º colocado em Taquarituba | % | 2º colocado | % | Outros relevantes |
|---|---|---|---|---|---|---|
| 1998 | 1º | Fernando Henrique (PSDB) | 71,53 | Lula (PT) | 18,49 | Ciro (PPS) 5,73 |
| 2002 | 1º | Lula (PT) | 49,80 | José Serra (PSDB) | 38,60 | Garotinho 6,64; Ciro 4,67 |
| 2002 | 2º | Lula (PT) | 55,66 | José Serra (PSDB) | 44,34 | |
| 2006 | 1º | Geraldo Alckmin (PSDB) | 62,73 | Lula (PT) | 34,40 | Heloísa Helena 1,81 |
| 2006 | 2º | Geraldo Alckmin (PSDB) | 55,44 | Lula (PT) | 44,56 | |
| 2010 | 1º | Dilma (PT) | 47,71 | José Serra (PSDB) | 43,41 | Marina (PV) 8,43 |
| 2010 | 2º | Dilma (PT) | 51,98 | José Serra (PSDB) | 48,02 | |
| 2014 | 1º | Aécio Neves (PSDB) | 50,24 | Dilma (PT) | 34,38 | Marina (PSB) 13,33 |
| 2014 | 2º | Aécio Neves (PSDB) | 61,51 | Dilma (PT) | 38,49 | |
| 2018 | 1º | Jair Bolsonaro (PSL) | 45,20 | Fernando Haddad (PT) | 23,69 | Alckmin (PSDB) 19,12; Ciro 6,06; Amoêdo 3,58 |
| 2018 | 2º | Jair Bolsonaro (PSL) | 65,59 | Fernando Haddad (PT) | 34,41 | |
| 2022 | 1º | Jair Bolsonaro (PL) | 48,38 | Lula (PT) | 44,27 | Tebet 4,61; Ciro 1,91 |
| 2022 | 2º | Jair Bolsonaro (PL) | 54,77 (7.291 votos) | Lula (PT) | 45,23 (6.021) | |
| 2026 | 1º | Flávio Bolsonaro (PL) | 58,63 (7.881) | Lula (PT) | 34,72 (4.667) | Augusto Cury (AVANTE) 2,77; Renan Santos (MISSÃO) 2,18; Caiado (PSD) 1,45 |

Comparação 2026 com o total do Brasil (fato, TSE): no país, Flávio Bolsonaro teve 47,03% e Lula 45,16% no 1º turno. Taquarituba deu a Flávio 11,6 pontos acima da média nacional e a Lula 10,4 pontos abaixo.

Comparecimento 2026: 14.294 de 18.080 eleitores (79,06%); brancos 3,27%, nulos 2,68% (presidente).

## 2. Governador de São Paulo

| Ano | Vencedor no município | % (turno decisivo no município) | Principal adversário | % |
|---|---|---|---|---|
| 1998 | Mário Covas (PSDB) | 61,69 (2º turno) | Paulo Maluf (PPB) | 38,31 |
| 2002 | Geraldo Alckmin (PSDB) | 56,86 (2º turno) | José Genoíno (PT) | 43,14 |
| 2006 | José Serra (PSDB) | 71,09 (1º turno) | Aloizio Mercadante (PT) | 24,35 |
| 2010 | Geraldo Alckmin (PSDB) | 58,89 (1º turno) | Aloizio Mercadante (PT) | 37,04 |
| 2014 | Geraldo Alckmin (PSDB) | 69,44 (1º turno) | Alexandre Padilha (PT) | 19,14 |
| 2018 | João Doria (PSDB) | 50,03 (2º turno, 5.639 votos) | Márcio França (PSB) | 49,97 (5.633 votos) |
| 2022 | Tarcísio (REPUBLICANOS) | 56,14 (2º turno) | Fernando Haddad (PT) | 43,86 |
| 2026 | Tarcísio (REPUBLICANOS) | 67,24 (1º turno, 8.320 votos) | Fernando Haddad (PT) | 32,02 (3.962) |

Detalhe 2018: no 1º turno Doria teve 44,73%, Marinho (PT) 20,60%, França 18,06%, Skaf 10,19%. A diferença no 2º turno foi de 6 votos.
Detalhe 2022, 1º turno: Tarcísio 42,17%, Haddad 39,53%, Rodrigo Garcia (PSDB) 16,75%.

## 3. Senado

| Ano | Mais votados em Taquarituba |
|---|---|
| 1998 | Oscar (PPB) 40,54%; Suplicy (PT) 24,03%; João Leite Neto (PTB) 23,96% |
| 2002 (2 vagas) | Romeu Tuma (PFL) 26,06%; Mercadante (PT) 23,29%; José Aníbal (PSDB) 22,34%; Quércia (PMDB) 13,61% |
| 2006 | Guilherme Afif (PFL) 65,22%; Suplicy (PT) 30,86% |
| 2010 (2 vagas) | Aloysio Nunes (PSDB) 31,09%; Marta Suplicy (PT) 24,18%; Netinho (PCdoB) 23,57% |
| 2014 | José Serra (PSDB) 65,43%; Suplicy (PT) 27,59% |
| 2018 (2 vagas) | Mara Gabrilli (PSDB) 22,64%; Major Olímpio (PSL) 18,89%; Suplicy (PT) 15,28%; Tripoli (PSDB) 13,26% |
| 2022 | Marcos Pontes (PL) 46,28%; Márcio França (PSB) 37,53%; Edson Aparecido (MDB) 14,28% |
| 2026 (2 vagas) | Guilherme Derrite (PP) 34,28%; André do Prado (PL) 33,56%; Simone Tebet (PSB) 15,91%; Marina Silva (REDE) 14,69% |

Em 2026, Derrite e André do Prado (chapa "Coragem para Seguir Avançando", de Tarcísio) somaram 67,8% dos votos válidos de senador no município e aparecem como eleitos no TSE.

## 4. Deputados mais votados no município

### Deputado federal

| Ano | 1º | 2º | 3º |
|---|---|---|---|
| 1998 | Paulo Kobayashi (PSDB) 43,62% | Cunha Bueno (PPB) 9,25% | Milton Monti (PMDB) 8,59% |
| 2002 | Madeira (PSDB) 45,72% | Orlando Fantazzini (PT) 9,47% | Valdemar Costa Neto (PL) 4,89% |
| 2006 | Arnaldo Madeira (PSDB) 52,26% | Delfim Netto (PMDB) 7,37% | Silvio Torres (PSDB) 3,46% |
| 2010 | Arnaldo Madeira (PSDB) 28,93% | Arlindo Chinaglia (PT) 15,59% | Wanda Corrêa (PTB) 12,35% |
| 2014 | Samuel Moreira (PSDB) 34,97% | Guilherme Mussi (PP) 5,30% | Hamilton Pereira (PT) 4,61% |
| 2018 | Samuel Moreira (PSDB) 22,92% | Paulo Teixeira (PT) 10,90% | Capitão Augusto (PR) 6,94% |
| 2022 | Paulo Teixeira (PT) 13,56% | Samuel Moreira (PSDB) 13,10% | Maurício Neves (PP) 11,20% |
| 2026 | Maurício Neves (PP) 18,41% (2.333 votos) | Lucas Pavanato (PL) 12,26% | Paulo Teixeira (PT) 10,15% |

Seguem em 2026: Vitor Lippi (PSD) 5,54%; Capitão Augusto (PL) 3,97%; Erika Hilton (PSOL) 2,86%; Arlindo Chinaglia (PT) 2,71%.

### Deputado estadual

| Ano | 1º | 2º | 3º |
|---|---|---|---|
| 1998 | Pedro Caruncho (PPB) 45,51% | Edson Aparecido (PSDB) 15,89% | Arnaldo Jardim (PMDB) 3,73% |
| 2002 | Edson Aparecido (PSDB) 44,27% | Levi Montebelo (PV) 8,76% | Tiãozinho (PT) 7,69% |
| 2006 | Sergio Siciliano (PSDB) 61,38% | Beraldo (PSDB) 4,94% | Tiãozinho (PT) 4,74% |
| 2010 | Samuel Moreira (PSDB) 33,38% | Hamilton Pereira (PT) 18,19% | Campos Machado (PTB) 5,29% |
| 2014 | Giriboni (PV) 21,44% | Gonzaga (PSDB) 13,62% | Francisco França (PT) 6,92% |
| 2018 | Edson Giriboni (PV) 23,27% | Carlos Neder (PT) 11,89% | Ricardo Madalena (PR) 8,25% |
| 2022 | Edson Giriboni (UNIÃO) 19,65% | Jé, Jeferson Modesto (PP) 16,30% | Eduardo Suplicy (PT) 15,48% |
| 2026 | Edson Giriboni (UNIÃO) 28,78% (3.622 votos) | Newton Lima (PT) 7,92% | Jé, Jeferson Modesto (PL) 7,53% |

No TSE, Giriboni aparece como "Suplente" em 2018, 2022 e 2026 e "Eleito por QP" em 2014 (situação estadual).

### Votos por partido para deputado (nominal + legenda)

| Partido | Federal 2018 | Federal 2022 | Federal 2026* | Estadual 2018 | Estadual 2022 | Estadual 2026* |
|---|---|---|---|---|---|---|
| PT | 16,8% | 21,8% | 15,6% | 13,6% | 22,2% | 14,6% |
| PSDB | 24,1% | 13,4% | 0,9% | 6,2% | 1,9% | 0,4% |
| PL (PR em 2018) | 14,3% | 21,8% | 25,1% | 13,6% | 20,7% | 30,8% |
| PP | 5,4% | 13,0% | 20,6% | 1,1% | 16,5% | 6,2% |
| UNIÃO (PV/DEM/PSL em 2018) | ver nota | 3,9% | 1,8% | ver nota | 20,9% | 31,9% |
| PSL (2018) | 11,7% | | | 11,3% | | |
| PSD | | 2,6% | 9,0% | 1,4% | 1,2% | 2,3% |
| PSOL | | 2,7% | 5,8% | 5,2% | 2,1% | 3,9% |

\* 2026: votos nominais somados por partido no arquivo oficial do município (o arquivo não separa legenda). Nota: em 2018, PV (com Giriboni) teve 25,5% para estadual. Fonte: `dados/votos_partido_deputados_2018_2026.csv`.

---

## 5. Visão partidária e perfil ideológico (inferência)

Tudo nesta seção é **inferência** a partir dos números acima. Classificação usada: esquerda (PT, PSOL, PCdoB, PSB quando aliado ao PT), centro e centro-direita (PSDB, MDB, PSD, PP tradicional, UNIÃO), direita (PL, PSL 2018, NOVO, Republicanos de Tarcísio).

1. **Eleitorado historicamente tucano até 2014, bolsonarista desde 2018.** De 1998 a 2014 o PSDB venceu todas as disputas para governador e quase todas para presidente no município (exceções: Lula em 2002 e Dilma em 2010, ambos por margem pequena). Em 2018 o voto migra em bloco para Bolsonaro (65,6% no 2º turno) e não volta mais ao PSDB, que cai a 0,9% para deputado federal em 2026.
2. **Direita majoritária, mas com piso petista relevante.** O PT tem um piso de 34% a 45% em 2º turno presidencial (34,4% em 2018, 45,2% em 2022, 34,7% no 1º turno de 2026). Em 2022 a disputa foi apertada (54,8 x 45,2); em 2026 a distância voltou a crescer.
3. **Perfil mais à direita que a média nacional.** Em 2026, 1º turno: Flávio Bolsonaro 58,6% no município contra 47,0% no Brasil. Somando candidatos de direita e centro-direita (Flávio, Cury, Renan Santos, Caiado, Zema) chega-se a cerca de 65%; Lula e demais de esquerda ficam perto de 35%.
4. **Tarcísio e o eixo PL/PP/Republicanos dominam o voto estadual.** Tarcísio subiu de 56% (2º turno de 2022) para 67% (1º turno de 2026). Os dois senadores da chapa dele somaram 68%.
5. **Voto em deputado é regional e pragmático.** O município concentra votos em poucos nomes por ciclo, o que sugere apoio de lideranças locais: Giriboni (mais votado para estadual em quatro eleições seguidas, 2014 a 2026, pelo PV e depois pelo UNIÃO) e, para federal, a sequência Paulo Kobayashi, Arnaldo Madeira, Samuel Moreira (todos PSDB) e agora Maurício Neves (PP, mesmo partido do prefeito). A base geográfica e as emendas desses deputados para o município não foram verificadas nesta pesquisa.
6. **Alinhamento local x estadual.** O prefeito Éder Miano é do PP; em 2026 o PP teve 20,6% para federal (Maurício Neves em 1º) e Derrite (PP) foi o senador mais votado. O PL do vice-presidente da Câmara e de 3 vereadores teve 25% para federal e 31% para estadual. **Inferência**: a base do prefeito (PP, PL, MDB, Republicanos) coincide com o campo que venceu no município em 2022 e 2026.
7. **Classificação resumida**: eleitorado de **centro-direita a direita**, conservador, com forte voto de legenda bolsonarista em eleição nacional, voto personalista em eleição municipal e uma minoria de esquerda estável em torno de um terço.
