# Contratações da Prefeitura no PNCP (2024 a 2026) e inconsistências encontradas

Fonte: Portal Nacional de Contratações Públicas (PNCP), API de consulta (https://pncp.gov.br/api/consulta), CNPJ 46.634.218/0001-07, consultada em 20/11/2026. Download feito por [`scripts/pncp_contratos.py`](../scripts/pncp_contratos.py) e alertas por [`scripts/pncp_inconsistencias.py`](../scripts/pncp_inconsistencias.py). Só a Prefeitura (a Câmara tem CNPJ próprio). Valores em R$ correntes.

Marcação: **[Fato]** dado do PNCP ou de cadastro oficial; **[Cálculo]** conta própria; **[Análise]** interpretação. Um alerta não prova irregularidade: é um ponto para conferir no processo ou pedir pela Lei de Acesso à Informação.

## 1. O que existe no PNCP

| Arquivo em `dados/` | Linhas | Conteúdo |
|---|---|---|
| `pncp_contratacoes_2024_2026.csv` | 396 | um processo de compra por linha, todas as modalidades |
| `pncp_contratos_2024_2026.csv` | 283 | contratos publicados |
| `pncp_atas_2024_2026.csv` | 94 | atas de registro de preços |
| `pncp_termos_aditivos_2024_2026.csv` | 10 | termos aditivos |
| `pncp_inconsistencias_2024_2026.csv` | 124 | alertas, um por linha, com link |
| `tce_2025_fornecedora_cnpj_33671633.csv` | 18 | empenhos, liquidações e pagamentos de 2025 à fornecedora do item 2.1 (TCE-SP) |

**[Fato] Processos publicados por modalidade e ano**

| Modalidade | 2024 | 2025 | 2026 (até 19/11) |
|---|---|---|---|
| Pregão eletrônico | 57 | 76 | 60 |
| Concorrência eletrônica | 5 | 13 | 12 |
| Dispensa | 19 | 44 | 44 |
| Inexigibilidade | 4 | 26 | 29 |
| Outros (leilão, credenciamento, pregão presencial) | 1 | 5 | 0 |
| **Total** | **86** | **164** | **145** |

**[Fato] Valor dos contratos publicados, por ano de assinatura (R$ milhões)**

| Modalidade de origem | 2024 | 2025 | 2026 |
|---|---|---|---|
| Concorrência | 2,01 | 4,34 | 13,01 |
| Pregão | 2,40 | 7,33 | 5,51 |
| Dispensa | 0,42 | 1,37 | 6,60 |
| Inexigibilidade | 0,11 | 3,34 | 3,84 |
| **Total** | **4,94** | **16,38** | **28,96** |

**[Análise]** O PNCP pega só parte do gasto. Em 2025 a Prefeitura empenhou R$ 6,5 mi por inexigibilidade e R$ 6,9 mi por dispensa (TCE, ver [compras-sem-licitacao-e-precatorios.md](compras-sem-licitacao-e-precatorios.md)); no PNCP aparecem R$ 3,3 mi e R$ 1,4 mi em contratos. Parte da diferença são contas de luz e água, que não geram contrato, e compras de registro de preços, que geram ata e empenho, não contrato. Em 2024 a cobertura é ainda menor (63 contratos). O total de 2024 inclui R$ 1,43 mi do Bradesco pela folha de pagamento, que é **receita** da Prefeitura, não gasto.

**[Fato] Maiores contratados (2024 a 2026, soma dos contratos publicados, R$ 50,4 mi no total, 231 fornecedores)**

| Fornecedor | Contratos | R$ mi | Origem |
|---|---|---|---|
| Vértice Construtora e Energia Solar | 1 | 5,03 | concorrência, usinas fotovoltaicas (2026) |
| Fundação CETREDE (Fortaleza/CE) | 1 | 4,34 | **dispensa** (art. 75, XV), geotecnologia, cadastro e Planta de Valores (2026) |
| Berseba (antes Seba) Estruturas Metálicas | 2 | 3,73 | concorrência, reforma da Praça São Roque e Farmácia |
| BMA Empreendimentos (antes BMA Negócios) | 7 | 3,69 | 4 concorrências e 3 dispensas |
| Prime Consultoria | 1 | 3,49 | pregão, cartão de abastecimento da frota |
| Marcos Humberto Gobbo de Oliveira | 8 | 1,30 | 7 concorrências e 1 dispensa |

## 2. Inconsistências e alertas

### 2.1 Fracionamento e sobrepreço na decoração de Natal de 2025
- **[Fato]** Três dispensas pelo art. 75, II para decoração natalina em 2025: [114/2025](https://pncp.gov.br/app/editais/46634218000107/2025/114) (cordões de LED, com aviso público e disputa de 01 a 08/09/2025, vencida pela Bazar Distribuidora por R$ 23.000), [157/2025](https://pncp.gov.br/app/editais/46634218000107/2025/157) (R$ 60.375) e [158/2025](https://pncp.gov.br/app/editais/46634218000107/2025/158) (R$ 59.155). As duas últimas foram para a mesma fornecedora, Celia Gobbo da Silva (CNPJ 33.671.633/0001-80), ratificadas em 18 e 24/11/2025, a 96% e 94% do limite.
- **[Cálculo]** As três somam R$ 142.530, mais que o dobro do limite anual de dispensa por valor em 2025 (R$ 62.725,59, Decreto 12.343/2024). O art. 75, § 1º manda somar no exercício as despesas do mesmo ramo. Houve ainda o pregão de registro de preços de decoração natalina ([129/2025](https://pncp.gov.br/app/editais/46634218000107/2025/129), teto de R$ 801 mil).
- **[Fato] O mesmo produto, 2,6 vezes mais caro.** Em setembro a Bazar vendeu 250 "cordões luminosos com 50 metros, 500 luminárias LED (400 branco quente e 100 strobo branco frio), IP44, 9 W" a **R$ 92,00** cada ([termo de ratificação da dispensa 036/2025](https://pncp.gov.br/pncp-api/v1/orgaos/46634218000107/compras/2025/114/arquivos/2)). Em novembro o contrato com Celia Gobbo da Silva comprou mais 250 unidades com a **mesma especificação, palavra por palavra** (só o cabo muda de 1,88 para 1,8 mm), a **R$ 241,50** cada ([contrato 0125/25](https://pncp.gov.br/pncp-api/v1/orgaos/46634218000107/contratos/2025/83/arquivos/1)).
- **[Cálculo]** Ao preço de setembro, os 250 cordões de novembro custariam R$ 23.000. A diferença é de **R$ 37.375**.
- **[Fato] Sem disputa publicada.** A dispensa de setembro teve aviso de contratação direta no PNCP e cita o § 3º do art. 75 (disputa eletrônica). As de novembro só têm o termo de ratificação: o processo foi ao PNCP depois de ratificado, sem aviso nem prazo para propostas, embora os contratos digam que o "Aviso de Contratação Direta" os vincula.
- **[Fato] Pago no mesmo dia.** Pela base de despesas do TCE-SP, os R$ 60.375 dos cordões foram **empenhados, liquidados e pagos em 19/11/2025**, o dia seguinte à ratificação. Liquidar significa atestar que os 250 cordões foram entregues e conferidos. O segundo contrato (uma árvore de Natal em estrutura de aço, R$ 29.375, e um túnel de LED de 10 m, R$ 29.780) foi empenhado em 25/11 e pago em 28/11/2025. Os dois contratos dizem que o pagamento vem depois do termo de recebimento, em até 30 dias.
- **[Fato] Fornecedora.** Empresária individual optante pelo **MEI** desde 21/05/2019, em Taquarituba, capital de R$ 6.750, atividade principal "comércio varejista de outros produtos" e 12 secundárias (material elétrico, paisagismo, aluguel de móveis e de palcos, organização de festas, instalação elétrica, brinquedos e outras) (Receita Federal via BrasilAPI, 20/11/2026). Na base do TCE-SP, de 2019 a 2024 ela não recebeu nada de nenhum órgão municipal paulista. Em 2025 recebeu **R$ 138.460** da Prefeitura de Taquarituba, todos por dispensa: piso de tacos da base da Guarda (R$ 9.150, jan), jardim da Segurança Pública (R$ 7.320, fev), decoração do Feirão do Emprego (R$ 1.500, abr), mesas e cadeiras para formação de professores (R$ 960, mai) e os dois contratos de Natal (R$ 119.530, nov). As quatro primeiras não estão no PNCP. Extrato em [dados/tce_2025_fornecedora_cnpj_33671633.csv](dados/tce_2025_fornecedora_cnpj_33671633.csv).
- **[Cálculo]** O teto de faturamento do MEI é R$ 81 mil por ano. Só a Prefeitura pagou 1,7 vez isso em 2025. Passar do teto obriga a sair do MEI; não torna o contrato nulo, mas mostra que a empresa não tinha porte declarado para esse volume.
- **[Fato]** Fiscal dos dois contratos: Gabriel Aparecido Almeida Rodrigues; gestora: Francine Medina Leite Miano. O pedido é do Fundo Social de Solidariedade.
- **[A verificar]** A gestora tem o sobrenome Miano, o mesmo do prefeito (Éder Miano Pereira), e o Fundo Social de Solidariedade costuma ser presidido pela primeira-dama. **Não confirmei parentesco nem o cargo dela.** Se for parente do prefeito, vale perguntar quem fez a pesquisa de preços e quem atestou o recebimento dos cordões no mesmo dia da compra.
- **[Análise]** Juntos, os fatos formam o padrão que os tribunais de contas descrevem como fracionamento com direcionamento: objeto repartido logo abaixo do teto, mesma fornecedora, nenhuma disputa, preço muito acima de uma compra igual feita semanas antes e pagamento sem o prazo normal de recebimento. Nada disso prova dolo; pode haver explicação (urgência, cordões diferentes na prática, erro de registro). Pedir: os processos 184 e 185/2025 completos, com a pesquisa de preços e a justificativa de não usar a cotação de setembro; o termo de recebimento e as notas fiscais; e onde os 500 cordões foram instalados. Pedir também o ato de nomeação da gestora do contrato e a composição do Fundo Social de Solidariedade.

### 2.2 Show contratado depois do evento e datas da FACITA 2026
- **[Fato]** O show de Luan Pereira "na FACITA 2026, no dia 14 de novembro de 2026" (R$ 180 mil, inexigibilidade) foi publicado no PNCP em **17/11/2026**, três dias depois da data do show, e não tem contrato publicado ([153/2026](https://pncp.gov.br/app/editais/46634218000107/2026/153)).
- **[Fato]** A própria Prefeitura informa no PNCP que a 31ª FACITA foi de **5 a 8 de novembro** de 2026 (dispensa da ambulância UTI, [142/2026](https://pncp.gov.br/app/editais/46634218000107/2026/142)). O dia 14/11 fica fora dessas datas.
- **[Análise]** Ou a data do objeto está errada, ou houve show fora da feira, ou a contratação foi formalizada depois do serviço prestado (contratação verbal, vedada pelo art. 95, § 2º, da Lei 14.133, salvo pequenas compras de pronto pagamento). Vale pedir a nota de empenho, a data do empenho e a nota fiscal.

### 2.3 FACITA 2026 sem estrutura contratada no PNCP
- **[Fato]** Para a FACITA 2026 há R$ 2,685 mi em cinco shows por inexigibilidade (Simone Mendes R$ 950 mil, Zezé Di Camargo & Luciano R$ 770 mil, Murilo Huff R$ 705 mil, Luan Pereira R$ 180 mil, Mateus & Cristiano R$ 80 mil) e mais R$ 30 mil do baile da rainha.
- **[Fato]** Não há no PNCP nenhum contrato de 2026 para palco, som, camarote, segurança ou organização da feira. O registro de preços de estrutura de eventos de R$ 52,35 mi ([1/2026](https://pncp.gov.br/app/editais/46634218000107/2026/1)) segue sem ata, sem valor homologado e sem contrato dez meses depois.
- **[Análise]** Em 2025 a estrutura veio de um pregão próprio (Organização Estrela Som, R$ 835,6 mil). Em 2026, ou a estrutura foi contratada fora do PNCP, ou foi bancada por terceiros (com que contrapartida?), ou a ata do registro de preços existe e não foi publicada.

### 2.4 Dispensas acima do limite do inciso declarado
| Processo | Inciso declarado | Limite no ano | Valor | Objeto |
|---|---|---|---|---|
| [51/2024](https://pncp.gov.br/app/editais/46634218000107/2024/51) | art. 75, II | R$ 59.906,02 | R$ 86.993,33 | troca de postes (repete o [32/2024](https://pncp.gov.br/app/editais/46634218000107/2024/32), R$ 85.085) |
| [121/2025](https://pncp.gov.br/app/editais/46634218000107/2025/121) | art. 75, II | R$ 62.725,59 | R$ 90.770,00 | plano de carreira do magistério, por instituição sem fins lucrativos |
| [19/2026](https://pncp.gov.br/app/editais/46634218000107/2026/19) | art. 75, II | R$ 65.492,11 | R$ 80.447,64 | cerca de 692 m no Loteamento Taquarituba H (BMA Empreendimentos) |

**[Análise]** Os casos de postes e cerca cabem no inciso I (obras e serviços de engenharia, limite de R$ 119,8 mil a R$ 131 mil), então pode ser só enquadramento errado no PNCP. O do plano de carreira não é engenharia: ou tem outro fundamento (inciso XV?), ou passou do teto.

### 2.5 Processos excluídos do PNCP
- **[Fato]** Há 36 buracos na numeração dos processos: 6 em 2024, 20 em 2025 e 10 em 2026. A API responde a todos com "a contratação informada foi excluída" (HTTP 410). Lista completa no CSV de alertas.
- **[Análise]** Excluir é permitido para corrigir erro de cadastro, mas 36 exclusões em 432 números (8%) é muito. Processo cancelado deveria aparecer como revogado ou anulado, não sumir. Pedir à Prefeitura a lista dos processos 2024/8, 44, 54, 67, 73, 81; 2025/1, 14, 17, 28, 29, 39, 44, 47, 64, 65, 68, 87, 100, 102, 103, 113, 126, 180, 182, 183; 2026/20, 29, 32, 67, 79, 81, 107, 108, 111, 114, com objeto e motivo da exclusão.

### 2.6 Limpeza: emergencial sem contrato e licitações sem resultado
- **[Fato]** A dispensa emergencial de limpeza escolar e urbana ([110/2025](https://pncp.gov.br/app/editais/46634218000107/2025/110), art. 75, VIII) foi homologada em R$ 1.499.232 e **não tem contrato publicado**. No TCE ela aparece como dispensa 141/2025 da J.S.L. Comércio e Serviços, com R$ 1,16 mi empenhados em 2025.
- **[Fato]** Licitações grandes publicadas há mais de quatro meses sem resultado, contrato ou ata: preparo de merenda escolar com mão de obra (R$ 4,87 mi, [55/2025](https://pncp.gov.br/app/editais/46634218000107/2025/55)) e fórmulas infantis (R$ 1,52 mi, [90/2025](https://pncp.gov.br/app/editais/46634218000107/2025/90)). A varredeira mecanizada ([9/2026](https://pncp.gov.br/app/editais/46634218000107/2026/9), R$ 1,81 mi) ficou sem resultado e foi refeita no [47/2026](https://pncp.gov.br/app/editais/46634218000107/2026/47) (M Locação, R$ 1,457 mi), mas o primeiro segue "divulgado" em vez de fracassado ou revogado.
- **[Fato]** Outros 14 registros de preços seguem sem ata publicada, incluindo pavimentação em microrrevestimento (R$ 10,1 mi, [90/2024](https://pncp.gov.br/app/editais/46634218000107/2024/90)), pintura de prédios (R$ 4,8 mi), uniformes escolares (R$ 3,5 mi) e alimentos estocáveis para merenda (R$ 3,6 mi).
- **[Análise]** Contratação emergencial pode durar no máximo um ano e não pode ser renovada (art. 75, VIII). A pergunta é se a licitação definitiva de limpeza já foi feita.

### 2.7 Publicação fora do prazo e contrato antes do processo
- **[Fato]** 22 contratos foram publicados depois do prazo do art. 94 (10 dias úteis em contratação direta, 20 em licitação), condição para o contrato ter eficácia. Os maiores atrasos: publicidade legal da Phabrica Produções (assinado 06/11/2025, publicado 13/11/2026), dois contratos de dispensa assinados em janeiro e fevereiro de 2026 e publicados em julho, B2B Instituição de Pagamentos (R$ 120 mil, 80 dias úteis) e Vértice (R$ 5,03 mi, 42 dias úteis).
- **[Fato]** Em 23 contratos o processo só foi ao PNCP mais de uma semana depois da assinatura. Exemplo: Zezé Di Camargo & Luciano (R$ 770 mil) assinado em 04/09/2026, processo publicado em 22/09/2026.

### 2.8 Fornecedores que trocaram de nome e concentração em obras
- **[Fato]** Quatro CNPJs aparecem com dois nomes: BMA Negócios → BMA Empreendimentos; Seba → Berseba Estruturas Metálicas; Gopel Distribuidora → Máxima Global; e Marcos Humberto Gobbo de Oliveira, com e sem o número do CNPJ no nome (formato típico de empresário individual).
- **[Fato]** A BMA (Itaberá, aberta em 2023, porte "microempresa" na Receita) tem 7 contratos e R$ 3,69 mi entre set/2025 e mar/2026: reforma do Paço (R$ 1,25 mi), UBS do Novo PAC (R$ 1,66 mi), duas praças, a cerca do item 2.4, a retirada de uma cobertura derrubada por vendaval e uma emergencial de calhas na rodoviária (as três últimas por dispensa). Três requerimentos da Câmara em 2026 pediram os contratos e aditivos da empresa ([03-bairros/dados/camara_proposicoes_2020_2026.csv](../03-bairros/dados/camara_proposicoes_2020_2026.csv)).
- **[Fato]** Marcos Humberto Gobbo de Oliveira (Piraju, atividade principal "pintura de edifícios", microempresa) tem 8 contratos e R$ 1,30 mi, sete deles obras por concorrência. Um aditivo na garagem da Agricultura somou **41%** ao valor inicial (R$ 34.660 sobre R$ 84.000), dentro do teto de 50% para reforma, mas acima dos 25% gerais.
- **[Análise]** Microempresa tem faturamento de até R$ 360 mil por ano. Se as duas usaram preferência da Lei Complementar 123 (desempate, cota) com contratos acima disso, o benefício pode ter sido indevido. Conferir nas atas das sessões.

### 2.9 Erros de cadastro menores
- Organização Estrela Som (FACITA 2025): homologado R$ 835.566,67, contrato R$ 835.556,67 (R$ 10 a menos).
- Três contratos com vigência de zero dias (início = fim).
- Pregão de fórmulas infantis (90/2025) descrito como "registro de preços" no objeto, mas com o campo de registro de preços marcado como "não" no PNCP.
- 72 processos fora de registro de preços com mais de três meses e sem valor homologado preenchido, mesmo quando há contrato.

## 3. Perguntas para pedido de LAI

1. Processos completos das dispensas 157 e 158/2025 (processos 184 e 185/2025), com pesquisa de preços, termo de recebimento, notas fiscais e local de instalação dos cordões; justificativa do preço 2,6 vezes maior que o da dispensa 036/2025; ato de nomeação da gestora dos contratos e composição do Fundo Social de Solidariedade.
2. Empenho, nota fiscal e data real do show de Luan Pereira (inexigibilidade 153/2026).
3. Contratos de estrutura, palco, som e segurança da FACITA 2026 e a ata do registro de preços 1/2026, se houver.
4. Lista dos 36 processos excluídos do PNCP, com objeto e motivo.
5. Contrato da dispensa emergencial de limpeza (110/2025) e situação da licitação definitiva.
6. Resultado dos pregões de merenda terceirizada (55/2025) e fórmulas infantis (90/2025).
7. Fundamento legal correto das dispensas 51/2024, 121/2025 e 19/2026.
