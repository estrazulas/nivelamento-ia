#!/usr/bin/env python3
"""Gera modulo-06-arquitetura-contexto.excalidraw — 6 slides, 3 rows."""

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

# ============ ROW 1: 6.1 Evolução + 6.2 4 Pilares ============

# --- Slide 6.1: Evolução 2023-2026 (left) ---
elements.append(slide_bg(20, R1, H1))
elements.append(text(60, R1+20, "A Evolução 2023-2026: De Tudo no Prompt às Skills Modulares", 26))
elements.append(text(60, R1+56, "Se você está começando agora, pode pular direto pra Fase 3", 14, "#868e96"))

fases = [
    ("2023-2024", "TUDO NO PROMPT", "Documentação, regras, MCPs,\nworkflows — num prompt só.", "Contexto gigante, tokens\ncaros, alucinações.", "Todos os ingredientes\nna panela de uma vez.", "#e03131", "#fff5f5"),
    ("Início 2025", "SUPER-AGENTES", "Agentes customizados de\n3000+ linhas que faziam\ntudo sozinhos.", "Cada conversa já começava\ncom metade do contexto\nocupado. Caro e lento.", "Robô gigante que gasta\nmetade da energia\nsó pra ligar.", "#fd7e14", "#fff4e6"),
    ("Meados 2025+", "SKILLS MODULARES", "Capacidades pequenas,\nfocadas, carregadas\nsob demanda.", "Contexto limpo, custo\nbaixo, respostas\nprecisas e rápidas.", "Mise en place —\ncada ingrediente\nno seu potinho.", "#40c057", "#f0fff4"),
]
for i, (period, title, desc, result, analogy, color, bg) in enumerate(fases):
    x = 40 + i*310
    elements.append(rect(x, R1+105, 290, 380, bg, color, 2))
    elements.append(text(x+15, R1+118, period, 13, "#868e96"))
    elements.append(text(x+15, R1+142, title, 17, color))
    elements.append(text(x+15, R1+185, "O que era:", 13, "#1e1e1e"))
    elements.append(text(x+15, R1+205, desc, 11, "#1e1e1e"))
    elements.append(text(x+15, R1+300, "Resultado:", 13, "#1e1e1e"))
    elements.append(text(x+15, R1+320, result, 11, "#495057"))
    elements.append(text(x+15, R1+400, f"Analogia: {analogy}", 10, "#868e96"))
    if i < 2:
        elements.append(text(x+293, R1+280, "→", 16, "#adb5bd"))

elements.append(rect(40, R1+500, 900, 100, "#f0fff4", "#b2f2bb", 2))
elements.append(text(60, R1+515, "💡 Lição: Não crie agentes enormes. Crie skills pequenas e modulares.", 15, "#2f9e44"))
elements.append(text(60, R1+545, "Cada skill faz UMA coisa bem. O agente carrega só o que precisa, quando precisa. Contexto limpo = respostas melhores = custo menor.", 13, "#1e1e1e"))
elements.append(text(480, R1+622, "MÓDULO 6 — SLIDE 1", 12, "#868e96"))

# --- Slide 6.2: Os 4 Pilares (right) ---
elements.append(slide_bg(1100, R1, H1))
elements.append(text(1160, R1+20, "Os 4 Pilares da Arquitetura de Contexto", 28))
elements.append(text(1160, R1+58, "Pensa na arquitetura de uma casa. Cada pilar tem seu papel específico.", 14, "#868e96"))

pilares = [
    ("1. 📐 Rules / Agents.md", "A PLANTA BAIXA", "O QUE é o projeto — estrutura,\nconvenções, arquitetura.\nMáximo 200 linhas.\nSó alto nível + ponteiros\npra docs detalhadas.", "Planta baixa da casa.", "#4c6ef5", "#e7f5ff"),
    ("2. 🛠️ Skills", "COMODOS FUNCIONAIS", "COMO fazer X — capacidades\nreutilizáveis e independentes.\nPortáteis: cria uma vez, usa no\nCursor, Claude Code, Copilot.\nCompartilhável entre times.", "Ferramentas na caixa.", "#40c057", "#f0fff4"),
    ("3. 🚪 MCPs", "PORTAS PRO MUNDO", "ONDE buscar/alterar dados —\nJira, GitHub, bancos.\nGerencia autenticação\ntransparente.\nSempre conectados.", "Portas e janelas.", "#fd7e14", "#fff4e6"),
    ("4. 👷 Sub-agents", "TRABALHADORES", "FAÇA isso em paralelo sem\npoluir meu contexto.\nNÃO crie customizados —\nferramentas modernas\ngerenciam automaticamente.", "Pedreiros em\ncômodos diferentes.", "#7950f2", "#f3f0ff"),
]
for i, (title, subtitle, desc, analogy, color, bg) in enumerate(pilares):
    col, row = i % 2, i // 2
    x, y = 1140 + col*450, R1+105 + row*245
    elements.append(rect(x, y, 430, 225, bg, color, 2))
    elements.append(text(x+15, y+15, title, 16, color))
    elements.append(text(x+15, y+42, subtitle, 12, "#868e96"))
    elements.append(text(x+15, y+70, desc, 11, "#1e1e1e"))
    elements.append(text(x+15, y+175, f"🏠 {analogy}", 11, "#495057"))

