#!/usr/bin/env python3
"""Gera modulo-07-sdd-ferramentas.excalidraw — 6 slides, 3 rows."""

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
H1, H2, H3 = 620, 660, 660
R1, R2, R3 = 20, 740, 1480

# ============ ROW 1: 7.1 Prompt Direto + 7.2 4 Fases SDD ============

# --- Slide 7.1: Por que Prompt Direto Falha (left) ---
elements.append(slide_bg(20, R1, H1))
elements.append(text(60, R1+20, "Por que Prompt Direto Falha em Projetos Grandes", 28))
elements.append(text(60, R1+58, 'Jogar um PRD gigante num prompt e pedir "implementa isso" = plano raso que perde contexto', 14, "#868e96"))

# Prompt Direto
elements.append(rect(40, R1+100, 430, 450, "#fff5f5", "#ffc9c9", 1))
elements.append(text(60, R1+115, "❌ Prompt Direto com PRD Gigante", 17, "#e03131"))
pd = [
    "O que acontece:",
    "• A IA prioriza o início",
    "• Ignora o meio",
    "• Alucina no final",
    "",
    "É o mesmo problema da janela",
    "de contexto cheia, aplicado ao",
    "desenvolvimento de software.",
    "",
    "50 requisitos num prompt só →",
    "resultado raso e incoerente.",
    "",
    "Analogia:",
    'Pedir pra um dev implementar 50',
    "features sem dividir em tasks,",
    "sem critério de aceite, sem",
    "definição de pronto.",
    "",
    "Resultado: frustração, retrabalho,",
    '"IA não presta pra projeto grande".'
]
elements.append(text(60, R1+148, "\n".join(pd), 12, "#1e1e1e"))

# SDD approach
elements.append(rect(510, R1+100, 430, 450, "#f0fff4", "#b2f2bb", 1))
elements.append(text(530, R1+115, "✅ SDD (Spec-Driven Development)", 17, "#2f9e44"))
sdd = [
    "Resolve o problema quebrando em",
    "fases com contexto controlado.",
    "",
    "Cada fase tem contexto reduzido",
    "e focado. A IA não precisa",
    '"lembrar" de tudo de uma vez.',
    "",
    "Fases:",
    "1. Specify  → O QUÊ",
    "2. Design   → COMO",
    "3. Tasks    → QUANDO/ONDE",
    "4. Execute  → FAZER",
    "",
    "SDD não é burocracia — é",
    "estratégia pra contornar as",
    "limitações das LLMs.",
    "",
    "Analogia:",
    "Construção civil — ninguém",
    "constrói um prédio sem planta."
]
elements.append(text(530, R1+148, "\n".join(sdd), 12, "#1e1e1e"))

elements.append(rect(40, R1+570, 900, 40, "#f0fff4", "#b2f2bb", 2))
elements.append(text(60, R1+580, "🔑 SDD resolve o maior problema do desenvolvimento com IA: contexto sobrecarregado → perda de coerência → resultado ruim.", 13, "#2f9e44"))
elements.append(text(480, R1+622, "MÓDULO 7 — SLIDE 1", 12, "#868e96"))

# --- Slide 7.2: SDD — As 4 Fases (right) ---
elements.append(slide_bg(1100, R1, H1))
elements.append(text(1160, R1+20, "SDD: As 4 Fases", 28))
elements.append(text(1160, R1+58, "Da especificação à execução paralela com contexto limpo — cada fase alimenta a próxima", 14, "#868e96"))

fases = [
    ("1. SPECIFY", "Definir problema,\nmetas, user stories,\nfora de escopo.\nAlinhamento antes\nde tudo.", "spec.md", "#4c6ef5", 1140),
    ("2. DESIGN", "Diagramas, arquitetura,\ndecisões técnicas.\n(Opcional para\nprojetos pequenos)", "design.md", "#40c057", 1370),
    ("3. TASKS", "Quebrar em tarefas\nautossuficientes.\nCada task: o quê,\nonde, pré-requisitos,\ndefinition of done.", "tasks.md", "#fd7e14", 1600),
    ("4. EXECUTE", "Sub-agents executando\nem paralelo, cada um\ncom contexto limpo\ne isolado.", "STATE.md", "#7950f2", 1830),
]
for title, desc, artifact, color, x in fases:
    elements.append(rect(x, R1+110, 210, 280, "#ffffff", color, 2))
    elements.append(text(x+10, R1+120, title, 16, color))
    elements.append(text(x+10, R1+152, desc, 11, "#1e1e1e"))
    elements.append(text(x+10, R1+340, f"📄 {artifact}", 11, "#868e96"))

