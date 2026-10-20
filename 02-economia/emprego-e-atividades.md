# Emprego, atividades econômicas e transferências em Taquarituba (SP)

Dados levantados em 20/10/2026. Legenda: **[oficial]**, **[cálculo]**, **[estimativa]**, **[secundário]** (fonte que reprocessa dado oficial).

## Fontes

- IBGE, Cadastro Central de Empresas (CEMPRE): tabela 1685 (2006 a 2021, série encerrada) e tabela 9509 (2022 a 2024, nova série): https://sidra.ibge.gov.br/tabela/1685 e https://sidra.ibge.gov.br/tabela/9509
- IBGE Censo 2022, ocupados por atividade e posição na ocupação, tabela 10262: https://sidra.ibge.gov.br/tabela/10262
- Caravela (reprocessa RAIS, CAGED, Receita Federal): https://www.caravela.info/municipios/sp/taquarituba-sp (acesso em 20/10/2026)
- MDS, MI Social / VIS Data (Bolsa Família, CadÚnico, BPC): https://aplicacoes.mds.gov.br/sagi/vis/data3/
- Tesouro Nacional, SICONFI, DCA Anexo I-C (receitas da prefeitura): https://siconfi.tesouro.gov.br
- Dados: `dados/cempre_empresas_emprego_salario.csv`, `dados/ocupados_censo2022_atividade_posicao.csv`, `dados/bolsa_familia_cadunico_bpc.csv`, `dados/receitas_taquarituba_2013_2025.csv`, `dados/receitas_municipais_dca.csv`

**O que não consegui:** os painéis e arquivos do Novo CAGED e da RAIS no PDET/MTE (pdet.mte.gov.br) não responderam deste ambiente (timeout). Por isso não há série oficial CAGED ano a ano nem estoque RAIS por setor tirados direto da fonte. Uso o CEMPRE do IBGE (montado a partir da RAIS e de outros registros) como série anual de emprego formal, e o Caravela como fonte secundária para CAGED 2025 e 2026. SEADE (perfil.seade.gov.br) também falhou (erro de certificado). DataViva e Empresômetro não foram consultados com sucesso.

## Emprego formal, série anual (CEMPRE, oficial)

| Ano | Empresas e organizações | Pessoal ocupado total | Assalariados | Salário médio (SM) |
|---|---|---|---|---|
| 2006 | 584 | 3.117 | 2.478 | 2,0 |
| 2007 | 635 | 3.663 | 2.962 | 2,0 |
| 2008 | 706 | 3.795 | 3.034 | 2,2 |
| 2009 | 1.208 | 4.444 | 3.186 | 2,0 |
| 2010 | 1.236 | 4.623 | 3.360 | 1,9 |
| 2011 | 1.232 | 5.125 | 3.847 | 2,0 |
| 2012 | 1.272 | 5.476 | 4.170 | 1,9 |
| 2013 | 1.365 | 5.775 | 4.369 | 2,0 |
| 2014 | 1.337 | 5.585 | 4.233 | 2,0 |
| 2015 | 1.310 | 5.437 | 4.117 | 2,0 |
| 2016 | 1.293 | 5.329 | 4.035 | 1,9 |
| 2017 | 1.326 | 5.440 | 4.092 | 2,0 |
| 2018 | 1.308 | 5.600 | 4.254 | 2,0 |
| 2019 | 1.155 | 5.667 | 4.516 | 2,0 |
| 2020 | 1.219 | 5.683 | 4.427 | 2,0 |
| 2021 | 1.200 | 5.616 | 4.372 | 2,0 |
| 2022* | 2.222 | 7.039 | 4.647 | 2,0 (R$ 2.434,59) |
| 2023* | 2.303 | 7.547 | 5.054 | 2,3 (R$ 2.971,51) |
| 2024* | 2.376 | 7.610 | 5.040 | 2,2 (R$ 3.171,13) |

