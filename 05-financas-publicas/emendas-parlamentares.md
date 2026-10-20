# Emendas parlamentares destinadas a Taquarituba

CSVs: [dados/emendas_federais_cgu_por_favorecido.csv](dados/emendas_federais_cgu_por_favorecido.csv), [dados/emendas_federais_resumo_por_autor.csv](dados/emendas_federais_resumo_por_autor.csv), [dados/emendas_estaduais_sp_taquarituba.csv](dados/emendas_estaduais_sp_taquarituba.csv).

## Método

- **Federais**: base completa de emendas do Portal da Transparência/CGU, arquivo `EmendasParlamentares_PorFavorecido.csv` (versão de 09/10/2026), baixado de https://portaldatransparencia.gov.br/download-de-dados/emendas-parlamentares/UNICO. Filtrei favorecidos com município = Taquarituba/SP. O valor é o **efetivamente pago** ao favorecido no ano (não o empenhado). Inclui repasses fundo a fundo ao Fundo Municipal de Saúde e repasses diretos a entidades (Santa Casa, APAE).
- Limitação: emendas executadas via contrato de repasse da Caixa ou pagas a fornecedores de outra cidade podem não aparecer como favorecido de Taquarituba. Exemplo: a base principal lista uma emenda de **Felipe Becari** de 2024 (urbanismo, R$ 1.000.000,00 empenhado, apenas R$ 39.981,00 pagos em restos a pagar), localidade Taquarituba ([arquivo EmendasParlamentares.csv, mesma base CGU](https://portaldatransparencia.gov.br/download-de-dados/emendas-parlamentares/UNICO)).
- **Estaduais**: não há base única aberta por município. Usei os PDFs de emendas impositivas 2020 a 2022 do Governo SP, o Diário Oficial do município e o quadro consolidado de emendas 2025 da ALESP. Lista **parcial**.

## 1. Emendas federais: totais por ano de pagamento (cálculo próprio sobre a base CGU)

| Ano | Valor pago a favorecidos de Taquarituba (R$) |
|---|---:|
| 2016 | 100.000,00 |
| 2017 | 397.550,00 |
| 2018 | 22,31 |
| 2019 | 439.051,42 |
| 2020 | 1.025.379,21 |
| 2021 | 997.980,95 |
| 2022 | 125.156,79 |
| 2023 | 839.752,86 |
| 2024 | 1.536.568,00 |
| 2025 | 2.994.665,00 |
| 2026 (até 09/10) | 2.739.711,00 |
| **Total 2016-2026** | **11.195.837,54** |

Por tipo (2016 a 2026): individuais com finalidade definida R$ 6,63 mi; transferências especiais (Pix) R$ 2,21 mi; comissão R$ 1,45 mi; relator (RP9) R$ 0,82 mi; bancada R$ 0,09 mi.

Por favorecido: Fundo Municipal de Saúde R$ 4,61 mi; Município (Prefeitura) R$ 4,40 mi; Santa Casa R$ 1,46 mi; Fundo Municipal de Assistência Social R$ 0,45 mi; APAE R$ 0,28 mi.

**Tendência:** os valores triplicaram a partir de 2024. 2025 e 2026 juntos (R$ 5,73 mi) superam todo o período 2016-2024 (R$ 5,46 mi). Quase tudo vai para custeio da saúde ("incremento temporário" da atenção primária e hospitalar), ou seja, dinheiro que entra e sai no mesmo ano, sem virar obra.

Conferência com a contabilidade municipal: o DCA 2025 registra R$ 1.807.410,00 de "Transferência Especial da União" ([DCA 2025](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2025&no_anexo=DCA-Anexo%20I-C&id_ente=3553807)), mais que os R$ 693 mil de Pix pagos em 2025 segundo a CGU; a diferença pode ser de data de registro ou de emendas Pix de exercícios anteriores. A RCL deduz como emendas individuais R$ 2,30 mi em 2025 e R$ 2,44 mi nos 12 meses até ago/2026 ([RGF](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rgf?an_exercicio=2026&in_periodicidade=Q&nr_periodo=2&co_tipo_demonstrativo=RGF&no_anexo=RGF-Anexo%2001&co_esfera=M&co_poder=E&id_ente=3553807)).

## 2. Emendas federais: lista completa (2016 a 2026, pagamentos acima de R$ 1 mil)

| Ano pgto | Parlamentar | Tipo | Favorecido | Ação (objeto) | Valor (R$) |
|---|---|---|---|---|---:|
| 2016 | Aline Correa | Individual (finalidade definida) | Municipio De Taquarituba | Estruturacao da rede de servicos de protecao social especial | 100.000,00 |
| 2017 | Guilherme Mussi | Individual (finalidade definida) | Santa Casa De Misericordia De Taquarituba | Estruturacao de unidades de atencao especializada em saude | 100.000,00 |
| 2017 | Paulo Teixeira | Individual (finalidade definida) | Santa Casa De Misericordia De Taquarituba | Estruturacao de unidades de atencao especializada em saude | 149.900,00 |
| 2017 | Samuel Moreira | Individual (finalidade definida) | Municipio De Taquarituba | Apoio a politica nacional de desenvolvimento urbano voltado a implantacao e qualificacao viaria | 147.650,00 |
| 2019 | Dr. Sinval Malheiros | Individual (finalidade definida) | A P A E De Taquarituba | Estruturacao de unidades de atencao especializada em saude | 95.115,70 |
| 2019 | Eli Correa Filho | Individual (finalidade definida) | Municipio De Taquarituba | Apoio a politica nacional de desenvolvimento urbano voltado a implantacao e qualificacao viaria | 54.095,24 |
| 2019 | Jorge Tadeu Mudalen | Individual (finalidade definida) | Santa Casa De Misericordia De Taquarituba | Estruturacao de unidades de atencao especializada em saude | 50.000,00 |
| 2019 | Samuel Moreira | Individual (finalidade definida) | Municipio De Taquarituba | Apoio a politica nacional de desenvolvimento urbano voltado a implantacao e qualificacao viaria | 147.650,00 |
| 2019 | Samuel Moreira | Individual (finalidade definida) | Municipio De Taquarituba | Apoio a politica nacional de desenvolvimento urbano voltado a implantacao e qualificacao viaria | 92.190,48 |
| 2020 | Arlindo Chinaglia | Individual, transferência especial (Pix) | Municipio De Taquarituba | Transferencias especiais | 150.000,00 |
| 2020 | Capitao Augusto | Individual (finalidade definida) | A P A E De Taquarituba | Estruturacao de unidades de atencao especializada em saude | 90.236,36 |
| 2020 | Eli Correa Filho | Individual (finalidade definida) | Municipio De Taquarituba | Apoio a politica nacional de desenvolvimento urbano voltado a implantacao e qualificacao viaria | 216.380,95 |
| 2020 | Jorge Tadeu Mudalen | Individual (finalidade definida) | Santa Casa De Misericordia De Taquarituba | Estruturacao de unidades de atencao especializada em saude | 200.000,00 |
| 2020 | Samuel Moreira | Individual (finalidade definida) | Municipio De Taquarituba | Apoio a politica nacional de desenvolvimento urbano voltado a implantacao e qualificacao viaria | 368.761,90 |
| 2021 | Arlindo Chinaglia | Individual (finalidade definida) | Municipio De Taquarituba | Apoio a politica nacional de desenvolvimento urbano voltado a implantacao e qualificacao viaria | 238.750,00 |
| 2021 | Guilherme Derrite | Individual, transferência especial (Pix) | Municipio De Taquarituba | Transferencias especiais | 250.000,00 |
| 2021 | Guilherme Mussi | Individual, transferência especial (Pix) | Municipio De Taquarituba | Transferencias especiais | 250.000,00 |
| 2021 | Relator Geral | Relator (RP9) | Municipio De Taquarituba | Múltiplo | 100.275,00 |
| 2021 | Samuel Moreira | Individual (finalidade definida) | Santa Casa De Misericordia De Taquarituba | Estruturacao de unidades de atencao especializada em saude | 36.315,95 |
| 2021 | Vinicius Carvalho | Individual (finalidade definida) | Santa Casa De Misericordia De Taquarituba | Estruturacao de unidades de atencao especializada em saude | 122.640,00 |
| 2022 | Renata Abreu | Individual (finalidade definida) | A P A E De Taquarituba | Estruturacao de unidades de atencao especializada em saude | 61.556,79 |
| 2022 | Samuel Moreira | Individual (finalidade definida) | Santa Casa De Misericordia De Taquarituba | Estruturacao de unidades de atencao especializada em saude | 63.600,00 |
| 2023 | Arlindo Chinaglia | Individual, transferência especial (Pix) | Municipio De Taquarituba | Transferencias especiais | 250.000,00 |
| 2023 | Paulo Teixeira | Individual (finalidade definida) | Fundo Municipal Da Saude | Estruturacao de unidades de atencao especializada em saude | 323.812,00 |
| 2023 | Paulo Teixeira | Individual (finalidade definida) | Santa Casa De Misericordia De Taquarituba | Estruturacao de unidades de atencao especializada em saude | 236.500,00 |
| 2023 | Renata Abreu | Individual (finalidade definida) | A P A E De Taquarituba | Estruturacao de unidades de atencao especializada em saude | 29.440,86 |
| 2024 | Arlindo Chinaglia | Individual, transferência especial (Pix) | Municipio De Taquarituba | Transferencias especiais | 120.000,00 |
| 2024 | Capitao Augusto | Individual, transferência especial (Pix) | Municipio De Taquarituba | Transferencias especiais | 200.000,00 |
| 2024 | Mauricio Neves | Individual, transferência especial (Pix) | Municipio De Taquarituba | Transferencias especiais | 300.000,00 |
| 2024 | Relator Geral | Relator (RP9) | Municipio De Taquarituba | Múltiplo | 716.568,00 |
| 2024 | Vicentinho | Individual (finalidade definida) | Fundo Municipal Da Saude | Estruturacao da rede de servicos de atencao primaria a saude | 200.000,00 |
| 2025 | Arlindo Chinaglia | Individual (finalidade definida) | Fundo Municipal Da Saude | Estruturacao da rede de servicos de atencao primaria a saude | 100.000,00 |
| 2025 | Capitao Augusto | Individual (finalidade definida) | Fundo Municipal Da Saude | Incremento temporario ao custeio dos servicos de assistencia hospitalar e ambulatorial para cumprimento de metas | 200.000,00 |
| 2025 | Cezinha De Madureira | Individual (finalidade definida) | Santa Casa De Misericordia De Taquarituba | Estruturacao de unidades de atencao especializada em saude | 250.000,00 |
| 2025 | Cezinha De Madureira | Individual (finalidade definida) | Santa Casa De Misericordia De Taquarituba | Estruturacao de unidades de atencao especializada em saude | 250.000,00 |
| 2025 | Com. Da Saude | Comissão | Fundo Municipal Da Saude | Incremento temporario ao custeio dos servicos de atencao primaria a saude para cumprimento de metas | 500.000,00 |
| 2025 | Com. Da Saude | Comissão | Fundo Municipal Da Saude | Incremento temporario ao custeio dos servicos de assistencia hospitalar e ambulatorial para cumprimento de metas | 500.000,00 |
| 2025 | Mauricio Neves | Individual, transferência especial (Pix) | Municipio De Taquarituba | Transferencias especiais | 495.000,00 |
| 2025 | Nilto Tatto | Individual (finalidade definida) | Virginia Da Ascencao Costa | Preservacao do patrimonio cultural brasileiro | 1.530,00 |
| 2025 | Vicentinho | Individual, transferência especial (Pix) | Municipio De Taquarituba | Transferencias especiais | 198.000,00 |
| 2025 | Vitor Lippi | Individual (finalidade definida) | Fundo Municipal Da Saude | Incremento temporario ao custeio dos servicos de assistencia hospitalar e ambulatorial para cumprimento de metas | 500.000,00 |
| 2026 | Bancada De Sao Paulo | Bancada | Fundo Municipal Da Saude | Incremento temporario ao custeio dos servicos de assistencia hospitalar e ambulatorial para cumprimento de metas | 89.711,00 |
| 2026 | Com. Da Saude | Comissão | Fundo Municipal Da Saude | Incremento temporario ao custeio dos servicos de atencao primaria a saude para cumprimento de metas | 200.000,00 |
| 2026 | Com. De Previ., Assis. Soci, Infan., Adol. E Famil | Comissão | Fundo Municipal De Assistencia Social | Estruturacao da rede de servicos e fortalecimento da gestao do sistema unico de assistencia social (suas) | 250.000,00 |
| 2026 | Eduardo Bolsonaro | Individual (finalidade definida) | Fundo Municipal Da Saude | Incremento temporario ao custeio dos servicos de assistencia hospitalar e ambulatorial para cumprimento de metas | 400.000,00 |
| 2026 | Guilherme Derrite | Individual (finalidade definida) | Fundo Municipal Da Saude | Incremento temporario ao custeio dos servicos de atencao primaria a saude para cumprimento de metas | 300.000,00 |
| 2026 | Luiz Carlos Motta | Individual (finalidade definida) | Fundo Municipal Da Saude | Incremento temporario ao custeio dos servicos de assistencia hospitalar e ambulatorial para cumprimento de metas | 100.000,00 |
| 2026 | Marcio Alvino | Individual (finalidade definida) | Fundo Municipal De Assistencia Social | Estruturacao da rede de servicos e fortalecimento da gestao do sistema unico de assistencia social (suas) | 100.000,00 |
| 2026 | Mauricio Neves | Individual (finalidade definida) | Fundo Municipal De Assistencia Social | Estruturacao da rede de servicos e fortalecimento da gestao do sistema unico de assistencia social (suas) | 100.000,00 |
| 2026 | Simone Marquetto | Individual (finalidade definida) | Fundo Municipal Da Saude | Incremento temporario ao custeio dos servicos de atencao primaria a saude para cumprimento de metas | 1.000.000,00 |
| 2026 | Vicentinho | Individual (finalidade definida) | Fundo Municipal Da Saude | Estruturacao da rede de servicos de atencao primaria a saude | 200.000,00 |

Fonte de todas as linhas: CGU, `EmendasParlamentares_PorFavorecido.csv` e `EmendasParlamentares.csv` (para ação orçamentária), https://portaldatransparencia.gov.br/download-de-dados/emendas-parlamentares/UNICO.

### Parlamentares federais que mais enviaram (valor pago, 2016 a 2026)

| # | Autor | Total (R$) |
|---|---|---:|
| 1 | Comissão de Saúde da Câmara | 1.200.000,00 |
| 2 | Simone Marquetto | 1.000.000,00 |
| 3 | Mauricio Neves | 895.000,00 |
| 4 | Arlindo Chinaglia | 858.750,00 |
| 5 | Samuel Moreira | 856.168,33 |
| 6 | Relator-geral (RP9) | 816.843,00 |
| 7 | Paulo Teixeira | 710.212,00 |
| 8 | Vicentinho | 598.000,00 |
| 9 | Guilherme Derrite | 550.000,00 |
| 10 | Vitor Lippi | 500.000,00 |
| 10 | Cezinha de Madureira | 500.000,00 |
| 12 | Capitão Augusto | 490.236,36 |
| 13 | Eduardo Bolsonaro | 400.000,00 |
| 14 | Guilherme Mussi | 350.000,00 |
| 15 | Eli Corrêa Filho | 270.476,19 |

Fonte: [dados/emendas_federais_resumo_por_autor.csv](dados/emendas_federais_resumo_por_autor.csv), cálculo próprio sobre a base CGU.

**Análise:** não há um "padrinho" federal dominante. Chinaglia e Paulo Teixeira (PT) aparecem em vários anos; Samuel Moreira (PSDB) concentrou 2017 a 2022; a partir de 2024 aparecem nomes do PL/Republicanos/PP (Mauricio Neves, Capitão Augusto, Derrite, Eduardo Bolsonaro, Simone Marquetto), alinhados à coligação do prefeito (PP, MDB, PL, Republicanos, Avante, segundo o [TSE](https://divulgacandcontas.tse.jus.br/divulga/#/candidato/SUDESTE/SP/2045202024/250001946387/2024/71773)).

## 3. Emendas estaduais (lista parcial)

| Ano da emenda | Deputado(a) estadual | Beneficiário | Objeto | Valor (R$) | Situação | Fonte |
|---|---|---|---|---:|---|---|
| 2020 | Dra. Damaris Moura | Santa Casa | custeio | 100.000,00 | paga | [Gov SP 2020 Saúde](https://www.transparencia.sp.gov.br/EmendasImpositivas/2020_Saude_30_01_25.pdf) |
| 2020 | Ricardo Madalena | Santa Casa | custeio | 110.000,00 | paga | idem |
| 2020 | Fernando Cury | Casa da Criança | reforma/ampliação | 100.000,00 | impedida | [Gov SP 2020 exceto saúde](https://www.transparencia.sp.gov.br/EmendasImpositivas/2020_ExcetoSaude_30_01_25.pdf) |
| 2020 | Reinaldo Alguz | Lar São Vicente de Paulo | reforma e ampliação | 200.000,00 | impedida | idem |
| 2020 | Ricardo Madalena | APAE | obras | 100.000,00 | impedida | idem |
| 2021 | Fernando Cury | Casa da Criança | equipamento | 40.000,00 | paga | [Gov SP 2021 exceto saúde](https://www.transparencia.sp.gov.br/EmendasImpositivas/2021_ExcetoSaude_30_01_25.pdf) |
| 2022 | Edson Giriboni | Santa Casa | mesa cirúrgica motorizada | 250.000,00 | paga | [Gov SP 2022 Saúde](https://www.transparencia.sp.gov.br/EmendasImpositivas/2022_Saude_30_01_25.pdf) |
| 2022 | Maria Lúcia Amary | Santa Casa | mobiliário e materiais hospitalares | 200.000,00 | paga | idem |
| 2022 | Frederico d'Avila | Santa Casa | custeio | 195.000,00 | paga | idem |
| 2022 | Wellington Moura | Santa Casa | rede de informática | 150.000,00 | em processamento (jan/2025) | idem |
| 2022 | Conte Lopes | Santa Casa | melhoria do atendimento | 100.000,00 | paga | idem |
| 2022 | Gilmaci Santos | Prefeitura | custeio da saúde | 100.000,00 | paga | idem |
| 2022 | Patrícia Bezerra | Prefeitura | veículo para saúde | 100.000,00 | paga | idem |
| 2022 | Paulo Fiorilo | Prefeitura | equipamentos e mobiliário (educação) | 80.000,00 | em processamento (jan/2025) | [Gov SP 2022 exceto saúde](https://www.transparencia.sp.gov.br/EmendasImpositivas/2022_ExcetoSaude_30_01_25.pdf) |
| 2022 | Fernando Cury | Casa da Criança | reforma/ampliação | 65.000,00 | paga | idem |
| 2023 | Ricardo Madalena | Santa Casa (via Prefeitura) | exames de imagem (SADT) | 150.000,00 | repassada em 2024 | [DO Taquarituba ed. 1123/2024](https://www.taquarituba.sp.gov.br/public/admin/globalarq/diario-eletronico/diario/A2RTxAsZ3ac32wA2.pdf) |
| 2023 | Dani Alonso | Santa Casa (via Prefeitura) | exames de imagem (SADT) | 100.000,00 | repassada em 2024 | idem |
| 2025 | Edson Giriboni | Prefeitura | ambulância | 250.000,00 | indicada na LOA | [ALESP quadro 2025](https://www.al.sp.gov.br/spl/2025/02/Acessorio/1000597524_1000740220_Acessorio.pdf) |
| 2025 | Edson Giriboni | Prefeitura | veículo para saúde | 150.000,00 | indicada | idem |
| 2025 | Edson Giriboni | Prefeitura | infraestrutura urbana | 100.000,00 | indicada | idem |
| 2025 | Agente Federal Danilo Balas | Prefeitura | equipamentos (saúde) | 150.000,00 | indicada | idem |
| 2025 | Major Mecca | Santa Casa | custeio | 150.000,00 | indicada | idem |
| 2025 | Major Mecca | Casa da Criança | custeio | 50.000,00 | indicada | idem |
| 2025 | Conte Lopes | Santa Casa | custeio | 100.000,00 | indicada | idem |
| 2025 | Tomé Abduch | APAE | custeio | 100.000,00 | indicada | idem |

Total da lista: R$ 3,19 mi (cálculo próprio). Não localizados: emendas estaduais de 2024 e 2026 e a maior parte de 2023 (os painéis do Governo SP para 2023 a 2025 são Power BI em https://www.transparencia.sp.gov.br/home/emendasparlamentares e não foram extraídos). O município também tem **emendas impositivas municipais** (de vereadores), como R$ 86.500,00 para a APATA em 2024 ([DO 1123/2024](https://www.taquarituba.sp.gov.br/public/admin/globalarq/diario-eletronico/diario/A2RTxAsZ3ac32wA2.pdf)).

### Deputados estaduais que mais destinaram (na lista parcial)

1. **Edson Giriboni**: R$ 750 mil (2022 e 2025)
2. **Ricardo Madalena**: R$ 360 mil (2020 e 2023)
3. Fernando Cury: R$ 205 mil (2020 a 2022, parte impedida)
4. Conte Lopes, Maria Lúcia Amary, Major Mecca e Reinaldo Alguz (impedida): R$ 200 mil cada
5. Frederico d'Avila: R$ 195 mil

## 4. Ranking combinado (federal pago + estadual listado)

Os maiores apoiadores identificados, juntando as duas esferas, são: Comissão de Saúde da Câmara (R$ 1,20 mi), Simone Marquetto (R$ 1,00 mi), Mauricio Neves (R$ 0,90 mi), Arlindo Chinaglia (R$ 0,86 mi), Samuel Moreira (R$ 0,86 mi), Edson Giriboni (R$ 0,75 mi, estadual) e Paulo Teixeira (R$ 0,71 mi).

**Análise:** emendas são relevantes para a saúde (custeio da Santa Casa e da atenção primária), mas pequenas frente ao orçamento: R$ 3 mi em 2025 contra R$ 181 mi de despesa, menos de 2%. Elas não financiam a agenda estruturante (industrial, turismo, saneamento). E o TCE apontou em 2023 falta de prestação de contas das emendas Pix na plataforma federal ([parecer 2023](https://www.tce.sp.gov.br/jurisprudencia/exibir?proc=4281/989/23&offset=0)).
