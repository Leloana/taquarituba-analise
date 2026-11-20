"""Procura inconsistências nas contratações da Prefeitura de Taquarituba publicadas no PNCP (2024 a 2026).

Entrada: CSVs gerados por scripts/pncp_contratos.py (05-financas-publicas/dados/pncp_*.csv).
Uso: python scripts/pncp_inconsistencias.py
Saída: 05-financas-publicas/dados/pncp_inconsistencias_2024_2026.csv (um alerta por linha)

Regras (Lei 14.133/2021):
- art. 75, I e II: limites de dispensa por valor, atualizados por decreto a cada ano
  (2024: Decreto 11.871/2023; 2025: Decreto 12.343/2024; 2026: Decreto 12.807/2025);
- art. 75, § 1º: o limite vale para a soma do ano no mesmo ramo (fracionamento);
- art. 94: o contrato só tem eficácia depois de divulgado no PNCP, em até 20 dias úteis (licitação)
  ou 10 dias úteis (contratação direta) da assinatura;
- art. 125: acréscimos de até 25% (50% em reforma de edifício ou equipamento).
Um alerta não é prova de irregularidade: é um ponto para conferir no processo.
"""
import time
from pathlib import Path

import numpy as np
import pandas as pd
import requests

RAIZ = Path(__file__).resolve().parent.parent
D = RAIZ / "05-financas-publicas" / "dados"
CNPJ = "46634218000107"
LIMITES = {2024: (119812.02, 59906.02), 2025: (125451.15, 62725.59), 2026: (130984.20, 65492.11)}


def ler(nome):
    return pd.read_csv(D / nome, skiprows=1)


cp = ler("pncp_contratacoes_2024_2026.csv")
ct = ler("pncp_contratos_2024_2026.csv")
tm = ler("pncp_termos_aditivos_2024_2026.csv")
at = ler("pncp_atas_2024_2026.csv")
alertas = []


def alerta(tipo, controle, descricao, valor=None, url=None):
    alertas.append({"tipo": tipo, "controle_pncp": controle, "valor_rs": valor, "descricao": descricao, "url": url})


def url_compra(c):
    _, resto = c.split("-1-")
    seq, ano = resto.split("/")
    return f"https://pncp.gov.br/app/editais/{CNPJ}/{ano}/{int(seq)}"


# 1. Processos excluídos: buracos na numeração sequencial de cada ano
for ano, g in cp.groupby("ano_compra"):
    if ano < 2024:
        continue
    for seq in sorted(set(range(1, g.sequencial.max() + 1)) - set(g.sequencial)):
        try:
            st = requests.get(f"https://pncp.gov.br/api/consulta/v1/orgaos/{CNPJ}/compras/{ano}/{seq}", timeout=90).status_code
        except requests.RequestException:
            st = "erro"
        situacao = "excluída pelo órgão (HTTP 410)" if st == 410 else f"não consultável (HTTP {st})"
        alerta("processo excluído do PNCP", f"{CNPJ}-1-{seq:06d}/{ano}", f"Sequencial {seq}/{ano} {situacao}")
        time.sleep(0.3)

cp["vmax"] = cp[["valor_estimado_rs", "valor_homologado_rs"]].max(axis=1)
soma_ct = ct.groupby("controle_pncp_compra").valor_global_rs.sum()
cp["soma_contratos"] = cp.controle_pncp.map(soma_ct)
cp["n_contratos"] = cp.controle_pncp.map(ct.groupby("controle_pncp_compra").size()).fillna(0)
cp["n_atas"] = cp.controle_pncp.map(at.groupby("controle_pncp_compra").size()).fillna(0)
# Contas de luz e água (concessionárias) não geram contrato próprio; ficam fora dos alertas 4 e 5
cp["concessionaria"] = cp.objeto.str.contains("concession", case=False, na=False)