\* Quebra de série: a partir de 2022 o IBGE usa nova metodologia (tabela 9509). O salto de empresas e de "pessoal ocupado total" em 2022 vem em boa parte da mudança de método, não de crescimento real. A coluna de assalariados é a mais comparável entre as duas séries, mas ainda com cautela. O mesmo vale para 2009, quando o número de empresas quase dobra de um ano para o outro.

Tendência:
- Assalariados dobraram de 2006 a 2024 (2.478 para 5.040). O crescimento foi forte até 2013, parou entre 2014 e 2017 (recessão nacional), voltou devagar até 2019 e retomou em 2023.
- O salário médio ficou travado perto de 2 SM por quase 20 anos. Como o SM teve ganho real no período, isso não quer dizer estagnação em reais, mas indica que a cidade não ganhou posição relativa.
- Em 2024 o salário médio formal foi R$ 3.171,13 (2,2 SM), contra R$ 4.598,40 (3,3 SM) do estado.

Comparação 2024 (CEMPRE, oficial): salário médio em SM: Itaí 2,6; Avaré 2,3; **Taquarituba 2,2**; Coronel Macedo 1,9; Itaporanga 1,8; Fartura 1,7; Taguaí 1,3; estado de SP 3,3. Assalariados: Avaré 24.978; Itaí 4.626; **Taquarituba 5.040**; Taguaí 4.409; Fartura 3.265; Itaporanga 2.113; Coronel Macedo 869.

## CAGED e RAIS recentes [secundário, Caravela]

- Estoque de empregos com carteira: cerca de 6,3 mil; remuneração média R$ 3,2 mil (estado: R$ 4,4 mil). Fonte RAIS, ano não informado na página.
- CAGED janeiro a agosto de 2026: 2.453 admissões, 2.089 desligamentos, **saldo +364**.
- CAGED 2025 (ano inteiro): **saldo +588**.
- Atividades que mais empregam (RAIS): administração pública em geral (974), abate de bovinos (237), segurança e ordem pública (211).
- Saldo por setor no último ano: a página traz "Restaurantes e bares +2.381", número incompatível com uma cidade de 6,3 mil empregos formais. Considero **erro da página** e não uso. Os saldos negativos citados (pescado -46, pecuária -43, aparelhamento de pedras -42) também não foram confirmados em fonte primária.
- MEI ativos: 1.764 (até 06/12/2025, Receita Federal via Caravela).

## Onde a população trabalha (Censo 2022, oficial)

11.240 pessoas ocupadas (14 anos ou mais), por local de moradia, formais e informais.

| Atividade | Taquarituba | Estado de SP |
|---|---|---|
| Comércio e reparação de veículos | 21,0% | 16,7% |
| Agropecuária | 14,4% | 2,7% |
| Indústria de transformação | 14,2% | 12,5% |
| Construção | 8,4% | 7,0% |
| Educação | 5,8% | 6,3% |
| Serviços domésticos | 4,7% | 3,7% |
| Transporte e armazenagem | 3,8% | 6,7% |
| Administração pública | 3,8% | 3,3% |
| Alojamento e alimentação | 3,7% | 4,5% |
| Saúde e serviços sociais | 2,9% | 6,5% |

| Posição na ocupação | Pessoas | % | Estado de SP |
|---|---|---|---|
| Empregado privado com carteira | 4.814 | 42,8% | 48,2% |
| Empregado privado sem carteira | 1.522 | 13,5% | 9,9% |
| Trabalhador doméstico | 450 (391 sem carteira) | 4,0% | 3,3% |
| Setor público (inclui estatutários) | 1.020 | 9,1% | 9,4% |
| Empregador | 765 | 6,8% | 3,5% |
| Conta própria | 2.605 (1.723 sem CNPJ) | 23,2% | 24,3% |

Informalidade [cálculo, critério próximo ao do IBGE: sem carteira, conta própria e empregador sem CNPJ]: cerca de **35%** dos ocupados em Taquarituba, contra cerca de 29% no estado.

