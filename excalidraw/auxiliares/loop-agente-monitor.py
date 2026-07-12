"""Gera o JSON do diagrama Loop do Agente — monitor-agent"""
import json

elements = []

def text(x, y, content, fontSize=13, strokeColor="#1e1e1e", fontFamily=2, textAlign="left", **kwargs):
    lines = content.split('\n')
    w = round(max(max(len(l) for l in lines) * fontSize * 0.58, 60))
    h = round(len(lines) * fontSize * 1.35)
    el = {
        "type": "text", "x": x, "y": y, "width": w, "height": h,
        "fontSize": fontSize, "fontFamily": fontFamily, "textAlign": textAlign,
        "verticalAlign": "top", "autoResize": True, "lineHeight": 1.25,
        "strokeColor": strokeColor, "angle": 0, "opacity": 100,
        "roundness": None, "boundElements": None, "groupIds": [], "frameId": None,
        "isDeleted": False, "locked": False, "seed": 1, "versionNonce": 1,
        "updated": 1, **kwargs
    }
    el["text"] = content
    return el

def rect(x, y, w, h, bg="#ffffff", stroke="#adb5bd", strokeWidth=2, **kwargs):
    return {
        "type": "rectangle", "x": x, "y": y, "width": w, "height": h,
        "backgroundColor": bg, "strokeColor": stroke, "strokeWidth": strokeWidth,
        "fillStyle": "solid", "roughness": 0, "angle": 0, "opacity": 100,
        "roundness": {"type": 3}, "boundElements": None, "groupIds": [],
        "frameId": None, "isDeleted": False, "locked": False,
        "seed": 1, "versionNonce": 1, "updated": 1, **kwargs
    }

def arrow(x1, y1, x2, y2, color="#868e96", strokeWidth=2):
    return {
        "type": "arrow", "x": x1, "y": y1, "width": x2-x1, "height": y2-y1,
        "strokeColor": color, "strokeWidth": strokeWidth, "fillStyle": "solid",
        "roughness": 0, "startArrowhead": None, "endArrowhead": "arrow",
        "points": [[0, 0], [x2-x1, y2-y1]], "angle": 0, "opacity": 100,
        "roundness": {"type": 2}, "boundElements": None, "groupIds": [],
        "frameId": None, "isDeleted": False, "locked": False,
        "seed": 1, "versionNonce": 1, "updated": 1
    }

# ── Fundo ──
elements.append(rect(20, 20, 920, 620, bg="#f8f9fa", stroke="#dee2e6"))

# ── Título ──
elements.append(text(60, 40, "Loop do Agente — monitor-agent", fontSize=26))
elements.append(text(60, 78, 'Entrada: "alerta de latencia no servico checkout"', fontSize=14, strokeColor="#868e96"))

# ── Colunas: esquerda (x=40, w=420) | direita (x=500, w=420) ──
COL_LEFT = 40
COL_RIGHT = 500
CARD_W = 420
ROW1_Y = 120
ROW2_Y = 370
CARD_H = 220

# Estilos por fase
styles = [
    {"bg": "#e7f5ff", "stroke": "#4c6ef5", "label": "1. PLANEJAR"},
    {"bg": "#fff4e6", "stroke": "#fd7e14", "label": "2. EXECUTAR"},
    {"bg": "#f0fff4", "stroke": "#40c057", "label": "3. OBSERVAR"},
    {"bg": "#f3f0ff", "stroke": "#7950f2", "label": "4. REPLANEJAR"},
]

positions = [
    (COL_LEFT, ROW1_Y),   # 1. PLANEJAR
    (COL_RIGHT, ROW1_Y),  # 2. EXECUTAR
    (COL_LEFT, ROW2_Y),   # 3. OBSERVAR
    (COL_RIGHT, ROW2_Y),  # 4. REPLANEJAR
]

