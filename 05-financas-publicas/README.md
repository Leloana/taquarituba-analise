# Finanças públicas de Taquarituba (SP), IBGE 3553807

Pesquisa feita em 20/10/2026. Série histórica de 2009 a 2026, com foco nos dados mais recentes (execução 2025, LOA 2026 e execução parcial de 2026 até agosto).

## Como ler

- **Dado oficial**: número tirado de fonte pública oficial (Tesouro Nacional/Siconfi, TCE-SP, leis municipais, CGU, Governo SP, ALESP, TSE). Sempre com URL ao lado.
- **Cálculo próprio**: razão ou soma feita por mim a partir de dados oficiais (marcado como "cálculo próprio").
- **Análise**: interpretação minha, marcada como **Análise**.
- Valores em R$ correntes (nominais, sem correção pela inflação), salvo indicação.
- Onde não achei o dado, está escrito "não localizado".

## Resumo em números (dados mais recentes)

| Indicador | Valor | Fonte |
|---|---|---|
| LOA 2026 (receita estimada = despesa fixada) | R$ 192,45 mi | [Lei 1.998/2025](https://www.taquarituba.sp.gov.br/legislacao/download-lei/13497/) |
| LOA 2025 (dotação inicial) | R$ 160,98 mi | [Siconfi RREO 2025](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?an_exercicio=2025&nr_periodo=6&co_tipo_demonstrativo=RREO&no_anexo=RREO-Anexo%2001&co_esfera=M&id_ente=3553807) |
| Receita realizada 2025 (com intra, líquida de FUNDEB) | R$ 196,01 mi, sendo R$ 18 mi de empréstimo | idem |
| Despesa empenhada 2025 | R$ 181,08 mi | idem |
| Execução 2026 até agosto | receita R$ 133,20 mi; empenho R$ 177,79 mi; liquidado R$ 129,50 mi | [Siconfi RREO 2026 4º bim](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?an_exercicio=2026&nr_periodo=4&co_tipo_demonstrativo=RREO&no_anexo=RREO-Anexo%2001&co_esfera=M&id_ente=3553807) |
| Dependência de transferências (2025) | 80,6% das receitas correntes (cálculo próprio) | [Siconfi DCA 2025](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2025&no_anexo=DCA-Anexo%20I-C&id_ente=3553807) |
| Pessoal / RCL (ago/2026) | 38,98% (limite 54%) | [Siconfi RGF 2026 2º quad.](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rgf?an_exercicio=2026&in_periodicidade=Q&nr_periodo=2&co_tipo_demonstrativo=RGF&no_anexo=RGF-Anexo%2001&co_esfera=M&co_poder=E&id_ente=3553807) |
| Dívida consolidada (ago/2026) | R$ 24,68 mi (14,81% da RCL) | [Siconfi RGF Anexo 02](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rgf?an_exercicio=2026&in_periodicidade=Q&nr_periodo=2&co_tipo_demonstrativo=RGF&no_anexo=RGF-Anexo%2002&co_esfera=M&co_poder=E&id_ente=3553807) |
| Empréstimo FINISA/Caixa | até R$ 25 mi autorizados; R$ 18 mi ingressaram em 2025 | [Lei 1.974/2025](https://www.taquarituba.sp.gov.br/legislacao/download-lei/12835/) |
| Passivo atuarial do RPPS (Capstuba) | R$ 151,39 mi (ago/2026) | [Siconfi RGF Anexo 02](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rgf?an_exercicio=2026&in_periodicidade=Q&nr_periodo=2&co_tipo_demonstrativo=RGF&no_anexo=RGF-Anexo%2002&co_esfera=M&co_poder=E&id_ente=3553807) |
| Último parecer do TCE (contas 2024) | Favorável (sessão 31/03/2026) | [TCE-SP TC-004288/989/24](https://www.tce.sp.gov.br/jurisprudencia/exibir?proc=4288/989/24&offset=0) |
| IEG-M 2024 | C+ (B em educação, saúde e fiscal; C em planejamento, ambiente e cidade) | idem |
| Emendas federais pagas a favorecidos de Taquarituba 2016 a 2026 | R$ 11,20 mi (cálculo próprio) | [CGU, base de emendas](https://portaldatransparencia.gov.br/download-de-dados/emendas-parlamentares/UNICO) |

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| [orcamento.md](orcamento.md) | LOAs 2011 a 2026, LDO 2026 e 2027, PPA 2026-2029, previsto x executado |
| [receitas.md](receitas.md) | Receitas 2013 a 2025, receita própria x transferências, dependência |
| [despesas.md](despesas.md) | Despesa por função e por natureza 2013 a 2025, saúde e educação, pessoal, investimento, dívida, resultado |
| [contas-e-tce.md](contas-e-tce.md) | Pareceres do TCE-SP 2009 a 2024, IEG-M 2014 a 2024, apontamentos |
| [emendas-parlamentares.md](emendas-parlamentares.md) | Emendas federais (CGU) e estaduais (Governo SP/ALESP) |
| [dados/](dados/) | CSVs com todas as séries |

### CSVs em `dados/`

- `receitas_2013_2025_siconfi_dca.csv`
- `despesas_funcao_2013_2025_siconfi_dca.csv`
- `despesas_natureza_2013_2025_siconfi_dca.csv`
- `orcamento_loa_execucao_2011_2026.csv`
- `loa_2026_por_funcao.csv`
- `pessoal_e_divida_rgf_2018_2026.csv`
- `tce_pareceres_e_indices_2009_2024.csv`
- `iegm_tce_2014_2024.csv`
- `emendas_federais_cgu_por_favorecido.csv`
- `emendas_federais_resumo_por_autor.csv`
- `emendas_estaduais_sp_taquarituba.csv`

## Fontes principais

- Tesouro Nacional, API de dados abertos do Siconfi (DCA, RREO, RGF, extrato de entregas): `https://apidatalake.tesouro.gov.br/ords/siconfi/tt/` com `id_ente=3553807`. O DCA no Siconfi começa em 2013 para o município; RREO e RGF começam em 2018. FINBRA anterior a 2013 não foi baixado.
- Leis municipais (LOA, LDO, PPA, operação de crédito): portal da Prefeitura, `https://www.taquarituba.sp.gov.br/legislacao/download-lei/<id>/`.
- TCE-SP, pesquisa de jurisprudência (pareceres de contas anuais): `https://www.tce.sp.gov.br/jurisprudencia/`; Relatório de Desempenho Municipal: https://www.tce.sp.gov.br/sites/default/files/rdm/taquarituba.pdf
- CGU, Portal da Transparência, base de emendas parlamentares (arquivo de 09/10/2026): https://portaldatransparencia.gov.br/download-de-dados/emendas-parlamentares/UNICO
- Governo SP, emendas impositivas 2020 a 2022: https://www.transparencia.sp.gov.br/home/emendasparlamentares ; ALESP, quadro consolidado de emendas 2025: https://www.al.sp.gov.br/spl/2025/02/Acessorio/1000597524_1000740220_Acessorio.pdf

## Lacunas conhecidas

- Receitas e despesas detalhadas de 2009 a 2012 (FINBRA) não foram baixadas; para esses anos há só LOA (2011 e 2012) e índices do TCE.
- DCA de 2016 declarado ao Siconfi sem ISS, ITBI e taxas (a própria declaração está incompleta).
- RGF/RREO no Siconfi só a partir de 2018. Percentuais de saúde e educação de 2025 e 2026 não estão no Siconfi (vêm de SIOPS/SIOPE e do TCE, que ainda não julgou 2025).
- Painéis de emendas estaduais 2023 a 2026 (Power BI do Governo SP) não foram extraídos; a lista estadual é parcial.
- Meu Município e Compara Brasil não foram consultados porque replicam os mesmos dados do Siconfi já usados aqui.
