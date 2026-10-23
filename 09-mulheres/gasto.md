# Quanto Taquarituba gasta com políticas para mulheres

Data de referência: 23/10/2026. Marcações: **[fato]**, **[cálculo]**, **[estimativa]**, **[análise]**.

Dados em `dados/gasto_politicas_mulheres_2021_2025.csv` e `dados/tce_2026_empenhos_amvapa.csv`.

---

## 1. Como medi

- **Fonte 2021 a 2025**: TCE-SP, conjunto de dados de despesas por ano (https://transparencia.tce.sp.gov.br/conjunto-de-dados, arquivos `despesas-<ano>.zip`, filtrados para Taquarituba em fluxo, baixados em 23/10/2026). Cada linha traz função, programa, ação, elemento e o histórico do empenho.
- **O orçamento não tem programa nem ação para mulheres.** Os programas de Assistência Social são genéricos ("Manutenção e desenvolvimento das atividades do Fundo Municipal de Assistência Social", "da Ação Social", "do Fundo da Criança e do Adolescente") **[fato]**. Por isso classifiquei empenho por empenho, lendo o histórico, em oito categorias (palavras-chave: SAI MULHERES, MARIA DA PENHA, AGOSTO LILÁS, VIOLÊNCIA CONTRA A MULHER, REDE MULHER, DIA DA MULHER, DIA DAS MÃES, OUTUBRO ROSA, GESTANTE). Empenhos de gêneros alimentícios que só citam "gestante" de passagem foram excluídos **[cálculo]**.
- **O que fica de fora**: salários de assistentes sociais e psicólogas do CRAS e CREAS, dos guardas da Patrulha e da equipe de saúde; exames e consultas de rotina para mulheres. O número abaixo é o gasto **específico e identificável**, não o custo total do atendimento.
- **2026**: o arquivo em massa de 2026 ainda não existe no TCE-SP (despesas-2026.zip retornou 404 em 23/10/2026). A API mensal (https://transparencia.tce.sp.gov.br/api/json/despesas/taquarituba/2026/<mes>) tem jan a ago, mas só fornecedor, valor e data, sem função nem histórico **[fato]**.

---

## 2. Série 2021 a 2025 (empenhado líquido, R$ correntes)

| Categoria | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| SAI Mulheres: rateio ao consórcio AMVAPA | | | | | 129.664 |
| SAI Mulheres: aluguel e contas do imóvel | | | | | 23.626 |
| Campanhas contra violência (Agosto Lilás, 10 de outubro, fórum) | 3.416 | | 10.943 | 4.657 | 9.184 |
| Rede Mulher (CREAS) | | 1.706 | 1.119 | 9.779 | 6.175 |
| Dia da Mulher e Dia das Mães (CRAS, proteção especial) | | | 580 | 2.330 | 3.165 |
| Patrulha Maria da Penha (braçais; empenho anulado) | | | | | 0 |
| Outubro Rosa (dividido com Novembro Azul) | 9.658 | 8.358 | 8.817 | 14.852 | 16.029 |
| Gestantes (kits, cartão, repelente) | | | 21.360 | 5.790 | 120 |
| **Total** | **13.074** | **10.065** | **42.819** | **37.408** | **187.963** |

**[cálculo sobre TCE-SP]** Valores pagos são praticamente iguais (2025: R$ 185.463 pagos).

Leituras **[cálculo]**:
- O gasto específico com mulheres saltou de cerca de R$ 40 mil por ano (2023 e 2024) para **R$ 188 mil em 2025**, por causa do SAI Mulheres (R$ 153 mil, 82% do total).
- Sem o SAI, a política de 2025 custou R$ 34,7 mil: campanhas, brindes, lanches de encerramento de grupos e material de Outubro Rosa.
- R$ 188 mil equivalem a **0,12%** da despesa empenhada da Prefeitura em 2025 (R$ 162,2 milhões) e a cerca de **R$ 16 por mulher residente** por ano (11.747 mulheres, Censo 2022).
- Na Assistência Social, os R$ 171,8 mil específicos para mulheres são **1,55%** da função (R$ 11,09 milhões empenhados em 2025).

### 2.1 Detalhe do SAI Mulheres em 2025 [fato, TCE-SP 2025]

- **Aluguel**: empenho de março de 2025 por inexigibilidade (licitação 17/2025), parcela de **R$ 4.554 por mês**; 5 parcelas pagas (R$ 22.770): 1 com recurso próprio e 4 com recurso estadual vinculado. Água e luz do imóvel: R$ 684 pagos (recurso estadual). Endereço e locador omitidos por sigilo do serviço.
- **Contrato de rateio 1044/2025 com a AMVAPA**, empenhos de 18/06/2025, todos pagos ao longo de 2025:
  - R$ 61.560 para equipamentos e material permanente, recurso estadual, parcela única;
  - R$ 48.103,50 de custeio mensal com recurso estadual (parcelas de cerca de R$ 6.012);
  - R$ 15.000 pagos de custeio mensal com recurso próprio (R$ 2.500 por mês, 6 parcelas; empenho de R$ 17.500);
  - R$ 2.500 de equipamentos com recurso próprio.
- Somando: cerca de **R$ 128,6 mil de recurso estadual** e **R$ 22,1 mil de recurso próprio** pagos em 2025 **[cálculo]**.

---

## 3. 2026 (jan a ago)

### 3.1 Consórcio AMVAPA [fato, API TCE-SP]

| Empenho | Data | Empenhado | Pago até ago | Parcela mensal |
|---|---|---|---|---|
| 2008-2026 | 26/02 | 555.180,00 | 370.120,00 | 46.265,00 |
| 2009-2026 | 26/02 | 76.980,00 | 51.320,00 | 6.415,00 |
| 2010-2026 | 26/02 | 48.913,20 | 32.608,80 | 4.076,10 |
| 2011-2026 | 26/02 | 11.025,72 | 7.350,48 | 918,81 |
| 1749-2026 | 13/02 | 12.600,00 | 12.600,00 | |
| 4141-2026 | 22/04 | 4.500,00 | 4.500,00 | |
| 6115-2026 | 19/06 | 15.300,00 | 3.060,00 | 1.530,00 |
| 7242-2026 | 21/07 | 7.000,00 | 0,00 | |

**[estimativa]** A API não diz qual empenho é o SAI. Comparando com 2025:
- 2008 (R$ 555 mil) tem o tamanho do rateio do SAMU (R$ 528,9 mil em 2025).
- 2011 (R$ 11,0 mil) tem o tamanho dos kits tapa-buraco (R$ 10,1 mil em 2025).
- **2009 (R$ 76.980 = 12 × R$ 6.415)** tem o perfil da parcela estadual mensal do SAI em 2025 (R$ 6.012), reajustada em 6,7%. É o candidato mais provável.
- A parcela de recurso próprio (R$ 2.500 por mês em 2025) pode estar em 2010 ou 6115, ou ter sido absorvida.

Faixa estimada do gasto municipal com o SAI Mulheres em 2026: **R$ 77 mil a R$ 110 mil** (só a parcela 2009, ou ela mais R$ 2.500 a R$ 2.750 por mês de recurso próprio) **[estimativa, confiança baixa; confirmar por LAI]**. Pago até agosto: cerca de R$ 51 mil a R$ 72 mil **[estimativa]**.

Do lado da receita, o Estado anunciou R$ 130 mil adicionais a Taquarituba por sediar o serviço, além de R$ 659,2 mil de cofinanciamento regional de implantação (Agência SP, 06/02/2026) **[fato]**. Não verifiquei o ingresso desses valores na receita municipal.

### 3.2 Outras despesas de 2026

Sem histórico na API, não dá para identificar Agosto Lilás, Rede Mulher, Patrulha ou kits de gestantes de 2026 **[lacuna]**. Fatos indiretos: 65 kits às gestantes em setembro de 2026 (notícia 2673) e campanha de Outubro Rosa em curso (notícia 2666).

**[estimativa]** Mantido o padrão de 2025 sem o SAI (R$ 35 mil) e somada a faixa do SAI, o gasto específico de 2026 ficaria entre **R$ 110 mil e R$ 150 mil**. Confiança baixa.

---

## 4. Orçamento, plano e emendas

- **LOA 2026** (Lei 1.998/2025): Assistência Social com R$ 11.483.832,90 (5,97% do orçamento); Segurança Pública R$ 4.020.500 (`05-financas-publicas/dados/loa_2026_por_funcao.csv`) **[fato]**. Não há programa ou ação nomeada para mulheres no quadro por função; o detalhamento por ação não foi verificado.
- **PPA 2026-2029** (Lei 1.996/2025): não consegui reler o anexo de programas; o portal da Prefeitura estava fora do ar (conexão recusada) a partir das 14h de 23/10/2026 **[lacuna]**.
- **Fundo Municipal dos Direitos da Mulher** (LC 377/2025): nenhum empenho identificável em 2025; em 2026 a API não permite saber **[lacuna]**.
- **Emendas parlamentares**: nas bases do repositório (`05-financas-publicas/dados/emendas_federais_cgu_por_favorecido.csv` e `emendas_estaduais_sp_taquarituba.csv`) não há emenda com objeto ligado a mulheres. Há três emendas federais de 2026 ao Fundo Municipal de Assistência Social para "estruturação da rede de serviços do SUAS", sem destinação específica **[fato]**.

---

## 5. Leitura (análise)

1. **O dinheiro novo é estadual e regional.** O salto de 2025 é o abrigo, pago em grande parte com recurso estadual e operado por consórcio e OSC. O esforço fiscal próprio do município com mulheres continua na casa de dezenas de milhares de reais por ano. **[análise]**
2. **Gasto de campanha, não de serviço.** Fora o SAI, o que se identifica são camisetas, folders, canecas, mudas e lanches. Isso informa, mas não atende. O atendimento real (CREAS, GCM, saúde) é pago com folha que não aparece separada. **[análise]**
3. **Transparência insuficiente.** Sem ação orçamentária própria, é impossível acompanhar pela execução quanto custa a Guardiã Maria da Penha ou o conselho. Criar uma ação "Políticas para as Mulheres" na LOA 2027 resolveria isso. **[análise]**