elements.append(text(1560, R1+622, "MÓDULO 6 — SLIDE 2", 12, "#868e96"))
elements.append(text(800, R1+H1+10, "Arraste com o mouse para a direita → Slide 2", 14, "#495057"))
elements.append(arrow(1050, R1+H1+15, 50, 0, "#adb5bd", 1))

# ============ ROW 2: 6.3 Agents.md + 6.4 Skills ============

# --- Slide 6.3: Rules e Agents.md (left) ---
elements.append(slide_bg(20, R2, H2))
elements.append(text(60, R2+20, "Rules e Agents.md: A Planta Baixa", 28))
elements.append(text(60, R2+58, "O arquivo na raiz do projeto que toda IA lê ao iniciar. Máximo 200 linhas.", 14, "#868e96"))

# Visual mockup
elements.append(rect(40, R2+100, 900, 270, "#e7f5ff", "#4c6ef5", 2))
elements.append(text(60, R2+115, "📄 Exemplo de Agents.md / CLAUDE.md", 17, "#4c6ef5"))
mockup = [
    "# Project Structure",
    "├── src/          # Código fonte (Go 1.22)",
    "├── internal/     # Pacotes internos",
    "├── api/          # Definições OpenAPI",
    "└── docs/         # Documentação detalhada",
    "",
    "## Code Conventions",
    "- Nomes de função em camelCase",
    "- Testes com testify + table-driven",
    "- Commits: conventional commits",
    "- Lint: golangci-lint com config em .golangci.yml",
    "",
    "## Links",
    "- Guia de Arquitetura: /docs/architecture.md",
    "- Runbooks: /docs/runbooks/",
    "- Postmortems: /docs/postmortems/"
]
elements.append(text(60, R2+148, "\n".join(mockup), 11, "#1e1e1e"))

# Two tips below
elements.append(rect(40, R2+390, 440, 120, "#f0fff4", "#b2f2bb", 2))
elements.append(text(60, R2+402, "📌 Always-apply vs On-demand", 15, "#2f9e44"))
elements.append(text(60, R2+432, "Regras críticas: sempre carregadas.\nDocs detalhadas: sob demanda.\nPode configurar triggers automáticos.", 12, "#1e1e1e"))

elements.append(rect(510, R2+390, 430, 120, "#f3f0ff", "#7950f2", 2))
elements.append(text(530, R2+402, "💡 Dica para Legados", 15, "#7950f2"))
elements.append(text(530, R2+432, "Peça pra IA analisar o repositório e\ngerar o Agents.md automaticamente.\nClaude Code: comando 'onboard'.", 12, "#1e1e1e"))

# Bottom emphasis
elements.append(rect(40, R2+530, 900, 110, "#ffffff", "#adb5bd", 1))
elements.append(text(60, R2+542, "🔑 Impacto Real:", 16, "#1e1e1e"))
elements.append(text(60, R2+572, "Sem Agents.md: a IA erra TODAS as convenções do time — nomes, estruturas, padrões.\nCom Agents.md: parece que a IA trabalha no projeto há 6 meses. É o fator que MAIS multiplica a qualidade.", 13, "#495057"))
elements.append(text(480, R2+662, "MÓDULO 6 — SLIDE 3", 12, "#868e96"))

# --- Slide 6.4: Skills — Capacidades Portáteis (right) ---
elements.append(slide_bg(1100, R2, H2))
elements.append(text(1160, R2+20, "Skills: Capacidades Portáteis", 28))
elements.append(text(1160, R2+58, "Skill está para MCP assim como classe está para API REST — encapsula complexidade", 14, "#868e96"))

# Sem Skill
elements.append(rect(1140, R2+100, 410, 240, "#fff5f5", "#ffc9c9", 1))
elements.append(text(1160, R2+115, "❌ Sem Skill", 17, "#e03131"))
elements.append(text(1160, R2+150, 'O dev diz:\n"Corrige o bug CAN-123 na URL\ntechleads.atlassian.net, cloud\ndigital, board CAN, instância\nAtlas..."\n\nToda vez: escrever headers,\ntokens, query params, IDs.\nSujeito a erro de digitação.', 12, "#1e1e1e"))

