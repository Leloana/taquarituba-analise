# Taquarituba (SP): voto por faixa de renda (estimativa ecológica)

Data de referência: 20/10/2026. Cruzamento próprio entre a votação por seção do TSE (agregada nos 8 locais de votação do município) e a renda dos setores censitários do IBGE 2022 em volta de cada local.

**Tudo neste arquivo é estimativa ecológica.** Mostra como votaram *lugares* de renda diferente, não *pessoas* de renda diferente. Concluir que "o eleitor de renda alta votou X" a partir daqui é falácia ecológica.

Gráficos: [16-voto-x-renda-dispersao.svg](../graficos/16-voto-x-renda-dispersao.svg) e [17-voto-por-faixa-renda.svg](../graficos/17-voto-por-faixa-renda.svg). Dados: [dados/voto_por_local_votacao_2022.csv](dados/voto_por_local_votacao_2022.csv), [2024](dados/voto_por_local_votacao_2024.csv), [2026](dados/voto_por_local_votacao_2026.csv) e [dados/voto_por_faixa_renda.csv](dados/voto_por_faixa_renda.csv). Código: [../scripts/voto_por_renda.py](../scripts/voto_por_renda.py).

## Resumo

- **Nas eleições nacionais e estaduais, quanto maior a renda do entorno do local de votação, maior o voto na direita.** No 2º turno de 2022, Bolsonaro teve 46,6% dos válidos no terço de menor renda, 56,8% no do meio e 60,3% no de maior renda. Lula venceu só no terço de baixo (53,4%).
- **2026 repete o desenho, com tudo deslocado para a direita.** Flávio Bolsonaro teve 52,7%, 59,6% e 63,0% nos três terços; venceu até nos locais mais pobres. Lula caiu de 53,4% (2º turno 2022) para 41,0% (1º turno 2026) no terço de baixo. A comparação mistura 2º e 1º turno, então serve como ordem de grandeza.
- **Governador acompanha:** Tarcísio 48,3% / 58,2% / 61,1% em 2022 (2º turno) e 61,4% / 67,7% / 71,8% em 2026 (1º turno).
- **Na eleição municipal o sinal se inverte.** Éder Miano (PP), prefeito reeleito em 2024, teve 63,8% no terço de menor renda e 54,4% no de maior renda. Marcelo Milla (PSD) foi mais forte no centro.
- **Correlação forte, mas com só 8 pontos.** Entre % do candidato bolsonarista e renda do entorno: r = 0,90 (presidente 2022) e r = 0,80 (presidente 2026). Cada R$ 1.000 a mais de renda média no entorno corresponde a cerca de +9,5 pontos para Bolsonaro em 2022 e +6,5 para Flávio em 2026 (reta ponderada por votos válidos).
- **A diferença de renda entre os terços é pequena em termos absolutos:** de 1,4 a 2,5 salários mínimos de 2022 de renda média do responsável. Não há "bairro rico" no sentido de capital; o terço "alto" é o centro antigo e a Bela Vista.

## Fontes

- Votação por seção, TSE, dados abertos (recorte do município 71773):
  - Presidente 2022 e 2026: https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_secao/votacao_secao_2022_BR.zip e https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_secao/votacao_secao_2026_BR.zip (o arquivo de SP não traz presidente).
  - Governador 2022 e 2026, prefeito 2024: https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_secao/votacao_secao_2022_SP.zip, https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_secao/votacao_secao_2024_SP.zip, https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_secao/votacao_secao_2026_SP.zip (este último publicado em 06/10/2026).
