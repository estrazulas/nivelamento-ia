#!/usr/bin/env python3
"""Gera modulo-05-mcp-agentes.excalidraw — 5 slides, 3 rows."""

import json, uuid

def mid(): return "m" + uuid.uuid4().hex[:16]

def rect(x, y, w, h, bg, stroke="#adb5bd", sw=1):
    return {"id": mid(), "type": "rectangle", "x": x, "y": y, "width": w, "height": h,
            "backgroundColor": bg, "strokeColor": stroke, "strokeWidth": sw,
            "angle": 0, "opacity": 100, "roughness": 0, "roundness": None,
            "boundElements": None, "groupIds": [], "frameId": None,
            "isDeleted": False, "locked": False, "seed": 1, "versionNonce": 1, "updated": 1, "fillStyle": "solid"}

def text(x, y, content, fs, color="#1e1e1e", w=None, h=None):
    lines = content.split("\n")
    max_line = max(len(l) for l in lines)
    if w is None: w = max_line * fs * 0.58
    if h is None: h = len(lines) * fs * 1.35
    return {"id": mid(), "type": "text", "x": x, "y": y, "width": w, "height": h,
            "text": content, "fontSize": fs, "strokeColor": color,
            "fontFamily": 2, "textAlign": "left", "verticalAlign": "top", "autoResize": True, "lineHeight": 1.25,
            "angle": 0, "opacity": 100, "roughness": 0, "roundness": None,
            "boundElements": None, "groupIds": [], "frameId": None,
            "isDeleted": False, "locked": False, "seed": 1, "versionNonce": 1, "updated": 1,
            "backgroundColor": "transparent", "fillStyle": "solid"}

def arrow(x, y, w, h, color="#adb5bd", sw=1):
    return {"id": mid(), "type": "arrow", "x": x, "y": y, "width": w, "height": h,
            "strokeColor": color, "strokeWidth": sw,
            "startArrowhead": "arrow", "endArrowhead": "arrow" if w > 0 or h > 0 else None,
            "startBinding": None, "endBinding": None, "lastCommittedPoint": None, "points": [[0, 0], [w, h]],
            "angle": 0, "opacity": 100, "roughness": 0, "roundness": None,
            "boundElements": None, "groupIds": [], "frameId": None,
            "isDeleted": False, "locked": False, "seed": 1, "versionNonce": 1, "updated": 1,
            "backgroundColor": "transparent", "fillStyle": "solid"}

def slide_bg(x, y, h=620): return rect(x, y, 960, h, "#f8f9fa", "#dee2e6", 1)

elements = []
H1, H2, H3 = 620, 660, 620
R1, R2, R3 = 20, 740, 1480

# ============ ROW 1: 5.1 MCP + 5.2 Arquitetura ============

# --- Slide 5.1: MCP — A Tomada Universal (left) ---
elements.append(slide_bg(20, R1, H1))
elements.append(text(60, R1+20, "MCP: A Tomada Universal", 28))
elements.append(text(60, R1+58, "Model Context Protocol (Anthropic) — o padrão que todo mundo adotou em 2025", 14, "#868e96"))

elements.append(rect(40, R1+100, 430, 460, "#fff5f5", "#ffc9c9", 1))
elements.append(text(60, R1+115, "❌ Antes do MCP", 18, "#e03131"))
elements.append(text(60, R1+150, "Cada ferramenta + modelo = código\ncustomizado de integração.\n\nConectar IA no banco de dados,\nJira e GitHub: um pesadelo.\n\nM × N integrações para\nM ferramentas × N modelos.", 12, "#1e1e1e"))

elements.append(rect(510, R1+100, 430, 460, "#f0fff4", "#b2f2bb", 1))
elements.append(text(530, R1+115, "✅ Depois do MCP", 18, "#2f9e44"))
elements.append(text(530, R1+150, "Qualquer ferramenta que segue o\npadrão conecta em qualquer IA\nque também segue.\n\nHoje é padrão da indústria:\nCursor, Claude Code, Copilot,\nCline, Continue, Windsurf.\n\nConfigura 1x, toda IA descobre\ne usa. Protocolo gerencia\nautenticação e descoberta.", 12, "#1e1e1e"))