Destaque: a proporção de **empregadores (6,8%) é o dobro da do estado**. Combina com cidade de produtores rurais e pequeno comércio.

## Atividade predominante

- **No PIB:** serviços e comércio (65,7% do VA em 2021), com a agropecuária em segundo (15,2%). Ver `pib.md`.
- **No emprego da população:** comércio (21%), agro (14%) e indústria (14%).
- **No emprego formal (RAIS via Caravela):** prefeitura e setor público lideram, seguidos de frigorífico (abate de bovinos).
- **Na exportação:** café (US$ 57,2 milhões em 2025, Comex Stat), feito por empresa comercial registrada no município. Ver `agropecuaria.md`.
- **Maiores empregadores nominais:** não encontrei lista oficial de empresas por número de empregados (a RAIS identificada não é pública). Pela RAIS agregada, o maior empregador é a Prefeitura.

## Dependência de transferências

### Receita da prefeitura, série anual (SICONFI, oficial; receitas brutas)

| Ano | Receitas correntes (R$ mi) | Impostos próprios (R$ mi) | FPM (R$ mi) | Cota ICMS (R$ mi) | % transferências | % impostos próprios | % FPM |
|---|---|---|---|---|---|---|---|
| 2014 | 59,9 | 6,4 | 13,2 | 12,3 | 77,7 | 10,7 | 22,0 |
| 2015 | 62,8 | 5,8 | 14,0 | 13,2 | 77,6 | 9,2 | 22,3 |
| 2016 | 65,3 | 3,6 | 16,2 | 14,1 | 83,2 | 5,6 | 24,8 |
| 2017 | 74,2 | 7,1 | 15,7 | 16,2 | 77,3 | 9,5 | 21,1 |
| 2018 | 80,2 | 9,9 | 16,0 | 17,9 | 79,2 | 12,3 | 19,9 |
| 2019 | 88,1 | 10,7 | 17,4 | 20,0 | 78,9 | 12,1 | 19,7 |
| 2020 | 92,7 | 11,4 | 16,6 | 19,7 | 80,2 | 12,3 | 17,9 |
| 2021 | 113,8 | 12,3 | 22,2 | 25,1 | 82,1 | 10,8 | 19,5 |
| 2022 | 127,8 | 15,2 | 27,6 | 29,5 | 79,8 | 11,9 | 21,6 |
| 2023 | 151,4 | 18,5 | 32,6 | 31,5 | 77,4 | 12,2 | 21,5 |
| 2024 | 168,5 | 19,6 | 40,8 | 36,4 | 78,8 | 11,6 | 24,2 |
| 2025 | 184,6 | 21,8 | 45,4 | 40,3 | 80,6 | 11,8 | 24,6 |

Percentuais sobre a receita corrente bruta [cálculo]. 2013 não veio no padrão da API. Valores de 2016 de impostos e ISS parecem mal classificados na declaração do município (ISS de só R$ 96 mil); usar com cautela.

2025 em detalhe (oficial): receita total R$ 214,2 milhões, sendo R$ 18 milhões de operação de crédito. IPTU R$ 7,7 milhões; ISS R$ 7,3 milhões; ITBI R$ 2,2 milhões; FUNDEB R$ 21,0 milhões; SUS (União) R$ 10,5 milhões; IPVA R$ 9,2 milhões.

Tendência: **cerca de 4 em cada 5 reais da prefeitura vêm de transferências**, e isso não mudou em 12 anos. O FPM ganhou peso desde 2021 (de 18% para 25%). Os impostos próprios ficam presos em 11% a 12%.

Comparação 2025 (SICONFI, oficial, % da receita corrente bruta):

| Município | Transferências | Impostos próprios | FPM |
|---|---|---|---|
| Avaré | 67,6 | 19,6 | 16,3 |
| Itaí | 72,3 | 14,9 | 19,7 |
| **Taquarituba** | **80,6** | **11,8** | **24,6** |
| Coronel Macedo | 82,2 | 9,5 | 33,5 |
| Fartura | 84,8 | 10,5 | 31,3 |
| Taguaí | 87,4 | 9,5 | 36,1 |
| Itaporanga | 89,2 | 8,0 | 35,6 |