# Com Skill
elements.append(rect(1610, R2+100, 410, 240, "#f0fff4", "#b2f2bb", 1))
elements.append(text(1630, R2+115, "✅ Com Skill Jira Assistant", 17, "#2f9e44"))
elements.append(text(1630, R2+150, 'O dev só diz:\n"Corrige a CAN-123."\n\nA skill já sabe:\n• Projeto: CAN\n• Cloud ID: configurado\n• Instância Atlas: configurada\n\nTrigger automático: o agente\ndetecta "CAN-NNN" e carrega\na skill automaticamente.', 12, "#1e1e1e"))

# Características
elements.append(rect(1140, R2+360, 880, 170, "#e7f5ff", "#4c6ef5", 2))
elements.append(text(1160, R2+375, "📋 Características de uma Skill:", 16, "#4c6ef5"))
chars = [
    "1. Front matter curto (~66 linhas) — descrição clara + triggers para carregamento automático",
    "2. Portátil — cria uma vez, usa no Cursor, Claude Code, Copilot. Compartilhável entre times.",
    "3. Trigger automático — o agente detecta padrões (ex: ID do Jira) e carrega a skill certa.",
    "4. Marketplaces internos — empresas têm criado repositórios de skills compartilhadas entre times."
]
elements.append(text(1160, R2+408, "\n".join(chars), 12, "#1e1e1e"))

# Bottom insight
elements.append(rect(1140, R2+550, 880, 90, "#f0fff4", "#b2f2bb", 1))
elements.append(text(1160, R2+562, "💡 Skills transformam conhecimento tribal em ativos reutilizáveis.", 14, "#2f9e44"))
elements.append(text(1160, R2+590, "Em vez de cada dev reinventar a roda, o time compartilha skills. onboarding mais rápido, consistência maior, menos erros.", 12, "#1e1e1e"))
elements.append(text(1560, R2+662, "MÓDULO 6 — SLIDE 4", 12, "#868e96"))

elements.append(text(820, R2+H2+10, "Arraste para baixo para ver os Slides 5 e 6", 13, "#495057"))
elements.append(arrow(960, R2+H2+15, 0, 30, "#adb5bd", 1))

# ============ ROW 3: 6.5 Sub-agents + 6.6 Checklist ============

# --- Slide 6.5: Sub-agents (left) ---
elements.append(slide_bg(20, R3, H3))
elements.append(text(60, R3+20, "Sub-agents Genéricos: A Revolução Silenciosa", 27))
elements.append(text(60, R3+56, "A novidade de 2025: você NÃO precisa criar sub-agents customizados", 14, "#868e96"))

# Clarification banner
elements.append(rect(40, R3+95, 900, 55, "#fff5f5", "#ffc9c9", 1))
elements.append(text(60, R3+102, "Antes: sub-agents eram usados para duas coisas ao mesmo tempo (isolamento + habilidade especializada). Isso criava confusão.", 12, "#e03131"))

# Skill vs Sub-agent
elements.append(rect(40, R3+165, 440, 380, "#e7f5ff", "#4c6ef5", 2))
elements.append(text(60, R3+180, "📋 SKILL", 20, "#4c6ef5"))
skill = [
    "O QUE É:",
    "Capacidade portátil — COMO fazer X.",
    "",
    "CONTEXTO:",
    "❌ NÃO reduz — roda no mesmo",
    "processo que o agente principal.",
    "",
    "QUANDO USAR:",
    "✅ Conhecimento estável",
    "✅ Reutilizável entre times",
    "✅ Padrões e convenções",
    "",
    "Analogia:",
    "Manual de instruções na sua mesa."
]
elements.append(text(60, R3+212, "\n".join(skill), 12, "#1e1e1e"))

elements.append(rect(510, R3+165, 440, 380, "#f0fff4", "#b2f2bb", 2))
elements.append(text(530, R3+180, "👷 SUB-AGENT", 20, "#2f9e44"))
sub = [
    "O QUE É:",
    "Isolamento de processo — FAÇA",
    "em paralelo sem poluir meu contexto.",
    "",
    "CONTEXTO:",
    "✅ SIM reduz — processo separado,",
    "devolve só o output final.",
    "",
    "QUANDO USAR:",
    "✅ Tarefas pesadas e multi-arquivo",
    "✅ Paralelismo (múltiplas tasks)",
    "✅ Tarefas que poluiriam o contexto",
    "",
    "Analogia:",
    "Assistente que vai pra outra sala",
    "e volta só com a resposta."
]
elements.append(text(530, R3+212, "\n".join(sub), 12, "#1e1e1e"))