elements.append(rect(40, R1+580, 900, 40, "#f0fff4", "#b2f2bb", 2))
elements.append(text(60, R1+590, "🔌 Analogia: Antes do MCP = cada eletrodoméstico com sua tomada. Depois = tomada universal de 3 pinos.", 13, "#2f9e44"))
elements.append(text(480, R1+622, "MÓDULO 5 — SLIDE 1", 12, "#868e96"))

# --- Slide 5.2: Arquitetura Server/Client (right) ---
elements.append(slide_bg(1100, R1, H1))
elements.append(text(1160, R1+20, "Arquitetura MCP Server/Client", 28))
elements.append(text(1160, R1+58, "O ecossistema tem dois lados: quem expõe capacidades e quem as consome", 14, "#868e96"))

# 3 nodes
nodes = [
    ("IA (Modelo)", 'Decide: "preciso\nbuscar a task\nCAN-123"', "#4c6ef5", 1140),
    ("MCP Client", "Descobre capacidades.\nGerencia chamadas.\nEx: Claude Code,\nCursor, Copilot.", "#40c057", 1440),
    ("MCP Server", "Expõe capacidades.\nTraduz para API\nexterna.\nEx: Jira, GitHub,\nBD, Confluence.", "#fd7e14", 1740),
]
for title, desc, color, x in nodes:
    elements.append(rect(x, R1+110, 260, 200, "#ffffff", color, 2))
    elements.append(text(x+10, R1+120, title, 16, color))
    elements.append(text(x+10, R1+155, desc, 12, "#1e1e1e"))

# Arrows between nodes
elements.append(text(1405, R1+195, "→", 18, "#adb5bd"))
elements.append(text(1705, R1+195, "→", 18, "#adb5bd"))

# Return flow
elements.append(rect(1140, R1+340, 860, 60, "#f0fff4", "#b2f2bb", 1))
elements.append(text(1160, R1+352, "↩ Resultado volta: API do Jira → MCP Server → MCP Client → IA → Resposta contextualizada para o usuário", 13, "#2f9e44"))

# Analogy
elements.append(rect(1140, R1+420, 860, 100, "#ffffff", "#adb5bd", 1))
elements.append(text(1160, R1+432, "🍽️ Analogia do Restaurante:", 15, "#1e1e1e"))
elements.append(text(1160, R1+460, "MCP Server = Garçom (traduz seu pedido pra cozinha)  |  MCP Client = Maître (sabe quem está disponível)  |  IA = Cliente (decide o que quer)", 13, "#495057"))

# MCP vs Skill vs API preview
elements.append(rect(1140, R1+540, 860, 60, "#f3f0ff", "#7950f2", 2))
elements.append(text(1160, R1+552, "📋 Próximos slides: MCP vs Skill vs API Direta — cada um tem seu papel na arquitetura de contexto.", 13, "#7950f2"))

elements.append(text(1560, R1+622, "MÓDULO 5 — SLIDE 2", 12, "#868e96"))
elements.append(text(800, R1+H1+10, "Arraste com o mouse para a direita → Slide 2", 14, "#495057"))
elements.append(arrow(1050, R1+H1+15, 50, 0, "#adb5bd", 1))

# ============ ROW 2: 5.3 Agentes + 5.4 Loop ============

# --- Slide 5.3: Agentes — Os 4 Componentes (left) ---
elements.append(slide_bg(20, R2, H2))
elements.append(text(60, R2+20, "Agentes de IA: Além do Chat", 28))
elements.append(text(60, R2+58, "Chat responde. Agente planeja, executa e verifica — de forma autônoma.", 14, "#868e96"))

# Top banner: Chat vs Agente
elements.append(rect(40, R2+100, 900, 70, "#f0fff4", "#b2f2bb", 2))
elements.append(text(60, R2+110, "💬 Chat: \"Qual a previsão do tempo?\" → Resposta. Fim.", 13, "#2f9e44"))
elements.append(text(60, R2+138, "🤖 Agente: \"Me avisa se chover amanhã e remarca minhas reuniões externas\" → Planeja → Consulta previsão → Verifica agenda → Remarca → Notifica.", 13, "#1e1e1e"))