# 2. Dispensa por valor acima do limite do inciso declarado
disp = cp[cp.amparo_legal.str.contains(r"Art\. 75, I{1,2}$", regex=True, na=False)].copy()
disp["inciso"] = np.where(disp.amparo_legal.str.endswith(", I"), "I", "II")
disp["limite"] = [LIMITES.get(a, LIMITES[2024])[0 if i == "I" else 1] for a, i in zip(disp.ano_compra, disp.inciso)]
for _, r in disp[disp.vmax > disp.limite].iterrows():
    alerta("dispensa acima do limite do inciso declarado", r.controle_pncp,
           f"Art. 75, {r.inciso}: limite R$ {r.limite:,.2f} em {r.ano_compra}; processo de R$ {r.vmax:,.2f}. "
           f"Ou o enquadramento no PNCP está errado, ou a dispensa passou do teto. {r.objeto[:120]}",
           r.vmax, r.url_pncp)

# 3. Fracionamento: dispensas do art. 75, II com o mesmo tema no ano somando acima do limite
TEMAS = {"decoração natalina": r"natal", "postes": r"\bpostes?\b", "pesquisa de satisfação": r"satisfa",
         "kits/brinquedos": r"kit|brinquedo", "fantasias": r"fantasia", "uniformes": r"uniforme"}
d2 = disp[disp.inciso == "II"]
for tema, rx in TEMAS.items():
    for ano, g in d2[d2.objeto.str.contains(rx, case=False, regex=True)].groupby("ano_compra"):
        v = g[["valor_homologado_rs", "valor_estimado_rs"]].bfill(axis=1).iloc[:, 0].sum()
        if len(g) > 1 and v > LIMITES[ano][1]:
            alerta("possível fracionamento (art. 75, § 1º)", "; ".join(g.controle_pncp),
                   f"{len(g)} dispensas de '{tema}' em {ano} somam R$ {v:,.2f}, acima do limite anual de "
                   f"R$ {LIMITES[ano][1]:,.2f} para o mesmo ramo", v)

# 4. Homologado sem contrato publicado (fora registro de preços, que gera ata)
sem = cp[(cp.n_contratos == 0) & (cp.valor_homologado_rs > 0) & (~cp.registro_de_precos) & (~cp.concessionaria)]
for _, r in sem.iterrows():
    alerta("homologado sem contrato no PNCP", r.controle_pncp,
           f"{r.modalidade}, homologado R$ {r.valor_homologado_rs:,.2f} sem contrato publicado. {r.objeto[:120]}",
           r.valor_homologado_rs, r.url_pncp)

# 5. Licitação grande sem resultado meses depois
lim_data = pd.Timestamp.today() - pd.Timedelta(days=120)
x = cp[(cp.vmax >= 500000) & (cp.valor_homologado_rs.isna() | (cp.valor_homologado_rs == 0)) & (cp.n_contratos == 0) & (cp.n_atas == 0)
       & (~cp.concessionaria) & (pd.to_datetime(cp.data_publicacao_pncp) < lim_data) & (cp.situacao != "Revogada")
       & ~cp.modalidade.str.contains("Leilão")]
for _, r in x.iterrows():
    tipo = "registro de preços sem ata nem resultado" if r.registro_de_precos else "licitação sem resultado publicado"
    alerta(tipo, r.controle_pncp,
           f"{r.modalidade}, estimado R$ {r.valor_estimado_rs:,.2f}, publicado em {r.data_publicacao_pncp}, "
           f"sem valor homologado, contrato ou ata. {r.objeto[:120]}", r.valor_estimado_rs, r.url_pncp)

# 6. Prazos de publicação do contrato (art. 94) e contrato assinado antes de publicar o processo
m = ct.merge(cp[["controle_pncp", "modalidade", "data_publicacao_pncp"]].rename(
    columns={"controle_pncp": "cc", "data_publicacao_pncp": "pub_compra"}), left_on="controle_pncp_compra", right_on="cc")
ass = pd.to_datetime(m.data_assinatura).values.astype("datetime64[D]")
m["dias_uteis"] = np.busday_count(ass, pd.to_datetime(m.data_publicacao_pncp).values.astype("datetime64[D]"))
m["prazo"] = np.where(m.modalidade.isin(["Dispensa", "Inexigibilidade"]), 10, 20)
for _, r in m[m.dias_uteis > m.prazo].iterrows():
    alerta("contrato publicado fora do prazo (art. 94)", r.controle_pncp,
           f"{r.fornecedor}: assinado em {r.data_assinatura}, publicado em {r.data_publicacao_pncp} "
           f"({r.dias_uteis} dias úteis; prazo {r.prazo})", r.valor_global_rs, r.url_pncp)
