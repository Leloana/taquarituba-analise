"""Baixa do PNCP todas as contratações, contratos, atas e termos aditivos da Prefeitura de Taquarituba (2024 a 2026).

Fonte: API pública do PNCP (https://pncp.gov.br/api/consulta/swagger-ui/index.html), CNPJ 46.634.218/0001-07.
Uso: python scripts/pncp_contratos.py [pasta_cache]
Saída (05-financas-publicas/dados/):
    pncp_contratacoes_2024_2026.csv  um processo de compra por linha (todas as modalidades)
    pncp_contratos_2024_2026.csv     um contrato/empenho publicado por linha
    pncp_atas_2024_2026.csv          atas de registro de preços
    pncp_termos_aditivos_2024_2026.csv
O JSON bruto fica na pasta de cache (padrão /tmp/pncp_taquarituba) para não ser baixado de novo.
"""
import json
import sys
import time
from pathlib import Path

import pandas as pd
import requests

CNPJ = "46634218000107"
ANOS = [2024, 2025, 2026]
BASE = "https://pncp.gov.br/api/consulta/v1"
BASE_PNCP = "https://pncp.gov.br/api/pncp/v1"
RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "05-financas-publicas" / "dados"
CACHE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/pncp_taquarituba")
CACHE.mkdir(parents=True, exist_ok=True)

# Códigos de modalidade da API do PNCP
MODALIDADES = {1: "Leilão - Eletrônico", 2: "Diálogo Competitivo", 3: "Concurso", 4: "Concorrência - Eletrônica",
               5: "Concorrência - Presencial", 6: "Pregão - Eletrônico", 7: "Pregão - Presencial",
               8: "Dispensa", 9: "Inexigibilidade", 10: "Manifestação de Interesse", 11: "Pré-qualificação",
               12: "Credenciamento", 13: "Leilão - Presencial"}

S = requests.Session()


def get(url, params=None, tentativas=6):
    for i in range(tentativas):
        try:
            r = S.get(url, params=params, timeout=90)
            if r.status_code == 204:
                return None
            if r.status_code == 200:
                return r.json()
            if r.status_code == 404:
                return None
        except requests.RequestException:
            pass
        time.sleep(3 * (i + 1))
    raise RuntimeError(f"falhou: {url} {params}")


def cache(nome, func):
    f = CACHE / f"{nome}.json"
    if f.exists():
        return json.loads(f.read_text())
    dados = func()
    f.write_text(json.dumps(dados, ensure_ascii=False))
    return dados


def paginar(endpoint, params):
    out, pag = [], 1
    while True:
        j = get(f"{BASE}/{endpoint}", {**params, "pagina": pag, "tamanhoPagina": 50})
        if not j or not j.get("data"):
            break
        out += j["data"]
        if j.get("paginasRestantes", 0) == 0:
            break
        pag += 1
    return out


def periodo(ano):
    fim = min(f"{ano}1231", time.strftime("%Y%m%d"))
    return f"{ano}0101", fim


def baixar():
    compras, contratos, atas = [], [], []
    for ano in ANOS:
        ini, fim = periodo(ano)
        contratos += cache(f"contratos_{ano}", lambda: paginar(
            "contratos", {"dataInicial": ini, "dataFinal": fim, "cnpjOrgao": CNPJ}))
        atas += cache(f"atas_{ano}", lambda: paginar(
            "atas", {"dataInicial": ini, "dataFinal": fim, "cnpj": CNPJ}))
        for cod in MODALIDADES:
            compras += cache(f"compras_{ano}_{cod}", lambda: paginar(
                "contratacoes/publicacao", {"dataInicial": ini, "dataFinal": fim, "cnpj": CNPJ,
                                            "codigoModalidadeContratacao": cod}))
    termos = []
    for c in contratos:
        a, s = c["anoContrato"], c["sequencialContrato"]
        t = cache(f"termos_{a}_{s}", lambda: get(f"{BASE_PNCP}/orgaos/{CNPJ}/contratos/{a}/{s}/termos") or [])
        for x in t:
            x["_contrato"] = c["numeroControlePNCP"]
        termos += t
    return compras, contratos, atas, termos