# 2x2 grid
comps = [
    ("1. 🧠 Cérebro", "A LLM que raciocina\ne decide os passos.\nEx: GPT-4o, Claude,\nGemini.", "#4c6ef5", "#e7f5ff"),
    ("2. 🖐️ Mãos", "Ferramentas que\nexecutam ações.\nMCPs e APIs.\nEx: MCP GitHub\n(criar PR), MCP\nJira (atualizar task).", "#40c057", "#f0fff4"),
    ("3. 📝 Memória", "Contexto da conversa\n+ banco externo para\npersistência.\nEx: STATE.md, vector\nDB, chat history.", "#fd7e14", "#fff4e6"),
    ("4. 🛡️ Guardrails", "Regras de segurança\ne limites.\n'Nunca delete sem\nconfirmar', 'Não faça\ndeploy sexta-feira'.", "#7950f2", "#f3f0ff"),
]
for i, (title, desc, color, bg) in enumerate(comps):
    col, row = i % 2, i // 2
    x, y = 40 + col*460, R2+190 + row*220
    elements.append(rect(x, y, 440, 200, bg, color, 2))
    elements.append(text(x+15, y+15, title, 17, color))
    elements.append(text(x+15, y+50, desc, 12, "#1e1e1e"))

elements.append(rect(40, R2+630, 900, 30, "#ffffff", "#adb5bd", 1))
elements.append(text(60, R2+636, "💡 Em IDEs modernas, o modo agente significa: lê código → planeja mudanças → edita arquivos → roda testes → itera. Tudo de uma vez.", 12, "#495057"))
elements.append(text(480, R2+662, "MÓDULO 5 — SLIDE 3", 12, "#868e96"))

# --- Slide 5.4: Loop do Agente (right) ---
elements.append(slide_bg(1100, R2, H2))
elements.append(text(1160, R2+20, "O Loop do Agente: Planejar-Executar-Observar-Replanejar", 26))
elements.append(text(1160, R2+58, "Um ciclo PDCA executado por IA em segundos, não em semanas", 14, "#868e96"))

# 4 phases in diamond layout
phases = [
    ("1. PLANEJAR", "A LLM analisa o\nobjetivo e define\nos passos.", "#4c6ef5", 1570, R2+100),
    ("2. EXECUTAR", "Chama as ferramentas\n(MCPs) para cada\npasso do plano.", "#40c057", 1840, R2+270),
    ("3. OBSERVAR", "Coleta e analisa\nos resultados de\ncada ação executada.", "#fd7e14", 1570, R2+440),
    ("4. REPLANEJAR", "Se algo falhou,\najusta o plano e\ncontinua iterando.", "#7950f2", 1280, R2+270),
]
for title, desc, color, x, y in phases:
    elements.append(rect(x, y, 260, 130, "#ffffff", color, 2))
    elements.append(text(x+10, y+10, title, 15, color))
    elements.append(text(x+10, y+42, desc, 11, "#1e1e1e"))

# Center: objetivo
elements.append(rect(1550, R2+360, 220, 55, "#f0fff4", "#b2f2bb", 2))
elements.append(text(1565, R2+370, "Objetivo\natingido?", 14, "#2f9e44", None, None))

# Explanation below
elements.append(rect(1140, R2+600, 900, 50, "#ffffff", "#adb5bd", 1))
elements.append(text(1160, R2+610, "🔄 O loop roda até o objetivo ser atingido ou um guardrail interromper. Entender esse ciclo permite criar agentes com fallbacks inteligentes.", 12, "#495057"))
elements.append(text(1560, R2+662, "MÓDULO 5 — SLIDE 4", 12, "#868e96"))

elements.append(text(820, R2+H2+10, "Arraste para baixo para ver o Slide 5", 13, "#495057"))
elements.append(arrow(960, R2+H2+15, 0, 30, "#adb5bd", 1))