m["antes"] = (pd.to_datetime(m.pub_compra) - pd.to_datetime(m.data_assinatura)).dt.days
for _, r in m[m.antes > 7].iterrows():
    alerta("contrato assinado antes de o processo ir ao PNCP", r.controle_pncp,
           f"{r.fornecedor}: assinado em {r.data_assinatura}, processo publicado {r.antes} dias depois ({r.pub_compra})",
           r.valor_global_rs, r.url_pncp)

# 7. Show contratado depois da data do evento (data lida no objeto)
MESES = {"janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4, "maio": 5, "junho": 6, "julho": 7, "agosto": 8,
         "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12}
for _, r in cp[cp.modalidade == "Inexigibilidade"].iterrows():
    t = r.objeto.lower()
    mt = pd.Series([t]).str.extract(r"dia (\d{1,2}) de (\w+) de (\d{4})").iloc[0]
    if mt.isna().any() or mt[1] not in MESES:
        continue
    evento = pd.Timestamp(int(mt[2]), MESES[mt[1]], int(mt[0]))
    if pd.Timestamp(r.data_publicacao_pncp) > evento:
        alerta("contratação publicada depois do evento", r.controle_pncp,
               f"Evento em {evento.date()}, processo publicado em {r.data_publicacao_pncp}. {r.objeto[:120]}",
               r.vmax, r.url_pncp)

# 8. Vigência de zero dias
for _, r in ct[ct.vigencia_fim <= ct.vigencia_inicio].iterrows():
    alerta("vigência de zero dias", r.controle_pncp, f"{r.fornecedor}: vigência {r.vigencia_inicio} a {r.vigencia_fim}",
           r.valor_global_rs, r.url_pncp)

# 9. Aditivos de valor acima de 25% do valor inicial
for _, r in tm[tm.valor_acrescido_rs > 0].merge(ct, left_on="controle_pncp_contrato", right_on="controle_pncp").iterrows():
    pct = r.valor_acrescido_rs / r.valor_inicial_rs
    if pct > 0.25 and "prorroga" not in str(r.objeto_x).lower():
        alerta("aditivo acima de 25%", r.controle_pncp_contrato,
               f"{r.fornecedor}: acréscimo de R$ {r.valor_acrescido_rs:,.2f} = {pct:.0%} do inicial "
               f"(limite 25%, ou 50% se reforma). {r.objeto_y[:100]}", r.valor_acrescido_rs, r.url_pncp)

# 10. Mesmo CNPJ com nomes diferentes (troca de razão social)
for cnpj, g in ct.groupby("fornecedor_cnpj_cpf"):
    nomes = sorted(set(g.fornecedor))
    if len(nomes) > 1 and cnpj != "(pessoa física)":
        alerta("mesmo CNPJ com nomes diferentes", cnpj, " / ".join(nomes), g.valor_global_rs.sum())

# 11. Contrato com valor diferente do homologado (fora registro de preços e sem aditivo)
com_aditivo = set(tm.controle_pncp_contrato)
for _, r in cp[(cp.n_contratos == 1) & (~cp.registro_de_precos) & (cp.valor_homologado_rs > 0)].iterrows():
    c = ct[ct.controle_pncp_compra == r.controle_pncp].iloc[0]
    if c.controle_pncp in com_aditivo:
        continue
    dif = c.valor_global_rs - r.valor_homologado_rs
    if c.valor_global_rs > 0 and abs(dif) >= 1:
        alerta("contrato diferente do homologado", c.controle_pncp,
               f"{c.fornecedor}: homologado R$ {r.valor_homologado_rs:,.2f}, contrato R$ {c.valor_global_rs:,.2f} "
               f"(diferença R$ {dif:,.2f})", dif, c.url_pncp)

out = pd.DataFrame(alertas)
with open(D / "pncp_inconsistencias_2024_2026.csv", "w", encoding="utf-8") as f:
    f.write(f"# Alertas gerados por scripts/pncp_inconsistencias.py em {time.strftime('%d/%m/%Y')} a partir dos CSVs pncp_*.csv. "
            "Alerta = ponto a conferir no processo, não prova de irregularidade.\n")
    out.to_csv(f, index=False)
print(out.tipo.value_counts().to_string())
