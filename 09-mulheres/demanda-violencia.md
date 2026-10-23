# Demanda: violência contra a mulher e vulnerabilidade em Taquarituba

Data de referência: 23/10/2026. Marcações: **[fato]**, **[cálculo]**, **[estimativa]**, **[análise]**.

Dados em `dados/ssp_violencia_domestica_mulher_2024_2026.csv`, `dados/ssp_taxa_violencia_domestica_comparada.csv`, `dados/ssp_ocorrencias_criminais_2019_2026.csv`, `dados/sinan_violencia_mulheres_residentes_2010_2025.csv`.

---

## 1. Fontes usadas

- **[S1] SSP-SP, base de vítimas de violência doméstica contra a mulher** (microdados por boletim, de 2024 a ago/2026): https://www.ssp.sp.gov.br/assets/estatistica/vitimas-violencia-domestica/Base_Viol%C3%AAncia%20contra%20mulher.xlsx, arquivo atualizado em 07/10/2026, baixado em 23/10/2026. Filtrei pelo município do fato (COD IBGE 3553807) e contei vítimas únicas por boletim. Os microdados têm nome de rua, bairro e coordenadas; nada disso foi copiado para o repositório, só contagens.
- **[S2] SSP-SP, ocorrências mensais por município** (API do portal): https://www.ssp.sp.gov.br/v1/OcorrenciasMensais/RecuperaDadosMensaisAgrupados?ano=2026&grupoDelito=6&tipoGrupo=MUNIC%C3%8DPIO&idGrupo=602, consulta 23/10/2026. Não separa por sexo.
- **[S3] DATASUS, SINAN violência interpessoal e autoprovocada, São Paulo**: http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sinannet/cnv/violesp.def, mulheres residentes em Taquarituba, consulta 23/10/2026. 2025 é preliminar.
- **[S4] IBGE, Censo 2022, SIDRA tabela 9514**: 11.747 mulheres residentes em Taquarituba (https://apisidra.ibge.gov.br/values/t/9514/n6/in%20n3%2035/v/93/p/2022/c2/5/c287/100362/c286/113635).
- **[S5] CNJ DataJud, API pública do TJ-SP** (https://api-publica.datajud.cnj.jus.br/api_publica_tjsp/_search), consulta 23/10/2026.

---

## 2. Violência doméstica registrada pela polícia [S1]

| Período | Mulheres vítimas | Lesão corporal | Ameaça | Calúnia, difamação, injúria | Descumprimento de medida protetiva | Violência psicológica | Perseguição |
|---|---|---|---|---|---|---|---|
| 2024 (ano) | 134 | 57 | 60 | 33 | 17 | 6 | 5 |
| 2025 (ano) | 182 | 45 | 78 | 69 | 33 | 14 | 7 |
| jan-ago 2024 | 91 | 39 | 37 | 21 | 13 | 4 | 4 |
| jan-ago 2025 | 106 | 25 | 43 | 40 | 22 | 11 | 3 |
| **jan-ago 2026** | **129** | **53** | 56 | 28 | 13 | 12 | 8 |

**[cálculo sobre S1]** Uma vítima pode ter mais de um crime no mesmo boletim, por isso as colunas não somam o total.

Leituras:
- De janeiro a agosto de 2026 foram **129 mulheres vítimas**, contra 106 no mesmo período de 2025 (**+22%**) e 91 em 2024 (**+42%**) **[cálculo]**.
- Lesão corporal dolosa contra mulher em contexto doméstico mais que dobrou: 25 para 53 no comparativo jan-ago **[cálculo]**.
- Projeção para 2026 inteiro: cerca de **190 mulheres**, mantido o ritmo de jan-ago (129 × 12/8 ≈ 194) **[estimativa]**.
- Relação com o agressor (2024 a ago/2026, 366 vítimas com relação informada, de 445): união estável 164, parentesco 82, casamento 67, envolvimento amoroso 42 **[cálculo]**.
- Faixa etária (mesmo período): 18 a 29 anos, 140; 30 a 39, 134; 40 a 49, 78; 60 ou mais, 38; menores de 18, 20 **[cálculo]**.
- Nenhuma vítima fatal registrada na base de 2024 a ago/2026 **[cálculo]**.

### 2.1 Quem levou o caso à delegacia [S1]

| Período | Pela própria vítima | Polícia Militar | GCM (Polícia Municipal) | Outros |
|---|---|---|---|---|
| 2024 (ano) | 87 | 44 | **0** | 3 |
| 2025 (ano) | 120 | 17 | **30** | 15 |
| jan-ago 2026 | 65 | 30 | **23** | 11 |

A GCM passou de nenhum caso de violência doméstica apresentado em 2024 para 30 em 2025 e 23 em jan-ago de 2026 **[cálculo]**. É o rastro mais objetivo da atuação da Patrulha Maria da Penha. Em 2026, 18% das vítimas chegaram à delegacia pela GCM (23 de 129) **[cálculo]**.

### 2.2 Comparação com o Estado e vizinhos (jan-ago, vítimas por mil mulheres) [S1, S4]

| Local | 2024 | 2025 | 2026 |
|---|---|---|---|
| **Taquarituba** | 7,75 | 9,02 | **10,98** |
| Itaí | 7,42 | 7,34 | 7,67 |
| Fartura | 10,33 | 10,21 | 10,45 |
| Paranapanema | 5,03 | 6,08 | 10,90 |
| Avaré | 9,37 | 8,34 | 10,46 |
| Estado de SP | 5,83 | 6,34 | 7,27 |
| Mediana de 99 municípios paulistas com 8 a 16 mil mulheres | 6,88 | 7,22 | 8,08 |

**[cálculo]** Em jan-ago de 2025, Taquarituba ficou na 128ª posição entre 643 municípios com registro, do maior para o menor **[cálculo]**. A taxa de Taquarituba em 2026 é 51% maior que a do Estado e 36% maior que a mediana de municípios parecidos **[cálculo]**.

**[análise]** O aumento pode ser mais violência ou mais notificação. Três sinais apontam para mais notificação: (a) a GCM passou a levar casos (0 → 30 → 23); (b) o Estado inteiro subiu 15% de 2025 para 2026 (145.876 → 167.363 vítimas jan-ago), sinal de mudança de registro ou de procura em escala estadual; (c) o crescimento de 2026 se concentra em lesão corporal, crime que costuma ser registrado em flagrante ou por terceiros. Mas não há como separar os dois efeitos com os dados públicos.

---

## 3. Ocorrências gerais no município (todos os sexos) [S2]

| Ano | Lesão corporal dolosa | Estupro + estupro de vulnerável | Homicídio doloso |
|---|---|---|---|
| 2019 | 129 | 16 | 1 |
| 2022 | 125 | 12 | 3 |
| 2023 | 93 | 24 | 2 |
| 2024 | 133 | 19 | 2 |
| 2025 | 145 | 15 | 3 |
| 2026 (jan-ago) | 120 | 10 | 1 |

**[fato]** Em 2026, todos os 10 estupros registrados foram de vulnerável (menor de 14 ou sem capacidade de resistir). A base de violência doméstica [S1] não cobre estupro, por isso violência sexual contra mulheres adultas fica sub-representada aqui.

**[cálculo]** Lesão corporal doméstica contra mulher (53, jan-ago 2026) equivale a 44% de todas as lesões corporais dolosas do município no período (120).

Feminicídio: a SSP-SP não publica feminicídio por município nessa API. O caso de maior repercussão é de 2022: um homem matou as duas filhas, de 5 e 6 anos, para atingir a ex-companheira, e foi condenado a 60 anos em outubro de 2026, com reconhecimento de feminicídio em contexto de violência doméstica (A Voz do Vale, https://avozdovale.com.br/pai-e-condenado-a-60-anos-de-prisao-por-matar-as-duas-filhas-em-taquarituba/; Sudoeste Paulista, https://sudoestepaulista.com.br/maldito-pai-que-matou-duas-filhas-em-taquarituba-e-condenado-a-60-anos-de-prisao/, out/2026) **[fato]**.

---

## 4. Saúde: notificações SINAN [S3]

| Ano | Notificações de mulheres residentes | Autoprovocadas | Violência interpessoal | com violência física | com violência sexual |
|---|---|---|---|---|---|
| 2022 | 27 | 21 | 6 | 5 | 1 |
| 2023 | 48 | 23 | 25 | 4 | 17 |
| 2024 | 25 | 18 | 7 | 5 | 2 |
| 2025 | 52 | 38 | 14 | 3 | 6 |

**[fato]** Em 2025, a saúde notificou 14 casos de violência interpessoal contra mulheres residentes, contra 182 vítimas na polícia [S1].

**[análise]** A notificação compulsória pela saúde (obrigatória para violência contra a mulher desde a Lei 10.778/2003) capta menos de 10% do que chega à polícia. Ou a rede de saúde não identifica ou não notifica os casos. Isso é um problema de eficácia da rede, porque a notificação é a porta para o CREAS. O pico de 2023 (17 casos com violência sexual) concentrou-se em meninas: 16 das 25 notificações interpessoais daquele ano eram de 5 a 14 anos.

---

## 5. Medidas protetivas (Justiça)

- **[fato]** A API pública do DataJud tem só 45 processos da classe "Medidas Protetivas de Urgência (Lei Maria da Penha) Criminal" (código 1268) na Vara Única de Taquarituba, o mais recente de 2024 [S5]. Medidas protetivas tramitam em segredo de justiça e quase não aparecem na base pública, por isso esse número não mede a demanda.
- **[fato]** Boletins por descumprimento de medida protetiva: 17 (2024), 33 (2025), 13 (jan-ago 2026) [S1]. É o único indicador público de que há medidas protetivas ativas no município.
- O painel do CNJ (Monitoramento da Política Judiciária Nacional de Enfrentamento à Violência contra as Mulheres) é em Power BI e não foi extraído **[lacuna]**. Número de medidas concedidas na comarca vai nos pedidos de LAI ao TJ-SP.

---

## 6. Vulnerabilidade

- **Mulheres residentes**: 11.747 (Censo 2022), contra 12.603 homens; o saldo masculino é inflado pela Penitenciária (`01-demografia/populacao.md`) **[fato]**.
- **Bolsa Família**: 1.174 famílias em jun/2026 (MDS MI Social, em `02-economia/renda-e-desigualdade.md`) **[fato]**. No Brasil, 84,1% das responsáveis familiares do programa são mulheres (MDS, Informe Bolsa Família, mar/2026, https://www.gov.br/mds/pt-br/acoes-e-programas/bolsa-familia/informes/2026/informe_bolsa_familia_n_109.pdf). Aplicando a proporção nacional: cerca de **990 famílias chefiadas por mulheres** no programa em Taquarituba **[estimativa]**.
- CadÚnico: 584 famílias em extrema pobreza e 391 em pobreza (MDS, 06/2026, mesmo arquivo do repositório) **[fato]**. O recorte por sexo do responsável não foi obtido: o portal do MDS (aplicacoes.mds.gov.br) redirecionava para uma página de aviso em 23/10/2026 **[lacuna]**.
- Mães solo e renda das mulheres pelo Censo 2022: não extraídos nesta rodada **[lacuna]**.

---

## 7. Tamanho da demanda (síntese)

| Grupo | Número | Tipo |
|---|---|---|
| Mulheres com boletim de violência doméstica em 2026 | 129 (jan-ago); cerca de 190 no ano | cálculo; estimativa |
| Mulheres com boletim em 2025 | 182 | cálculo |
| Casos que a saúde notificou em 2025 | 14 | fato |
| Vítimas que chegam pela GCM em 2026 | 23 (jan-ago) | cálculo |
| Famílias do Bolsa Família chefiadas por mulheres | cerca de 990 | estimativa |
| Mulheres residentes | 11.747 | fato |

**[análise]** Pesquisas nacionais de vitimização indicam que a maior parte das mulheres agredidas não registra boletim, então a demanda real é maior que os 190 por ano. Não usei multiplicador de subnotificação para não inventar número local.