# Bottom banner
elements.append(rect(40, R3+565, 910, 75, "#f0fff4", "#b2f2bb", 2))
elements.append(text(60, R3+575, "🎯 Você foca em criar boas skills. A ferramenta gerencia os sub-agents automaticamente.", 14, "#2f9e44"))
elements.append(text(60, R3+605, "Ferramentas modernas (Cursor, Claude Code) detectam quando paralelizar e iniciam agentes isolados com contexto limpo.", 12, "#1e1e1e"))
elements.append(text(480, R3+662, "MÓDULO 6 — SLIDE 5", 12, "#868e96"))

# --- Slide 6.6: Checklist + Resumo (right) ---
elements.append(slide_bg(1100, R3, H3))
elements.append(text(1160, R3+20, "Da Teoria à Prática: Checklist dos 4 Pilares", 27))
elements.append(text(1160, R3+56, "Evite o erro clássico: criar um agente de 3000 linhas em vez de 5 skills de 200 linhas", 14, "#868e96"))

# Table
elements.append(rect(1140, R3+95, 900, 260, "#ffffff", "#adb5bd", 1))
elements.append(text(1160, R3+108, "Pilar               O que colocar                              Máximo          Quando carrega", 12, "#868e96"))
table_rows = [
    "Rules/Agents.md     Estrutura, convenções, ponteiros           200 linhas      Always ou on-demand",
    "Skills              Como criar testes, buscar tasks            500 linhas      On-demand (triggers)",
    "MCPs                APIs corporativas: Jira, GitHub            —               Always (conectados)",
    "Sub-agents          NÃO crie customizados                      —               Automático",
]
for i, row in enumerate(table_rows):
    elements.append(text(1160, R3+138 + i*32, row, 12, "#1e1e1e" if i % 2 == 0 else "#495057"))

# Danger zone
elements.append(rect(1140, R3+370, 900, 50, "#fff5f5", "#ffc9c9", 1))
elements.append(text(1160, R3+382, "⚠️ Antipadrão: 1 agente de 3000 linhas que faz tudo  →  ✅ Padrão correto: 5 skills de 200 linhas, cada uma com 1 responsabilidade", 13, "#e03131"))

# Module 6 summary
elements.append(rect(1140, R3+440, 900, 200, "#f0fff4", "#b2f2bb", 2))
elements.append(text(1160, R3+455, "📋 Resumo Módulo 6:", 17, "#2f9e44"))
resumo = [
    "1. 2023-2026: Tudo no prompt → Super-agentes → Skills modulares (pule pra Fase 3 direto)",
    "2. 4 Pilares da Arquitetura de Contexto:",
    "   Rules/Agents.md (planta)  •  Skills (ferramentas)  •  MCPs (portas)  •  Sub-agents (pedreiros)",
    "3. Agents.md: Máximo 200 linhas — estrutura de alto nível + ponteiros para docs detalhadas",
    "4. Skills: Capacidade portátil, compartilhável entre times, com trigger automático",
    "5. Sub-agents genéricos: A ferramenta gerencia o isolamento e paralelismo. Você foca nas skills.",
    "",
    "🧰 Canivete suíço que faz tudo mal  vs  Kit de ferramentas especializadas."
]
elements.append(text(1160, R3+488, "\n".join(resumo), 12, "#1e1e1e"))

elements.append(text(1560, R3+662, "MÓDULO 6 — SLIDE 6", 12, "#868e96"))

# ============ Assemble ============
doc = {"type": "excalidraw", "version": 2, "source": "https://marketplace.visualstudio.com/items?itemName=pomdtr.excalidraw-editor",
       "elements": elements,
       "appState": {"viewBackgroundColor": "#ffffff", "gridSize": None, "scrollX": 0, "scrollY": 0, "zoom": {"value": 1},
                    "viewModeEnabled": False, "zenModeEnabled": False, "objectsSnapModeEnabled": False,
                    "activeTool": {"type": "selection", "customType": None, "locked": False, "lastActiveTool": None}},
       "files": {}}

out = "/home/estrazulas/git/docs_capacitacao_ia/excalidraw/modulo-06-arquitetura-contexto.excalidraw"
with open(out, "w") as f: json.dump(doc, f, indent=2, ensure_ascii=False)
print(f"✅ {out}")
print(f"   {len(elements)} elementos em 6 slides")