# ============ ROW 3: 5.5 MCP vs Skill vs API + Resumo ============

elements.append(slide_bg(20, R3, H3))
elements.append(text(60, R3+20, "MCP vs Skill vs API Direta + Resumo do Módulo", 27))
elements.append(text(60, R3+58, "Dado mutável → MCP. Conhecimento estável → Skill. Integração pontual → API direta.", 14, "#868e96"))

# 3 columns
cols = [
    ("🔌 MCP", "Dados que MUDAM.\nStatus de tasks,\npáginas do Confluence,\nPRs no GitHub.", "Protocolo gerencia\nautenticação.\nIdeal para sistemas\ncorporativos.", "Porta giratória\npro mundo externo.", "#4c6ef5", "#e7f5ff"),
    ("📋 Skill", "Conhecimento ESTÁVEL.\nComo criar teste e2e,\ntemplate de tarefa,\nconvenção de commit.", "Encapsula conhecimento,\nnão dados.\nPortátil e reutilizável\nentre times.", "Manual de instruções\nna gaveta.", "#40c057", "#f0fff4"),
    ("🔧 API Direta", "Integrações pontuais\nou quando não existe\nMCP Server disponível.", "Mais trabalho manual,\nmais controle fino.\nBypass do protocolo.", "Construir uma\nporta nova.", "#fd7e14", "#fff4e6"),
]
for i, (title, desc, when, analogy, color, bg) in enumerate(cols):
    x = 40 + i*310
    elements.append(rect(x, R3+100, 290, 320, bg, color, 2))
    elements.append(text(x+15, R3+115, title, 18, color))
    elements.append(text(x+15, R3+155, "O quê:", 13, "#1e1e1e"))
    elements.append(text(x+15, R3+175, desc, 11, "#1e1e1e"))
    elements.append(text(x+15, R3+270, "Quando:", 13, "#1e1e1e"))
    elements.append(text(x+15, R3+290, when, 11, "#495057"))
    elements.append(text(x+15, R3+370, f"Analogia: {analogy}", 11, "#868e96"))

# Warning
elements.append(rect(40, R3+440, 920, 50, "#fff5f5", "#ffc9c9", 1))
elements.append(text(60, R3+450, "⚠️ Erro comum: Times misturam os conceitos e acabam com MCPs pesados ou skills que deveriam ser MCPs. A regra é clara: dado mutável → MCP; conhecimento estável → Skill.", 12, "#e03131"))

# Module summary
elements.append(rect(40, R3+510, 920, 100, "#f0fff4", "#b2f2bb", 2))
elements.append(text(60, R3+522, "📋 Resumo Módulo 5:", 15, "#2f9e44"))
elements.append(text(60, R3+548, "MCP = tomada universal para ferramentas externas (dados que mudam)  |  Agente = cérebro + mãos + memória + guardrails  |  Loop = planejar → executar → observar → replanejar  |  Skill ≠ MCP ≠ API — cada um tem seu papel.", 12, "#1e1e1e"))

elements.append(text(480, R3+622, "MÓDULO 5 — SLIDE 5", 12, "#868e96"))

# ============ Assemble ============
doc = {"type": "excalidraw", "version": 2, "source": "https://marketplace.visualstudio.com/items?itemName=pomdtr.excalidraw-editor",
       "elements": elements,
       "appState": {"viewBackgroundColor": "#ffffff", "gridSize": None, "scrollX": 0, "scrollY": 0, "zoom": {"value": 1},
                    "viewModeEnabled": False, "zenModeEnabled": False, "objectsSnapModeEnabled": False,
                    "activeTool": {"type": "selection", "customType": None, "locked": False, "lastActiveTool": None}},
       "files": {}}

out = "/home/estrazulas/git/docs_capacitacao_ia/excalidraw/modulo-05-mcp-agentes.excalidraw"
with open(out, "w") as f: json.dump(doc, f, indent=2, ensure_ascii=False)
print(f"✅ {out}")
print(f"   {len(elements)} elementos em 5 slides")
