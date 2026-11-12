# -*- coding: utf-8 -*-
"""
Configuração do cliente — Bruno Corano · Black Manhattan Connection (Black Friday 2026).

Este é o ÚNICO arquivo que precisa ser editado para colocar o funil de um
cliente novo no ar (o build se recusa a rodar enquanto algum marcador de
preenchimento do template continuar aqui).
Ordem completa: "CHECKLIST DE NOVO CLIENTE" no topo do CLAUDE.md.

Depois de editar, teste localmente:

    python build/build.py --meta-file meta.csv --sales-file sales.csv --out dist/index.html

`build/config.example.py` é a cópia intacta deste modelo — mantenha-o
sem preencher, para restaurar o config.py se precisar começar do zero.
"""
from __future__ import annotations

# ==========================================================================
# 1) PLANILHA(S) DO CLIENTE (Google Sheets)
# ==========================================================================
# SPREADSHEET_ID: o trecho entre /d/ e /edit na URL da planilha
#   (https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit#gid=...)
# GID_META / GID_SALES: o número depois de "gid=" na URL de cada aba.
# A planilha precisa estar com o link público em modo "Qualquer pessoa com
# o link pode visualizar" (o build lê via export CSV, SOMENTE LEITURA).
# Meta Ads: planilha "Dados gerenciador - MCBF26", aba "Página1".
SPREADSHEET_ID = "1FCsTZj2b02kQtbQcvp_NrknCH3YgAdDLxb97lUFkN8A"
# Opcional: se a lista de Compradores estiver em OUTRA planilha, coloque o ID
# dela aqui. Vazio = Compradores na mesma planilha do Meta Ads (padrão).
# Compradores: planilha "MCTV| ACOMPANHAMENTO GERAL | LOOKER", aba "Dados The Members".
SPREADSHEET_ID_SALES = "1X6XKBc65KVsfrFIoBHsk_rxC4iUrzu0l9VSYoaF6PHY"
GID_META = "0"
GID_SALES = "953734831"

# ==========================================================================
# 2) REGRAS DE NEGÓCIO
# ==========================================================================
# Fator de imposto aplicado sobre o gasto do Meta Ads quando o toggle
# "Imposto Meta" estiver ligado. Use 1.0 se o cliente não tiver imposto.
TAX_FACTOR = 1.13806

# Produto principal do funil (base de Vendas/CAC/ConvCHK/Ticket). Casamento
# por PREFIXO sobre o nome NORMALIZADO (sem acento, minúsculas) da coluna
# Produto da planilha de Compradores — escreva sem acento e em minúsculas.
# Vários prefixos podem ser separados por "|".
# Neste cliente: 3 produtos principais da Black Friday — assinaturas Anual,
# Mensal e Semestral com o sufixo "- Black Friday" (ex.: "Assinatura Anual -
# Black Friday"). As vendas do perpétuo (mesmos produtos SEM o sufixo) ficam
# FORA do funil, a menos que a UTM case com um anúncio MC-BF26 do Meta.
# Variações de espaço no hífen ("-Black Friday", sem hífen) e a grafia sem
# "Assinatura" (como já ocorre na planilha: "Anual - Manhattan ...") cobertas.
# Trimestral fica de fora.
MAIN_PRODUCT_PREFIX = "|".join(
    f"{base}{sep}black friday"
    for base in ("assinatura anual", "assinatura mensal", "assinatura semestral",
                 "anual", "mensal", "semestral")
    for sep in (" - ", " -", " ")
)

# Qual coluna UTM da planilha de Compradores carrega o Ad Name do Meta:
# "utm_content", "utm_term" ou "utm_medium". Depende do parametrizador de URL
# dos anúncios do cliente — CONFIRA nos dados antes de assumir: a coluna que
# não carrega o anúncio costuma trazer o posicionamento (Instagram_Feed/Stories),
# e casar pela coluna errada zera as atribuições.
# Neste cliente: utm_content = Ad Name (utm_campaign = Campaign Name,
# utm_medium = Ad Set Name, utm_term = ID numérico). Verificado em 12/11/2026.
AD_UTM_COLUMN = "utm_content"

# A planilha de Compradores tem uma coluna de status de pagamento confiável?
# SIM -> False (o build filtra por is_paid()). NÃO (toda linha já é uma compra
# concretizada) -> True (conta todas as linhas como venda paga).
# Neste cliente: a aba "Dados The Members" só tem PURCHASE_APPROVED e não tem
# coluna de status -> conta todas as linhas.
COUNT_ALL_AS_PAID = True

# ==========================================================================
# 3) RÓTULOS EXIBIDOS NA INTERFACE
# ==========================================================================
CLIENT_NAME = "Manhattan Connection"
CLIENT_SUB = "Black Friday 2026"
TAX_LABEL = "Imposto Meta ×1,13806"
MAIN_PRODUCT = "Black Friday (Anual · Mensal · Semestral)"

# ==========================================================================
# 4) METAS (aba Relatórios) — código de cor de CAC/ROAS
# ==========================================================================
#   • ROAS: quanto MAIOR, melhor  -> desempenho = roas / ROAS_TARGET
#   • CAC : quanto MENOR, melhor  -> desempenho = CAC_TARGET / cac
# Faixas (sobre o desempenho): <REPORT_BAND_LOW vermelho · até 0,99 amarelo ·
#   até REPORT_BAND_HIGH verde · acima disso azul-ciano.
# Sem metas por enquanto (0 = sem código de cor). Definir após as primeiras
# leituras do funil da Black Friday.
CAC_TARGET = 0.0   # CAC alvo em R$ por venda do produto principal
ROAS_TARGET = 0.0  # ROAS alvo (Faturamento / Gasto)
REPORT_BAND_LOW = 0.70
REPORT_BAND_HIGH = 1.30

# ==========================================================================
# 5) IA INSIGHTS (Cloudflare Worker) — ver SETUP-IA.md
# ==========================================================================
# URL pública do Worker (não é secreta). Vazio = aba IA Insights indisponível.
# Preencher depois de publicar o Worker (checklist do CLAUDE.md).
# Por enquanto vazio (Worker ainda não configurado). Formato:
# https://black-manhattan-ia-insights.<subdominio>.workers.dev
IA_WORKER_URL = ""