# Arrows between phases
for x in [1355, 1585, 1815]:
    elements.append(text(x, R1+240, "→", 16, "#adb5bd"))

# Bottom
elements.append(rect(1140, R1+420, 900, 100, "#ffffff", "#adb5bd", 1))
elements.append(text(1160, R1+432, "🏗️ Analogia da Construção Civil:", 15, "#1e1e1e"))
elements.append(text(1160, R1+460, "Specify = \"Quero 3 quartos\"  |  Design = Planta baixa  |  Tasks = Cronograma  |  Execute = Pedreiros em paralelo", 13, "#495057"))
elements.append(text(1160, R1+490, "Cada fase tem contexto progressivamente refinado, nunca sobrecarregado. A IA só precisa do contexto da fase atual.", 12, "#495057"))

elements.append(rect(1140, R1+540, 900, 60, "#f0fff4", "#b2f2bb", 2))
elements.append(text(1160, R1+552, "💡 O SDD é o MACRO-ciclo. O RPI (próximo slide) é o MICRO-ciclo dentro de cada fase.", 13, "#2f9e44"))
elements.append(text(1560, R1+622, "MÓDULO 7 — SLIDE 2", 12, "#868e96"))

elements.append(text(800, R1+H1+10, "Arraste com o mouse para a direita → Slide 2", 14, "#495057"))
elements.append(arrow(1050, R1+H1+15, 50, 0, "#adb5bd", 1))

# ============ ROW 2: 7.3 STATE.md+Doc + 7.4 RPI ============

# --- Slide 7.3: STATE.md e Documentação (left) ---
elements.append(slide_bg(20, R2, H2))
elements.append(text(60, R2+20, "STATE.md e Documentação como Combustível", 28))
elements.append(text(60, R2+58, "Duas práticas que transformam a experiência de desenvolver com IA", 14, "#868e96"))

# STATE.md card
elements.append(rect(40, R2+100, 440, 520, "#e7f5ff", "#4c6ef5", 2))
elements.append(text(60, R2+115, "📝 STATE.md: Memória Entre Sessões", 17, "#4c6ef5"))
state = [
    "O STATE.md guarda:",
    "• Decisões tomadas e POR QUÊ",
    "• Tasks concluídas e pendentes",
    "• Blockers e dependências",
    "• Aprendizados e descobertas",
    "",
    "Quando você volta (5 minutos ou",
    "5 dias depois), o agente lê o",
    "STATE.md e continua de onde parou.",
    "",
    "Problema que resolve:",
    "O MAIOR problema de desenvolver",
    "com IA: perda de contexto entre",
    "sessões. Sem STATE.md, cada nova",
    "conversa começa do zero.",
    "",
    "📖 Analogia:",
    "Diário de obra. O pedreiro do turno",
    "seguinte lê e sabe exatamente o",
    "que foi feito, o que falta e quais",
    "decisões foram tomadas."
]
elements.append(text(60, R2+148, "\n".join(state), 12, "#1e1e1e"))

# Documentação card
elements.append(rect(510, R2+100, 440, 520, "#f0fff4", "#b2f2bb", 2))
elements.append(text(530, R2+115, "📚 Documentação como Combustível", 17, "#2f9e44"))
doc_content = [
    "Na era da IA, documentação deixou de",
    "ser burocracia e virou COMBUSTÍVEL.",
    "",
    "Quanto melhor documentado seu",
    "projeto, mais rápido e preciso o",
    "agente trabalha.",
    "",
    "Dica prática:",
    "A cada feature nova, peça pra IA",
    "atualizar as guidelines do projeto.",
    "A documentação cresce organicamente",
    "como parte do fluxo de desenvolvimento.",
    "",
    "Inversão de incentivo:",
    "Documentar NÃO é mais \"perda de",
    "tempo que o próximo dev aproveita\".",
    "É investimento que volta IMEDIATA-",
    "MENTE na qualidade do código que",
    "a IA gera PRA VOCÊ, AGORA.",
    "",
    "⛽ Analogia:",
    "Documentação = gasolina do motor",
    "de IA. Sem gasolina, o motor rateia.",
    "Com gasolina de qualidade, roda liso."
]
elements.append(text(530, R2+148, "\n".join(doc_content), 12, "#1e1e1e"))

elements.append(text(480, R2+662, "MÓDULO 7 — SLIDE 3", 12, "#868e96"))

# --- Slide 7.4: RPI — Research-Plan-Implement (right) ---
elements.append(slide_bg(1100, R2, H2))
elements.append(text(1160, R2+20, "RPI: Research → Plan → Implement", 28))
elements.append(text(1160, R2+58, "O micro-ciclo dentro de cada fase do SDD. Método científico no desenvolvimento.", 14, "#868e96"))