Algumas declarações de anos antigos de vizinhos têm o FPM em conta diferente (ex.: Avaré 2015, Coronel Macedo 2020); ver `dados/receitas_municipais_dca.csv`.

### Bolsa Família, CadÚnico e BPC, série anual (MDS, oficial; mês de dezembro)

| Ano | Famílias no PBF | Valor do mês (R$) | Benefício médio (R$) | Famílias no CadÚnico | Beneficiários BPC | Valor BPC do mês (R$) |
|---|---|---|---|---|---|---|
| 2004 | 1.193 | 66.558 | 55,79 | sem dado | 224 | 58.462 |
| 2006 | 1.804 | 88.893 | 49,28 | sem dado | 336 | 118.047 |
| 2008 | 1.570 | 95.964 | 61,12 | sem dado | 492 | 204.056 |
| 2010 | 1.309 | 99.245 | 75,82 | sem dado | 592 | 301.920 |
| 2012 | 1.352 | 154.654 | 114,39 | 3.524 | 636 | 395.219 |
| 2014 | 1.069 | 139.074 | 130,10 | 3.752 | 670 | 481.484 |
| 2016 | 1.007 | 138.218 | 137,26 | 3.027 | 743 | 650.660 |
| 2018 | 946 | 145.452 | 153,75 | 2.840 | 792 | 754.977 |
| 2019 | 888 | 137.311 | 154,63 | 2.910 | 801 | 800.396 |
| 2020 | 991 | 28.228 (Auxílio Emergencial no lugar) | 28,48 | 2.832 | 827 | 868.396 |
| 2021 | Auxílio Brasil: cerca de 1.019 [cálculo] | 201.092 | 197,34 | 3.085 | 816 | 899.800 |
| 2022 | Auxílio Brasil: cerca de 1.471 [cálculo] | 890.145 | 605,13 | 3.789 | 860 | 1.042.357 |
| 2023 | 1.444 | 942.470 | 658,61 | 3.926 | 954 | 1.260.641 |
| 2024 | 1.381 | 877.214 | 639,37 | 3.660 | 1.099 | 1.551.855 |
| 2025 | 1.162 | 742.815 | 648,75 | 3.538 | 1.068 | 1.625.846 |
| jun/2026 | 1.174 (3.045 pessoas) | 750.965 | 640,21 | 3.568 | 1.061 | 1.719.942 |

Série completa (todos os anos) em `dados/bolsa_familia_cadunico_bpc.csv`. Famílias do Auxílio Brasil = valor pago dividido pelo benefício médio (MI Social não traz a contagem direta nesses meses).

Tendência: o número de famílias no programa caiu de 1.800 (2006) para menos de 900 (2019), subiu de novo com o Auxílio Brasil e o novo Bolsa Família (pico de 1.444 em 2023) e voltou a cair em 2025 e 2026 (cerca de 1.170). O valor por família subiu muito a partir de 2022. O BPC (idosos e pessoas com deficiência) cresce sem parar e hoje paga mais que o dobro do Bolsa Família.

### Peso das transferências na economia [estimativa]

Anualizando o mês de junho de 2026 (vezes 12):
- Bolsa Família: cerca de R$ 9,0 milhões por ano, uns 0,7% do PIB de 2023 (R$ 1,279 bilhão).
- BPC: cerca de R$ 20,6 milhões por ano, uns 1,6% do PIB.
- FPM 2025: R$ 45,4 milhões (oficial), uns 3,5% do PIB.

Leitura: a **prefeitura** é muito dependente de transferência (80%), como quase toda cidade pequena. A **economia** da cidade não é: Bolsa Família e BPC juntos somam pouco mais de 2% do PIB, e só 19,7% da renda das famílias vem de fontes que não são trabalho (Censo 2022), abaixo dos vizinhos menores.