contents = [
    # 1. PLANEJAR
    "LLM recebe o alerta e decide\npor onde começar:\n\n🔍 consultar_metricas(\n    'checkout', 30)\n→ métricas primeiro, depois\n  logs se necessário",
    # 2. EXECUTAR
    "Runtime chama a ferramenta:\n\n⚡ consultar_metricas(\n  nome_servico='checkout',\n  janela_tempo_minutos=30)\n\n↪ latencia_p99: 450ms\n↪ taxa_erro: 12%\n↪ status: degraded",
    # 3. OBSERVAR
    "Coleta e analisa o resultado:\n\n📊 p99 subiu 3× em 30 min\n📊 12% das reqs. falhando\n📊 degradação súbita\n→ Evidências coletadas,\n  mas sem causa raiz ainda",
    # 4. REPLANEJAR
    "Ajusta o plano com novas\nferramentas:\n\n1️⃣ buscar_logs('checkout', 60)\n2️⃣ historico_deploys('checkout', 4)\n3️⃣ buscar_issues(repo='checkout')\n4️⃣ relatorio_incidente(...)\n→ volta para EXECUTAR",
]

for i, ((cx, cy), style, content) in enumerate(zip(positions, styles, contents)):
    # Card
    elements.append(rect(cx, cy, CARD_W, CARD_H, bg=style["bg"], stroke=style["stroke"], strokeWidth=2))
    # Número da fase
    elements.append(text(cx + 15, cy + 10, style["label"], fontSize=17, strokeColor=style["stroke"], fontFamily=2))
    # Conteúdo
    elements.append(text(cx + 15, cy + 40, content, fontSize=12, strokeColor="#1e1e1e", fontFamily=3))

# ── Setas ──
# PLANEJAR → EXECUTAR (horizontal, entre cards da row 1)
elements.append(arrow(COL_LEFT + CARD_W, ROW1_Y + CARD_H//2, COL_RIGHT, ROW1_Y + CARD_H//2, color="#4c6ef5", strokeWidth=2))
# EXECUTAR ↓ OBSERVAR (vertical, lado direito)
elements.append(arrow(COL_RIGHT + CARD_W//2, ROW1_Y + CARD_H, COL_LEFT + CARD_W//2, ROW2_Y, color="#fd7e14", strokeWidth=2))
# OBSERVAR → REPLANEJAR (horizontal, entre cards da row 2)
elements.append(arrow(COL_LEFT + CARD_W, ROW2_Y + CARD_H//2, COL_RIGHT, ROW2_Y + CARD_H//2, color="#40c057", strokeWidth=2))
# REPLANEJAR volta pra EXECUTAR (seta curva indicando loop)
elements.append(arrow(COL_RIGHT + CARD_W - 20, ROW2_Y, COL_RIGHT + CARD_W - 20, ROW1_Y + CARD_H, color="#7950f2", strokeWidth=2))

# ── Anti-loop no rodapé ──
elements.append(text(COL_LEFT, ROW2_Y + CARD_H + 25, "Anti-loop: max_etapas=12 | sem_progresso=3 | limite_tempo=120s | budget cap | human-in-the-loop pra rollback", fontSize=11, strokeColor="#868e96"))

# ── Label de arquivo ──
elements.append(text(380, ROW2_Y + CARD_H + 55, "conteudos_ia/OUTROS/loop-agente-monitor.excalidraw", fontSize=10, strokeColor="#adb5bd"))

# ── Monta JSON ──
output = {
    "type": "excalidraw",
    "version": 2,
    "source": "https://excalidraw.com",
    "elements": elements,
    "appState": {
        "viewBackgroundColor": "#ffffff",
        "gridSize": None,
        "scrollX": 0,
        "scrollY": 0,
        "zoom": {"value": 1},
        "activeTool": {"type": "selection", "customType": None, "locked": False, "lastActiveTool": None}
    },
    "files": {}
}

with open("/home/estrazulas/git/docs_capacitacao_ia/conteudos_ia/OUTROS/loop-agente-monitor.excalidraw", "w") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print("✅ Salvo em conteudos_ia/OUTROS/loop-agente-monitor.excalidraw")
print(f"   {len(elements)} elementos")