- Eleitores aptos por seção (2022 e 2024): https://cdn.tse.jus.br/estatistica/sead/odsele/detalhe_votacao_secao/detalhe_votacao_secao_2022.zip e https://cdn.tse.jus.br/estatistica/sead/odsele/detalhe_votacao_secao/detalhe_votacao_secao_2024.zip. O de 2026 ainda não estava publicado em 20/10/2026, por isso a coluna `aptos` de 2026 fica vazia.
- Locais de votação com endereço e latitude/longitude: https://cdn.tse.jus.br/estatistica/sead/odsele/eleitorado_locais_votacao/eleitorado_local_votacao_2024.zip. Os mesmos 8 locais, com os mesmos códigos e coordenadas, aparecem em 2022 e em 2024; em 2026 os códigos de local na votação por seção são os mesmos. O arquivo de 2026 estava vazio em 20/10/2026.
- Renda: IBGE, Censo 2022, agregados por setor censitário, rendimento médio do responsável pelo domicílio (https://ftp.ibge.gov.br/Censos/Censo_Demografico_2022/Agregados_por_Setores_Censitarios_Rendimento_do_Responsavel/), já organizado em [../03-bairros/dados/setores_censitarios_2022_taquarituba.csv](../03-bairros/dados/setores_censitarios_2022_taquarituba.csv).
- Polígonos dos setores: malha IBGE 2022 (https://ftp.ibge.gov.br/Censos/Censo_Demografico_2022/Agregados_por_Setores_Censitarios/malha_com_atributos/setores/).

Conferência: as somas por local batem com os totais oficiais do município já registrados neste dossiê (presidente 2022, 2º turno: Bolsonaro 7.291, Lula 6.021; presidente 2026: Flávio 7.881, Lula 4.667; prefeito 2024: Éder 8.224, Marcelo 5.951; comparecimento 2026: 14.294).

## Método

1. **Votos por local.** Somei os votos de cada seção no seu local de votação (`NR_LOCAL_VOTACAO`). São 64 seções em 8 locais, todos escolas. Percentuais sobre votos válidos (sem brancos e nulos).
2. **Local no mapa.** Coordenada do cadastro do TSE; o setor censitário que contém o ponto foi achado por ponto em polígono na malha do IBGE.
3. **Renda do entorno (medida principal).** Média da renda média do responsável dos setores cujo centróide fica a até 500 m do local (mais o próprio setor do local), ponderada pelo número de domicílios. Entram de 3 a 11 setores por local.
4. **Medidas alternativas (robustez).** (a) Renda só do setor onde fica a escola. (b) "Área de influência": cada um dos 76 setores vai para o local de votação mais próximo e a renda é a média ponderada desses setores.
5. **Faixas.** Ordenei os locais pela renda do entorno e cortei em terços aproximados do comparecimento do 2º turno de 2022 (cada local inteiro vai para um terço). Os terços ficaram com 3, 3 e 2 locais e 4.486, 4.847 e 4.831 votantes em 2022. A mesma divisão de locais vale para todas as eleições. O agregado por faixa soma votos (não faz média de percentuais).
6. **Correlação.** Pearson entre % do 1º candidato e renda do entorno; também a versão ponderada por votos válidos e a inclinação da reta ponderada. Com n = 8, calculei o p bicaudal exato por permutação (todas as 40.320 ordens).

## Limitações

- **Falácia ecológica.** O dado é do lugar, não da pessoa. Um local de renda alta pode ter dado mais votos à direita porque nele votam mais aposentados, mais proprietários, mais evangélicos ou mais funcionários públicos, e não por causa da renda.
- **O eleitor não vota necessariamente perto de casa.** O local é definido quando a pessoa tira ou transfere o título e muitos nunca mudam depois de se mudar. Em cidade pequena isso é forte: as três escolas do centro (EMEI Julieta, ETEC e EE José Penna) têm 8.754 eleitores aptos em 2022, mas a população dos setores mais próximos delas soma 5.664 pessoas de todas as idades. Ou seja, o centro recebe eleitores de bairros afastados e da zona rural. Já a área mais próxima da EMEI Virgínia (Vila São Vicente) tem 6.251 moradores e só 2.934 eleitores votando lá. A associação local x renda é aproximada.
- **n = 8.** São só 8 locais. A correlação é forte e o teste por permutação dá p entre 0,001 e 0,03 nas eleições gerais, mas um local diferente pode mexer bastante no número. No prefeito 2024 o p é 0,07.
- **Seção não ajuda.** Dentro de uma escola as seções não correspondem a ruas ou bairros; por isso não usei a seção como unidade geográfica.
- **Tempo.** Renda é de 2022 (Censo). O conjunto CDHU de 253 casas entregue em 01/2026 na Vila Santa Rita não está na renda; seus moradores votam onde estava o título.
- **Rural e presídio.** Os eleitores da zona rural (Barreiro, Muniz, Porto Taquari) não têm local próprio e votam na sede; a renda deles não entra no entorno de nenhuma escola urbana.
- **Medida sensível ao recorte.** Com a renda só do setor da escola, a correlação cai (r = 0,61 em 2022 e 0,31 em 2026), porque o setor da EMEI Bernadete (Novo Centro, R$ 4.200) e da EMEI Virgínia (R$ 3.191) são ilhas mais ricas dentro de entornos mais modestos. Com a área de influência, fica igual à principal (r = 0,92 e 0,81). Tirando o local rural (Aleixos), também se mantém (0,90 e 0,76).

## Resultados por local de votação

Renda: média do responsável no entorno de 500 m, Censo 2022. Votantes = comparecimento. % sobre válidos.

| Local (bairro no cadastro TSE) | Setor IBGE do local, bairro reconstruído | Renda entorno | Terço | Votantes 2022 2ºT | Bolsonaro 2022 2ºT | Lula 2022 2ºT | Flávio 2026 1ºT | Lula 2026 1ºT | Éder 2024 |
|---|---|---|---|---|---|---|---|---|---|
| EMEI Maria de Lourdes (Vila Santa Rita) | Vila Santa Rita de Cássia | R$ 1.517 | baixa | 1.564 | 42,2% | 57,8% | 50,7% | 43,7% | 66,4% |
| EM Célia de Castilhos (Aleixos) | Bairro dos Aleixos | R$ 1.719 | baixa | 534 | 42,9% | 57,1% | 52,1% | 44,4% | 54,2% |
| EMEI Virgínia (Vila São Vicente) | Nova Vila Mendes / Jardim São Pedro | R$ 1.880 | baixa | 2.388 | 50,4% | 49,6% | 54,1% | 38,5% | 64,1% |
| EMEI Maria Esther (Pedro Mário de Barros) | Pedro Mário de Barros | R$ 2.058 | média | 947 | 55,1% | 44,9% | 62,9% | 31,8% | 64,4% |
| EMEI Bernadete (Novo Centro) | Residencial Novo Centro / Colina Verde | R$ 2.613 | média | 1.591 | 59,5% | 40,5% | 60,6% | 32,5% | 56,4% |
| EMEI Julieta (Centro) | Centro | R$ 2.856 | média | 2.309 | 55,7% | 44,3% | 57,4% | 36,2% | 52,8% |
| ETEC Terezinha Monteiro (Centro) | Centro | R$ 2.914 | alta | 2.553 | 59,5% | 40,5% | 61,8% | 30,2% | 54,7% |
| EE José Penna (Bela Vista) | Centro | R$ 3.288 | alta | 2.278 | 61,2% | 38,8% | 64,6% | 29,3% | 54,0% |

Governador e o detalhe completo (aptos, brancos, nulos, outros candidatos, renda pelas medidas alternativas) estão nos CSVs.

## Resultados por faixa de renda (terços de eleitorado)

Renda média do entorno, ponderada pelo comparecimento: baixa R$ 1.734 (1,43 SM de 2022), média R$ 2.620 (2,16 SM), alta R$ 3.090 (2,55 SM).

| Eleição | 1º candidato x 2º | Renda baixa | Renda média | Renda alta | Diferença alta menos baixa (1º cand.) |
|---|---|---|---|---|---|
| Presidente 2022, 2º turno | Bolsonaro x Lula | 46,6 x 53,4 | 56,8 x 43,2 | 60,3 x 39,7 | +13,7 pp |
| Governador 2022, 2º turno | Tarcísio x Haddad | 48,3 x 51,7 | 58,2 x 41,8 | 61,1 x 38,9 | +12,8 pp |
| Prefeito 2024 | Éder Miano (PP) x Marcelo Milla (PSD) | 63,8 x 36,2 | 56,3 x 43,7 | 54,4 x 45,6 | −9,4 pp |
| Presidente 2026, 1º turno | Flávio Bolsonaro x Lula (outros) | 52,7 x 41,0 (6,3) | 59,6 x 34,0 (6,4) | 63,0 x 29,8 (7,2) | +10,3 pp |
| Governador 2026, 1º turno | Tarcísio x Haddad (outros) | 61,4 x 37,7 (0,9) | 67,7 x 31,7 (0,6) | 71,8 x 27,4 (0,8) | +10,4 pp |

## Correlação com a renda do entorno (n = 8 locais)

| Eleição | r | r ponderado | Inclinação (pp por R$ 1.000) | p (permutação) | r, área de influência | r, só setor da escola | r, sem Aleixos |
|---|---|---|---|---|---|---|---|
| Bolsonaro, pres. 2022 2ºT | 0,90 | 0,92 | +9,5 | 0,001 | 0,92 | 0,61 | 0,90 |
| Tarcísio, gov. 2022 2ºT | 0,88 | 0,89 | +8,8 | 0,002 | 0,90 | 0,62 | 0,87 |
| Éder Miano, pref. 2024 | −0,71 | −0,87 | −7,5 | 0,071 | −0,74 | −0,49 | −0,95 |
| Flávio Bolsonaro, pres. 2026 1ºT | 0,80 | 0,84 | +6,5 | 0,028 | 0,81 | 0,31 | 0,76 |
| Tarcísio, gov. 2026 1ºT | 0,79 | 0,81 | +6,4 | 0,022 | 0,80 | 0,40 | 0,76 |

## Leitura

Tudo abaixo é **inferência** sobre os números acima.

- **O padrão nacional de renda aparece também dentro da cidade.** Os locais do centro antigo e da Bela Vista dão mais voto à direita; Vila Santa Rita e Aleixos foram os únicos lugares onde Lula venceu com folga em 2022. É o mesmo sentido das pesquisas nacionais (abaixo), embora aqui a escala de renda seja curta e a unidade seja o lugar.
- **Em 2026 a direita avançou em todas as faixas e mais na de baixo.** Lula perdeu cerca de 12 pontos no terço de menor renda entre o 2º turno de 2022 e o 1º turno de 2026, contra cerca de 9 a 10 nos outros dois. Parte disso é efeito de 1º turno (os demais candidatos somaram de 6% a 7% dos válidos em cada faixa). O 2º turno de 2026 vai mostrar se o gradiente encolhe.
- **Pedro Mário de Barros foge da reta**: renda de entorno modesta (R$ 2.058) e voto bolsonarista alto (55% em 2022, 63% em 2026). Pode ser perfil de loteamento novo de casa própria, ou eleitores do vetor leste de renda alta votando nessa escola; não dá para separar com estes dados.
- **No município a lógica é outra.** O prefeito Éder Miano foi mais forte justamente nos locais de renda baixa (Vila Santa Rita, Vila São Vicente, Pedro Mário de Barros), onde costuma pesar a presença da prefeitura em serviços e obras; a oposição (PSD, com PSDB e União na coligação) foi melhor no centro. Isso é coerente com o histórico de eleição municipal pouco alinhada à disputa nacional (ver [eleicoes-municipais.md](eleicoes-municipais.md)).
- **A força da direita em Taquarituba não é só de renda.** Mesmo o terço de menor renda deu maioria a Flávio e a Tarcísio em 2026. A renda explica a diferença entre lugares, não o nível geral.

## O que as pesquisas dizem (separado do cálculo acima)

Não achei pesquisa eleitoral registrada para Taquarituba nem estudo publicado de voto por renda no município ou na região de Avaré e Itapeva. O que há é pesquisa nacional por renda familiar declarada pelo entrevistado (renda da família, não do responsável, e em faixas diferentes das daqui):

- **Datafolha, 22 e 23/09/2026, Brasil, 2.002 entrevistas, registro BR-00304/2026, intenção de voto estimulada no 1º turno:** Lula 46% x Flávio 32% entre renda familiar até 2 SM; 34% x 40% de mais de 2 a 5 SM; 33% x 43% acima de 5 SM. No interior, 38% x 38%. Fonte: relatório Datafolha publicado pelo Poder360, https://static.poder360.com.br/uploads/2026/10/pesquisa-datafolha-23set-presidente.pdf
- **Datafolha, 27 e 28/07/2022, Brasil, registro BR-01192/2022, 1º turno:** Lula 54% x Bolsonaro 23% até 2 SM; 40% x 34% de 2 a 5 SM; 44% x 34% de 5 a 10 SM; 41% x 33% acima de 10 SM. Fonte: https://www.poder360.com.br/pesquisas/datafolha-bolsonaro-tem-leve-alta-entre-eleitores-de-baixa-renda/
- Não localizei a tabela por renda da última pesquisa Datafolha do 2º turno de 2022 (28 e 29/10/2022, BR-08297/2022); o relatório publicado traz só o perfil da amostra por renda (https://static.poder360.com.br/2022/12/datafolha-BR-082972022-1.pdf).

As pesquisas medem indivíduos e confirmam o sentido do gradiente (renda mais alta, mais voto no candidato do PL). O cruzamento deste arquivo mede lugares e não pode ser comparado ponto a ponto com elas.

## Como refazer

Baixar os arquivos listados em Fontes (os zips de votação por seção têm de 0,5 a 0,9 GB; dá para recortar em streaming, ex. `curl -s URL | funzip | awk 'NR==1 || /"TAQUARITUBA"/' > votacao_secao_2022_SP.csv`), pôr os CSVs num diretório com os nomes originais do TSE e rodar:

```
python scripts/voto_por_renda.py preparar --tse DIRETORIO_TSE --malha SP_setores_CD2022.gpkg
```

Sem argumentos, o script só refaz os gráficos 16 e 17 a partir dos CSVs do repo.
