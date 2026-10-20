# O que fez Cultura e Urbanismo saltarem (2019 a 2025)

Abertura empenho por empenho da base de despesas do TCE-SP (https://transparencia.tce.sp.gov.br/conjunto-de-dados), que traz função, ação, natureza (elemento), fonte do recurso, fornecedor, modalidade e histórico de cada despesa. Valores em **R$ mil correntes**, despesa empenhada líquida de anulações, só Prefeitura. Os totais batem com o Siconfi, com diferença de 1% a 3%. Script: [`scripts/tce_areas.py`](../scripts/tce_areas.py). Dados: [`dados/tce_urbanismo_cultura_2019_2025.csv`](dados/tce_urbanismo_cultura_2019_2025.csv) e [`dados/tce_fornecedores_urbanismo_cultura_2019_2025.csv`](dados/tce_fornecedores_urbanismo_cultura_2019_2025.csv). Para valores acima da inflação, ver [gasto-real-por-area.md](gasto-real-por-area.md).

**Cuidado com "reempenho":** obra que atravessa o ano pode ser cancelada e empenhada de novo no ano seguinte. Somar vários anos do mesmo contrato pode contar a mesma obra duas vezes. Os totais por ano estão certos; os totais por contrato são aproximados.

---

## 1. Cultura: de R$ 0,8 mi para R$ 3,0 mi

| Grupo de despesa | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| Pessoal | 344 | 352 | 384 | 406 | 365 | 428 | 490 |
| Festividades e homenagens (shows, eventos) | 0 | 0 | 0 | 13 | 142 | 0 | **1.931** |
| Outro custeio (locações, serviços, editais) | 411 | 286 | 362 | 939 | 1.319 | 1.027 | 484 |
| Energia elétrica | 74 | 46 | 79 | 70 | 57 | 90 | 106 |
| Equipamentos e outros | 3 | 4 | 8 | 74 | 2 | 7 | 20 |
| **Total** | **832** | **688** | **833** | **1.502** | **1.885** | **1.552** | **3.031** |

O que aconteceu em cada fase:
- **2019 a 2021, a cultura mínima.** Basicamente a folha da coordenadoria e o custeio dos prédios.
- **2022 e 2023, a volta dos eventos depois da pandemia.** Shows contratados sem licitação (inexigibilidade): Agromusic R$ 125 mil, BMW Produções R$ 75 mil e Outro Lugar R$ 70 mil em 2022; Live Talentos R$ 110 mil, Easy Produções R$ 85 mil, BV Music R$ 75 mil e Rosa de Saron R$ 56 mil em 2023. Somam-se locação de palco, som e estrutura (Marcella Silva Andrade Eventos e SEA Locações).
- **2024, os editais.** Aparecem pagamentos a pessoas físicas "contempladas no edital" a pedido da coordenadoria de cultura (exemplo: R$ 123 mil e R$ 60 mil a dois contemplados), que coincidem com a Lei Paulo Gustavo e a PNAB. Também a reforma de fachada (Fuca, R$ 129 mil) e o aluguel de imóvel no centro (Rua Marechal Floriano, 1.294).
- **2025, a FACITA.** A Prefeitura assumiu a festa e lançou **R$ 1,93 mi em "festividades"**, com cerca de R$ 1,6 mi em shows por inexigibilidade: Cobaia R$ 582 mil (R$ 530 mil na FACITA e R$ 52 mil num show de junho), CER R$ 300 mil, B4 R$ 288 mil, OK Music R$ 250 mil, LR R$ 180 mil, SAM R$ 175 mil, MC Music R$ 80 mil e JVS R$ 50 mil. Mais a Festa Junina (palco, som, painel de LED, banheiros) e o evento da Rainha da FACITA.
- **Fonte do dinheiro em 2025: 100% Tesouro municipal.** Nada veio de convênio ou de repasse federal ou estadual.
- **O que ficou fora da função Cultura:** a decoração de Natal (Criativa Arte e Fibra, R$ 308 mil) foi para Desporto e Lazer. A organizadora da FACITA (Organização Estrela Som, R$ 835,6 mil homologados no PNCP) não aparece como empenho da Prefeitura de 2025 em nenhuma função. O custo real das festas é maior que o da função Cultura.

**Conclusão:** o salto da cultura **não veio de política cultural** (biblioteca, oficinas, patrimônio, editais), e sim de **shows**. Em 2025, quase dois terços do gasto foram festividades.

---

## 2. Urbanismo: de R$ 6,4 mi (2021) para R$ 16 a 21 mi (2022 a 2025)

| Grupo de despesa | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| Pessoal | 1.621 | 1.691 | 1.457 | **3.864** | 5.494 | 5.209 | 5.301 |
| Combustível | 161 | 163 | 163 | **1.233** | 1.161 | 956 | 1.090 |
| Energia (iluminação pública e prédios) | 1.531 | 1.678 | 1.616 | 1.726 | 1.431 | 1.455 | 2.164 |
| Obras | 1.976 | 3.446 | 2.129 | 3.171 | **6.325** | 3.253 | 2.312 |
| Veículos, máquinas e equipamentos | 975 | 933 | 37 | **3.042** | **3.210** | 321 | 891 |
| Limpeza terceirizada | 0 | 0 | 0 | 2 | 257 | 745 | 822 |
| Outro custeio (materiais, manutenção, sinalização) | 1.205 | 1.011 | 996 | 3.100 | 2.717 | 3.594 | 3.122 |
| **Total** | **7.469** | **8.922** | **6.398** | **16.138** | **20.595** | **15.533** | **15.702** |

### 2.1 O salto de 2022 (+R$ 9,7 mi): uma parte é contábil, a maior parte é real

| Componente | Variação 2021 para 2022 | Natureza |
|---|---|---|
| Pessoal | +2.407 | **Reclassificação.** No mesmo ano, o pessoal da função Administração caiu de 5.629 para 3.347 (−2.282). Os servidores de obras e serviços passaram a ser lançados em Urbanismo, coincidindo com a reorganização em Coordenadorias (LC 293/2021) |
| Combustível | +1.070 | **Em boa parte reclassificação.** O combustível da Administração caiu de 646 para 46 (−600). A frota de obras passou para Urbanismo (cartão combustível Link Card) |
| Veículos e máquinas | +3.005 | **Real.** Compra de caminhões e máquinas: ECS Veículos R$ 743 mil, M.R. Caminhões R$ 630 mil, Veneza Equipamentos R$ 469 mil, OK Nobre R$ 369 mil, Rodonaves R$ 350 mil |
| Obras | +1.042 | **Real.** Nova garagem da frota municipal (EDL Construtora, R$ 2,3 mi em 2022, com 4 aditivos), recapeamento (JRT) e início da ligação entre as ruas José Alfredo Nunes e Aparecido Custódio de Camargo (Maqterra) |
| Outro custeio | +2.493 | Real: materiais de construção e manutenção, peças, sinalização de trânsito (Sistrans R$ 278 mil) |

**Estimativa:** cerca de **R$ 3 mi do salto de 2022 (um terço) é mudança de lançamento contábil**: o mesmo gasto saiu da Administração e foi para o Urbanismo. Os outros **cerca de R$ 6,5 mi são gasto novo**: máquinas, caminhões, garagem, obras e materiais. Assim, a alta de +315% acima da inflação de 2013 a 2025, calculada em [gasto-real-por-area.md](gasto-real-por-area.md), superestima o aumento real. Descontada a reclassificação, o urbanismo ainda cresceu, mas perto de 2 a 2,5 vezes, e não 4 vezes.

### 2.2 O pico de 2023 (R$ 20,6 mi)
- **Obras: R$ 6,3 mi.**
  - Maqterra, R$ 3,9 mi: pavimentação em concreto de alto desempenho na ligação entre as ruas José Alfredo Nunes e Aparecido Custódio de Camargo, com termo aditivo de "acréscimos de serviços". O contrato aparece de 2022 a 2025, com reempenhos.
  - Noromix, R$ 1,4 mi: recapeamento em CBUQ com contratos de repasse federais (910894/2021, 925696/2021 e 925698/2021, Ministério do Desenvolvimento Regional e Caixa), ou seja, emendas e programas federais.
  - Construtora Azevedo: reforma da área administrativa, capela e sanitários e ampliação do pátio coberto do cemitério central.
- **Máquinas: R$ 3,2 mi.** Rolo compactador e motoniveladora (WC Veículos, R$ 1,35 mi), caminhões (Rodonaves, R$ 615 mil) e tratores (Agro PL, Carine).
- Em 2023 entraram R$ 2,5 mi de **convênios estaduais** em Urbanismo, o maior valor da série.

### 2.3 2024 e 2025: patamar alto e mais rígido
- **Pessoal (cerca de R$ 5,3 mi), energia (R$ 1,5 a 2,2 mi) e combustível (cerca de R$ 1 mi) somam cerca de R$ 8,5 mi fixos por ano.** Isso é mais da metade do urbanismo.
- **Limpeza pública terceirizada** desde 2023 (Absolluta, R$ 745 mil em 2024 e R$ 502 mil em 2025). Em 2025 houve contratação **com dispensa de licitação** de outra empresa de limpeza (J.S.L., R$ 320 mil). Um requerimento na Câmara cita processo administrativo contra a Absolluta por "abandono contratual" e uma contratação emergencial para o mesmo serviço (as datas no documento são inconsistentes).
- **Obras com dinheiro federal:** repavimentação (Makmo, R$ 1,6 mi, contrato de repasse 895283/2019 MDR/Caixa) e recapeamento (EMAV).
- **2025: o empréstimo FINISA entrou em Urbanismo.** Dos R$ 1,33 mi de "operações de crédito" empenhados em Urbanismo, **R$ 1,25 mi foram para a BMA Negócios, na "escadaria, estacionamento e reforma do Paço Municipal"**, ou seja, a sede da Prefeitura. Ver ponto de fiscalização na estratégia.
- Emenda parlamentar federal financiou a ampliação do Canil Municipal (Tantini, nº 202430640003).

### 2.4 De onde veio o dinheiro do Urbanismo (R$ mil)

| Fonte | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| Tesouro municipal | 5.485 | 6.224 | 3.922 | 15.638 | 17.643 | 13.310 | 12.705 |
| Convênios estaduais | 300 | 100 | 389 | 500 | 2.524 | 668 | 1.050 |
| Convênios e repasses federais | 1.684 | 2.597 | 2.087 | 0 | 427 | 1.556 | 614 |
| Operação de crédito (FINISA) | 0 | 0 | 0 | 0 | 0 | 0 | 1.334 |

O salto foi pago quase todo com **dinheiro próprio do município**. Isso foi possível com a alta das transferências livres (FPM e ICMS) a partir de 2021 (ver [receitas.md](receitas.md)).

---

## 3. Leitura (análise)

1. **A cultura dobrou por causa de show, não de política cultural.** Em 2025, quase dois terços foram festividades, pagas com dinheiro próprio. O que é estrutura de cultura (biblioteca, patrimônio, oficinas, fundo de turismo) seguiu parado.
2. **O urbanismo cresceu de verdade, mas menos do que parece.** Cerca de um terço do salto de 2022 é reclassificação contábil. O restante foi máquinas, caminhões, garagem, pavimentação e recapeamento, boa parte concentrada em 2022 e 2023, os anos do "Programa Novo Asfalto" e da troca de lajota por asfalto.
3. **O urbanismo ficou mais caro de manter.** Folha, energia, combustível e limpeza terceirizada criaram um piso de cerca de R$ 8,5 mi por ano, antes de qualquer obra.
4. **Pontos para fiscalizar:** (a) uso do FINISA na reforma do Paço Municipal; (b) aditivos da obra da Maqterra; (c) a troca emergencial da empresa de limpeza em 2025; (d) o custo total das festas espalhado por Cultura, Desporto e Urbanismo; (e) pagamento da organizadora da FACITA.