# 3 nodes
rpi = [
    ("🔍 RESEARCH", "Abrir o leque — pesquisar\nabordagens, bibliotecas,\npatterns. Fase exploratória.\n\nPergunte: \"Quais as opções?\nO que a comunidade usa?\nQuais os trade-offs?\"", "#4c6ef5", 1140),
    ("📋 PLAN", "Salvar o plano em markdown\n— documentar decisão e\nracional.\n\nEstado: \"Escolhemos X porque\nY. Alternativas consideradas:\nZ. Trade-off: A vs B.\"", "#40c057", 1440),
    ("🔧 IMPLEMENT", "Executar as tasks conforme\no plano. Cada task alimenta\no STATE.md.\n\nSe algo novo surgir durante\na implementação → volta\npro Research.", "#fd7e14", 1740),
]
for title, desc, color, x in rpi:
    elements.append(rect(x, R2+110, 260, 280, "#ffffff", color, 2))
    elements.append(text(x+10, R2+120, title, 16, color))
    elements.append(text(x+10, R2+155, desc, 11, "#1e1e1e"))

# Arrows
for x in [1405, 1705]:
    elements.append(text(x, R2+240, "→", 16, "#adb5bd"))

# Feedback loop
elements.append(text(1880, R2+260, "↩", 14, "#7950f2"))

# Why RPI
elements.append(rect(1140, R2+420, 900, 110, "#f3f0ff", "#7950f2", 2))
elements.append(text(1160, R2+432, "🎯 Por que RPI importa:", 16, "#7950f2"))
elements.append(text(1160, R2+462, 'Evita o "vibe coding" — codar no feeling sem planejar. Cada decisão tem racional documentado que pode ser revisado depois.', 13, "#1e1e1e"))
elements.append(text(1160, R2+490, "RPI é o micro-ciclo dentro de cada fase. SDD é o macro-ciclo do projeto. Juntos = disciplina de desenvolvimento com IA.", 13, "#1e1e1e"))

# Bottom
elements.append(rect(1140, R2+550, 900, 90, "#f0fff4", "#b2f2bb", 1))
elements.append(text(1160, R2+562, "🔄 O ciclo completo: SDD define as 4 fases do projeto. Em cada fase, você aplica RPI.", 13, "#2f9e44"))
elements.append(text(1160, R2+590, "Specify (RPI) → Design (RPI) → Tasks (RPI) → Execute (RPI). Cada iteração deixa rastro no STATE.md.", 12, "#1e1e1e"))
elements.append(text(1560, R2+662, "MÓDULO 7 — SLIDE 4", 12, "#868e96"))

elements.append(text(820, R2+H2+10, "Arraste para baixo para ver os Slides 5 e 6", 13, "#495057"))
elements.append(arrow(960, R2+H2+15, 0, 30, "#adb5bd", 1))

# ============ ROW 3: 7.5 Ferramentas + 7.6 Workshop ============

# --- Slide 7.5: Ferramentas (left) ---
elements.append(slide_bg(20, R3, H3))
elements.append(text(60, R3+20, "Ferramentas: O Que Usar e Quando", 28))
elements.append(text(60, R3+58, "Não existe ferramenta universal melhor. Existe a certa pro seu contexto.", 14, "#868e96"))

tools = [
    ("Cursor", "Multi-agentes, plan mode,\nskills e MCPs.\nExperiência mais completa.", "SUV completo", "#4c6ef5", 40, 110),
    ("GitHub Copilot", "Funciona em qualquer IDE,\necosystema GitHub.\nIntegração nativa.", "Integrado de fábrica", "#40c057", 510, 110),
    ("Claude Code", "Terminal, modelos Claude\nde alta qualidade.\nComando 'onboard' nativo.", "Moto esportiva", "#7950f2", 40, 300),
    ("Windsurf", "Browser interno embutido.\nIdeal para devs frontend\ne design iterativo.", "Conversível", "#fd7e14", 510, 300),
    ("Cline / Roo Code", "Extensões VS Code\ngratuitas com MCP.\nOrçamento zero.", "Carro popular", "#e64980", 40, 490),
    ("Continue / Aider", "Open-source, foco em\nplanejamento.\nControle total.", "Kit turbo", "#40c057", 510, 490),
]
for name, desc, analogy, color, x, y in tools:
    elements.append(rect(x, R3+y, 450, 170, "#ffffff", color, 2))
    elements.append(text(x+15, R3+y+12, name, 18, color))
    elements.append(text(x+15, R3+y+45, desc, 12, "#1e1e1e"))
    elements.append(text(x+15, R3+y+120, f"🚗 {analogy}", 11, "#868e96"))

