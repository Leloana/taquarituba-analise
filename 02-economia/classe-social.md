# Classe social predominante em Taquarituba (SP)

**Tudo neste arquivo é ESTIMATIVA**: classificação própria aplicada sobre dado oficial do IBGE. Não existe estatística oficial de "classe social" por município.

Dados: `dados/classes_estimadas_renda_per_capita.csv` (classes) e `dados/pessoas_por_faixa_renda_per_capita_sm.csv` (dado oficial de origem).

## Método

Base oficial: IBGE Censo 2022, tabela 10296 (https://sidra.ibge.gov.br/tabela/10296), pessoas por faixa de **renda domiciliar per capita** em salários mínimos (SM de 2022 = R$ 1.212). Para 2010, Censo 2010 tabela 3535 (https://sidra.ibge.gov.br/tabela/3535), SM de 2010 = R$ 510.

O critério mais usado na imprensa (classes ABCDE por renda familiar: A acima de 20 SM, B de 10 a 20, C de 4 a 10, D de 2 a 4, E até 2) usa renda **da família inteira**. O IBGE publica faixas **por pessoa**. Para não inventar tamanho de família, as faixas foram convertidas para per capita, supondo uma família típica de cerca de 3 pessoas, e ajustadas aos cortes que o IBGE publica:

| Classe | Renda domiciliar per capita | Equivalente aproximado para família de 3 pessoas |
|---|---|---|
| E | até 1/2 SM (inclui sem rendimento) | até 1,5 SM |
| D | mais de 1/2 até 1 SM | 1,5 a 3 SM |
| C | mais de 1 até 3 SM | 3 a 9 SM |
| B | mais de 3 até 10 SM | 9 a 30 SM |
| A | mais de 10 SM | mais de 30 SM |

Limites do método:
- O Critério Brasil (ABEP), usado em pesquisa de mercado, classifica por posse de bens e escolaridade, não por renda. Não há dado municipal para aplicá-lo.
- Faixas em SM mudam de valor real com o tempo. O SM subiu cerca de 15% acima do IPCA entre 2010 e 2022, então "1 SM" em 2022 é uma linha mais alta que em 2010. A comparação 2010 x 2022 é só indicativa.
- A renda do Censo é declarada e tende a subestimar o topo.

## Resultado 2022 (% das pessoas)

| Local | E | D | C | B | A |
|---|---|---|---|---|---|
| **Taquarituba** | **23,1** | **36,4** | **34,1** | **5,7** | **0,7** |
| Avaré | 18,7 | 31,4 | 41,3 | 8,0 | 0,6 |
| Itaí | 27,8 | 32,7 | 33,6 | 5,8 | 0,1 |
| Fartura | 24,6 | 31,6 | 38,5 | 5,1 | 0,3 |
| Itaporanga | 26,4 | 41,5 | 28,0 | 3,8 | 0,3 |
| Coronel Macedo | 25,8 | 44,1 | 26,4 | 3,7 | 0,1 |
| Taguaí | 18,9 | 41,2 | 37,0 | 2,8 | 0,1 |
| Estado de SP | 20,2 | 27,8 | 39,5 | 11,1 | 1,4 |
| Brasil | 31,8 | 29,2 | 30,2 | 7,8 | 0,9 |

Faixas oficiais de Taquarituba em 2022 (IBGE, tabela 10296): sem rendimento 1,37%; até 1/4 SM 3,81%; 1/4 a 1/2 SM 17,87%; 1/2 a 1 SM 36,42%; 1 a 2 SM 27,99%; 2 a 3 SM 6,16%; 3 a 5 SM 4,31%; 5 a 10 SM 1,39%; 10 a 15 SM 0,44%; 15 a 20 SM 0,23%; mais de 20 SM 0 pessoas (sinal "-" no SIDRA).

## Resultado 2010 (% das pessoas)

| Local | E | D | C | B (3 a 5 SM) | acima de 5 SM |
|---|---|---|---|---|---|
| **Taquarituba** | **28,2** | **36,5** | **29,3** | **4,1** | **1,8** |
| Estado de SP | 19,4 | 27,5 | 39,0 | 7,2 | 6,9 |

Em 2010 o IBGE agrupa tudo acima de 5 SM, então B alta e A não se separam.

## Conclusão

- **Classe predominante: D (renda por pessoa entre meio e um salário mínimo), com C logo atrás.** 36% da população está em D e 34% em C. Somando E e D, **59,5% das pessoas viviam com até 1 SM per capita** em 2022 (estado: 48%).
- A pessoa mediana (R$ 1.102 per capita, Censo 2022) está na **fronteira entre D e C**. Numa família de 3 pessoas isso dá cerca de R$ 3.300 por mês, uns 2,7 SM, que no critério familiar tradicional também cai em **classe D (2 a 4 SM)**.
- Topo fino: B mais A somam 6,4% (estado: 12,5%). Ninguém declarou renda per capita acima de 20 SM.
- Entre 2010 e 2022 a classe E encolheu (28% para 23%) e a C cresceu (29% para 34%), mesmo com o SM real mais alto. É sinal de mobilidade para cima na base.
- Comparada aos vizinhos, Taquarituba é mais "classe média baixa" que Itaporanga, Coronel Macedo e Taguaí, e um pouco abaixo de Avaré.

Indicador independente que confirma o quadro: o Caravela, com dados da RAIS (só emprego formal), diz que as faixas E e D concentram 58,3% do total de remunerações da cidade e A e B 3,3% (https://www.caravela.info/municipios/sp/taquarituba-sp, acesso em 20/10/2026, ano da RAIS não informado na página; critério do Caravela não detalhado).