def main():
    compras, contratos, atas, termos = baixar()

    cp = pd.DataFrame([{
        "controle_pncp": c["numeroControlePNCP"],
        "ano_compra": c["anoCompra"],
        "sequencial": c["sequencialCompra"],
        "numero_compra": c.get("numeroCompra"),
        "processo": c.get("processo"),
        "modalidade": c.get("modalidadeNome"),
        "amparo_legal": (c.get("amparoLegal") or {}).get("nome"),
        "registro_de_precos": c.get("srp"),
        "situacao": c.get("situacaoCompraNome"),
        "data_publicacao_pncp": (c.get("dataPublicacaoPncp") or "")[:10],
        "data_abertura_proposta": (c.get("dataAberturaProposta") or "")[:10],
        "valor_estimado_rs": c.get("valorTotalEstimado"),
        "valor_homologado_rs": c.get("valorTotalHomologado"),
        "objeto": " ".join(str(c.get("objetoCompra") or "").split()),
        "url_pncp": f"https://pncp.gov.br/app/editais/{CNPJ}/{c['anoCompra']}/{c['sequencialCompra']}",
    } for c in compras]).drop_duplicates("controle_pncp").sort_values(["ano_compra", "sequencial"])

    ct = pd.DataFrame([{
        "controle_pncp": c["numeroControlePNCP"],
        "controle_pncp_compra": c.get("numeroControlePncpCompra"),
        "ano_contrato": c["anoContrato"],
        "sequencial": c["sequencialContrato"],
        "numero_contrato": c.get("numeroContratoEmpenho"),
        "processo": c.get("processo"),
        "tipo": (c.get("tipoContrato") or {}).get("nome"),
        "categoria": (c.get("categoriaProcesso") or {}).get("nome"),
        "fornecedor_cnpj_cpf": c.get("niFornecedor") if c.get("tipoPessoa") == "PJ" else "(pessoa física)",
        "fornecedor": c.get("nomeRazaoSocialFornecedor") if c.get("tipoPessoa") == "PJ" else "(pessoa física)",
        "data_assinatura": c.get("dataAssinatura"),
        "vigencia_inicio": c.get("dataVigenciaInicio"),
        "vigencia_fim": c.get("dataVigenciaFim"),
        "data_publicacao_pncp": (c.get("dataPublicacaoPncp") or "")[:10],
        "valor_inicial_rs": c.get("valorInicial"),
        "valor_global_rs": c.get("valorGlobal"),
        "valor_acumulado_rs": c.get("valorAcumulado"),
        "objeto": " ".join(str(c.get("objetoContrato") or "").split()),
        "url_pncp": f"https://pncp.gov.br/app/contratos/{CNPJ}/{c['anoContrato']}/{c['sequencialContrato']}",
    } for c in contratos]).drop_duplicates("controle_pncp").sort_values(["ano_contrato", "sequencial"])

    at = pd.DataFrame([{
        "controle_pncp_ata": a.get("numeroControlePNCPAta"),
        "controle_pncp_compra": a.get("numeroControlePNCPCompra"),
        "numero_ata": a.get("numeroAtaRegistroPreco"),
        "ano_ata": a.get("anoAta"),
        "data_assinatura": (a.get("dataAssinatura") or "")[:10],
        "vigencia_inicio": (a.get("vigenciaInicio") or "")[:10],
        "vigencia_fim": (a.get("vigenciaFim") or "")[:10],
        "cancelado": a.get("cancelado"),
        "objeto": " ".join(str(a.get("objetoContratacao") or "").split()),
    } for a in atas]).drop_duplicates("controle_pncp_ata")

    tm = pd.DataFrame([{
        "controle_pncp_contrato": t["_contrato"],
        "sequencial_termo": t.get("sequencialTermoContrato"),
        "numero_termo": t.get("numeroTermoContrato"),
        "tipo": t.get("tipoTermoContratoNome"),
        "data_assinatura": t.get("dataAssinatura"),
        "vigencia_fim": t.get("dataVigenciaFim"),
        "valor_acrescido_rs": t.get("valorAcrescido"),
        "valor_global_rs": t.get("valorGlobal"),
        "prazo_aditado_dias": t.get("prazoAditadoDias"),
        "objeto": " ".join(str(t.get("objetoTermoContrato") or "").split()),
    } for t in termos])

    cab = (f"# Fonte: PNCP, API de consulta (https://pncp.gov.br/api/consulta), CNPJ 46.634.218/0001-07 "
           f"(Prefeitura de Taquarituba), consultada em {time.strftime('%d/%m/%Y')}. Gerado por scripts/pncp_contratos.py.\n")
    for df, nome in [(cp, "pncp_contratacoes_2024_2026.csv"), (ct, "pncp_contratos_2024_2026.csv"),
                     (at, "pncp_atas_2024_2026.csv"), (tm, "pncp_termos_aditivos_2024_2026.csv")]:
        with open(SAIDA / nome, "w", encoding="utf-8") as f:
            f.write(cab)
            df.to_csv(f, index=False)
        print(nome, len(df))


if __name__ == "__main__":
    main()