# Selection criteria
elements.append(rect(40, R3+680, 900, 60, "#f0fff4", "#b2f2bb", 1))
elements.append(text(60, R3+692, "🎯 Critérios: Ecossistema (GitHub? → Copilot) | Autonomia (modo agente? → Cursor/Claude Code) | Custo (zero? → Cline/Continue) | Stack (frontend? → Windsurf)", 12, "#2f9e44"))

elements.append(text(480, R3+762, "MÓDULO 7 — SLIDE 5", 12, "#868e96"))

# --- Slide 7.6: Workshop Prático + Resumo (right) ---
elements.append(slide_bg(1100, R3, H3))
elements.append(text(1160, R3+20, "Workshop Prático: Execute as 4 Fases do SDD", 27))
elements.append(text(1160, R3+56, "Cada participante (ou dupla) recebe um requisito real e aplica o ciclo completo", 14, "#868e96"))

ws_fases = [
    ("1. SPECIFY", "10 min", "Escrever spec com\nuser stories, metas\ne fora de escopo.\nFerramenta: IA +\ntemplate spec.md", "#4c6ef5", 1140),
    ("2. DESIGN", "10 min", "Esboçar arquitetura\ne decisões técnicas.\nFerramenta: IA +\ndiagramas.", "#40c057", 1380),
    ("3. TASKS", "10 min", "Quebrar em 3-5 tasks\ncom definition of\ndone, pré-requisitos\ne arquivos.", "#fd7e14", 1620),
    ("4. EXECUTE", "15 min", "Simular execução\ncom sub-agents.\nRodar em paralelo\ncom contexto limpo.", "#7950f2", 1860),
]
for title, time, desc, color, x in ws_fases:
    elements.append(rect(x, R3+100, 220, 250, "#ffffff", color, 2))
    elements.append(text(x+10, R3+110, title, 15, color))
    elements.append(text(x+10, R3+142, f"⏱ {time}", 14, "#868e96"))
    elements.append(text(x+10, R3+170, desc, 11, "#1e1e1e"))

# Presentation
elements.append(rect(1140, R3+370, 900, 45, "#f0fff4", "#b2f2bb", 2))
elements.append(text(1160, R3+382, "🎤 5. APRESENTAÇÃO (5 min): Cada dupla apresenta o STATE.md final. Discussão coletiva: o que funcionou, o que travou.", 13, "#2f9e44"))

# Module 7 summary
elements.append(rect(1140, R3+435, 900, 290, "#f0fff4", "#b2f2bb", 2))
elements.append(text(1160, R3+450, "📋 Resumo do Módulo 7 — e do Workshop:", 17, "#2f9e44"))
final = [
    "1. Prompt direto falha em projetos grandes — o contexto sobrecarrega e a IA perde coerência.",
    "2. SDD resolve com 4 fases: Specify → Design → Tasks → Execute. Cada fase = contexto controlado.",
    "3. STATE.md mantém memória entre sessões — o agente continua de onde parou, mesmo após dias.",
    "4. Documentação é combustível da IA — investimento que volta IMEDIATAMENTE em qualidade.",
    "5. RPI (Research → Plan → Implement) é o micro-ciclo dentro de cada fase do SDD.",
    "6. Ferramenta certa para o contexto certo — não existe bala de prata, existe a melhor escolha.",
    "",
    "🎯 Regra Final: ESPECIFICAR antes de codar. PLANEJAR antes de executar. DOCUMENTAR enquanto faz."
]
elements.append(text(1160, R3+483, "\n".join(final), 12, "#1e1e1e"))

elements.append(text(1560, R3+762, "MÓDULO 7 — SLIDE 6", 12, "#868e96"))

# ============ Assemble ============
doc = {"type": "excalidraw", "version": 2, "source": "https://marketplace.visualstudio.com/items?itemName=pomdtr.excalidraw-editor",
       "elements": elements,
       "appState": {"viewBackgroundColor": "#ffffff", "gridSize": None, "scrollX": 0, "scrollY": 0, "zoom": {"value": 1},
                    "viewModeEnabled": False, "zenModeEnabled": False, "objectsSnapModeEnabled": False,
                    "activeTool": {"type": "selection", "customType": None, "locked": False, "lastActiveTool": None}},
       "files": {}}

out = "/home/estrazulas/git/docs_capacitacao_ia/excalidraw/modulo-07-sdd-ferramentas.excalidraw"
with open(out, "w") as f: json.dump(doc, f, indent=2, ensure_ascii=False)
print(f"✅ {out}")
print(f"   {len(elements)} elementos em 6 slides")
