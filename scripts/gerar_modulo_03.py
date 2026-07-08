#!/usr/bin/env python3
"""Gera modulo-03-prompt-engineering.excalidraw — 5 slides, 3 rows."""

import json, uuid, math

def mid():
    return "m" + uuid.uuid4().hex[:16]

def rect(x, y, w, h, bg, stroke="#adb5bd", sw=1):
    return {
        "id": mid(), "type": "rectangle", "x": x, "y": y, "width": w, "height": h,
        "backgroundColor": bg, "strokeColor": stroke, "strokeWidth": sw,
        "angle": 0, "opacity": 100, "roughness": 0, "roundness": None,
        "boundElements": None, "groupIds": [], "frameId": None,
        "isDeleted": False, "locked": False, "seed": 1, "versionNonce": 1, "updated": 1,
        "fillStyle": "solid"
    }

def text(x, y, content, fs, color="#1e1e1e", w=None, h=None):
    lines = content.split("\n")
    max_line = max(len(l) for l in lines)
    if w is None:
        w = max_line * fs * 0.58
    if h is None:
        h = len(lines) * fs * 1.35
    return {
        "id": mid(), "type": "text", "x": x, "y": y, "width": w, "height": h,
        "text": content, "fontSize": fs, "strokeColor": color,
        "fontFamily": 2, "textAlign": "left", "verticalAlign": "top",
        "autoResize": True, "lineHeight": 1.25,
        "angle": 0, "opacity": 100, "roughness": 0, "roundness": None,
        "boundElements": None, "groupIds": [], "frameId": None,
        "isDeleted": False, "locked": False, "seed": 1, "versionNonce": 1, "updated": 1,
        "backgroundColor": "transparent", "fillStyle": "solid"
    }

def arrow(x, y, w, h, color="#adb5bd", sw=1):
    return {
        "id": mid(), "type": "arrow", "x": x, "y": y, "width": w, "height": h,
        "strokeColor": color, "strokeWidth": sw,
        "startArrowhead": "arrow", "endArrowhead": "arrow",
        "startBinding": None, "endBinding": None, "lastCommittedPoint": None,
        "points": [[0, 0], [w, h]],
        "angle": 0, "opacity": 100, "roughness": 0, "roundness": None,
        "boundElements": None, "groupIds": [], "frameId": None,
        "isDeleted": False, "locked": False, "seed": 1, "versionNonce": 1, "updated": 1,
        "backgroundColor": "transparent", "fillStyle": "solid"
    }

def slide_bg(x, y, h=620):
    return rect(x, y, 960, h, "#f8f9fa", "#dee2e6", 1)

def slide_label(x, y, txt):
    """Label centralizado abaixo do slide"""
    return text(x + 450, y + 625, txt, 12, "#868e96")

def nav_text(x, y, txt, fs=13):
    return text(x, y, txt, fs, "#495057")

elements = []

# Row offsets
R1, R2, R3 = 20, 740, 1480

# ============================================================
# ROW 1: y=20 — Slides 3.1 + 3.2
# ============================================================

# --- Slide 3.1: Os 5 Elementos (left, x=20) ---
elements.append(slide_bg(20, R1))
elements.append(text(60, R1 + 20, "Os 5 Elementos de um Prompt Eficiente", 28))
elements.append(text(60, R1 + 58, "A diferença entre receber código que você commita e código que você reescreve do zero", 14, "#868e96"))

# Green section background
elements.append(rect(40, R1 + 100, 900, 430, "#f0fff4", "#b2f2bb", 1))

# 5 strips with colored labels
strips = [
    ("1. ROLE", "Define quem a IA é. Ex: \"Você é um dev sênior especialista em refatoração de código legado\"", "#4c6ef5"),
    ("2. CONTEXTO", "O background que a IA não tem. Ex: \"API Go 1.22 com arquitetura hexagonal, PostgreSQL\"", "#40c057"),
    ("3. INSTRUÇÃO", "A ação, clara e direta. Ex: \"Refatore a função extraindo a validação pra outra função\"", "#fd7e14"),
    ("4. RESTRIÇÕES", "Limites e o que não fazer. Ex: \"Mantenha os nomes de função. Não use generics.\"", "#7950f2"),
    ("5. FORMATO", "Estrutura esperada da resposta. Ex: \"Retorne só o código em markdown com o nome do arquivo\"", "#e64980"),
]
for i, (label, desc, color) in enumerate(strips):
    y = R1 + 120 + i * 78
    elements.append(text(60, y, label, 16, color))
    elements.append(text(60, y + 22, desc, 13, "#1e1e1e"))

# Bottom analogy
elements.append(text(60, R1 + 540, 'Analogia: Pedir sem estrutura = "conserta minha casa". Com os 5 elementos = entregar planta baixa, materiais, normas e prazo.', 13, "#495057"))

elements.append(slide_label(20, R1, "MÓDULO 3 — SLIDE 1"))

# --- Slide 3.2: Frameworks RTF, CARE, RISE (right, x=1100) ---
elements.append(slide_bg(1100, R1))
elements.append(text(1160, R1 + 20, "Frameworks de Prompt: RTF, CARE, RISE", 28))
elements.append(text(1160, R1 + 58, "Nem todo prompt precisa dos 5 elementos. Escolha o framework certo para cada tarefa.", 14, "#868e96"))

# 3 columns
fw_data = [
    ("RTF", "Role, Task, Format", "Tarefas simples e de padrão conhecido", ["Gerar Dockerfile", "Criar JSON schema", "Script SQL simples"], "Post-it — resolve com 3 linhas", "#4c6ef5", "#e7f5ff"),
    ("CARE", "Context, Action, Result, Example", "Tarefas com objetivo de negócio", ["Runbook de incidente", "Plano de migração", "Documento de arquitetura"], "E-mail formal bem estruturado", "#40c057", "#f0fff4"),
    ("RISE", "Role, Input, Steps, Example", "Tarefas com múltiplos passos (CoT implícito)", ["Análise de vulnerabilidade", "Troubleshooting complexo", "Code review estruturada"], "Documentação técnica passo a passo", "#7950f2", "#f3f0ff"),
]

for i, (name, acronym, use_case, examples, analogy, color, bg) in enumerate(fw_data):
    x = 1140 + i * 300
    # Card bg
    elements.append(rect(x, R1 + 100, 280, 460, bg, color, 2))
    # Name
    elements.append(text(x + 15, R1 + 115, name, 22, color))
    # Acronym
    elements.append(text(x + 15, R1 + 145, acronym, 13, "#868e96"))
    # Use case header
    elements.append(text(x + 15, R1 + 180, "Quando usar:", 14, "#1e1e1e"))
    elements.append(text(x + 15, R1 + 202, use_case, 12, "#1e1e1e"))
    # Examples
    elements.append(text(x + 15, R1 + 250, "Exemplos:", 14, "#1e1e1e"))
    for j, ex in enumerate(examples):
        elements.append(text(x + 15, R1 + 272 + j * 22, f"• {ex}", 12, "#1e1e1e"))
    # Analogy
    elements.append(text(x + 15, R1 + 380, "Analogia:", 14, "#1e1e1e"))
    elements.append(text(x + 15, R1 + 402, analogy, 12, "#495057"))

# Arrow labels between columns
elements.append(text(1420, R1 + 320, "→", 16, "#adb5bd"))
elements.append(text(1720, R1 + 320, "→", 16, "#adb5bd"))

elements.append(slide_label(1100, R1, "MÓDULO 3 — SLIDE 2"))

# --- Row 1 navigation ---
elements.append(nav_text(800, R1 + 630, "Arraste com o mouse para a direita → Slide 2", 14))
elements.append(arrow(1050, R1 + 635, 50, 0, "#adb5bd", 1))

# ============================================================
# ROW 2: y=740 — Slides 3.3 + 3.4
# ============================================================

# --- Slide 3.3: Técnicas de Raciocínio (left, x=20) ---
elements.append(slide_bg(20, R2))
elements.append(text(60, R2 + 20, "Técnicas de Raciocínio", 28))
elements.append(text(60, R2 + 58, "Frameworks estruturam o prompt. Técnicas definem como o modelo raciocina.", 14, "#868e96"))

tecnicas = [
    ("Zero-shot", "Instrução direta, sem exemplo", "Tarefas comuns que o modelo já conhece: CRUD, explicar erro, traduzir código.", 'Analogia: "Faz um bolo."', "Funciona bem para tarefas objetivas e sem ambiguidade.", "#4c6ef5", "#e7f5ff"),
    ("Few-shot", "Você dá 1-3 exemplos de input → output", "Formato muito específico ou convenção interna que o modelo não conhece.", 'Analogia: "Faz um bolo igual a este" (mostra foto).', "A técnica mais subestimada — 2 exemplos bem escolhidos entregam mais qualidade que 2h refinando prompt.", "#40c057", "#f0fff4"),
    ("Chain of Thought", "Força o modelo a mostrar o raciocínio passo a passo", "Análise, troubleshooting, decisões com trade-off.", 'Analogia: "Me explica como você vai fazer antes de começar."', "A que mais reduz alucinação em tarefas analíticas.", "#7950f2", "#f3f0ff"),
]

for i, (name, desc, when, analogy, insight, color, bg) in enumerate(tecnicas):
    x = 40 + i * 310
    elements.append(rect(x, R2 + 100, 290, 460, bg, color, 2))
    elements.append(text(x + 15, R2 + 115, name, 20, color))
    elements.append(text(x + 15, R2 + 148, desc, 12, "#1e1e1e"))
    elements.append(text(x + 15, R2 + 210, "Quando usar:", 14, "#1e1e1e"))
    elements.append(text(x + 15, R2 + 232, when, 12, "#1e1e1e"))
    elements.append(text(x + 15, R2 + 310, analogy, 12, "#495057"))
    elements.append(text(x + 15, R2 + 350, "Por que importa:", 14, "#1e1e1e"))
    elements.append(text(x + 15, R2 + 372, insight, 12, "#1e1e1e"))

# Bottom banner
elements.append(rect(40, R2 + 580, 900, 40, "#f0fff4", "#b2f2bb", 1))
elements.append(text(60, R2 + 590, "Regra: Zero-shot para tarefas objetivas. Few-shot para estilo, tom e convenções. CoT para análise e diagnóstico.", 13, "#2f9e44"))

elements.append(slide_label(20, R2, "MÓDULO 3 — SLIDE 3"))

# --- Slide 3.4: Antipadrões (right, x=1100) ---
elements.append(slide_bg(1100, R2))
elements.append(text(1160, R2 + 20, "Antipadrões e Erros Comuns", 28))
elements.append(text(1160, R2 + 58, "A maioria dos prompts ruins sofre de um desses 4 problemas", 14, "#868e96"))

antipadroes = [
    ("1. Sobrecarga de Instruções", "10 comandos num prompt só → o modelo prioriza os primeiros e ignora os últimos.", "Fix: Quebre em prompts separados ou use RISE com steps.", "#e03131", "#fff5f5", "#ffc9c9"),
    ("2. Prompt Vago Demais", '"Melhore esse código" → o modelo não sabe se é performance, legibilidade ou segurança.', 'Fix: Especifique a dimensão. Ex: "Melhore a performance reduzindo alocações de memória."', "#fd7e14", "#fff4e6", "#ffc9c9"),
    ("3. Restrições Contraditórias", '"Seja conciso" + "Explique em detalhes" → o modelo trava.', 'Fix: Priorize. Ex: "Seja conciso. Se precisar de detalhes, eu pergunto."', "#4c6ef5", "#e7f5ff", "#ffc9c9"),
    ("4. Confiar Cegamente", "Não validar saídas, especialmente código e dados estruturados.", "Fix: Sempre rode testes, valide JSON schema, verifique imports.", "#7950f2", "#f3f0ff", "#ffc9c9"),
]

for i, (title, problem, fix, color, bg, border) in enumerate(antipadroes):
    col = i % 2
    row = i // 2
    x = 1140 + col * 450
    y = R2 + 100 + row * 240
    elements.append(rect(x, y, 430, 210, bg, border, 1))
    elements.append(text(x + 15, y + 15, title, 16, color))
    elements.append(text(x + 15, y + 45, problem, 12, "#1e1e1e"))
    elements.append(text(x + 15, y + 100, fix, 12, "#2f9e44"))

elements.append(slide_label(1100, R2, "MÓDULO 3 — SLIDE 4"))

# --- Row 2 navigation ---
elements.append(nav_text(820, R2 + 635, "Arraste para baixo para ver o Slide 5", 13))
elements.append(arrow(960, R2 + 640, 0, 30, "#adb5bd", 1))

# ============================================================
# ROW 3: y=1480 — Slide 3.5 (apenas esquerda)
# ============================================================

elements.append(slide_bg(20, R3))
elements.append(text(60, R3 + 20, "Qual Framework Usar? — Cheat Sheet", 28))
elements.append(text(60, R3 + 58, "Um guia rápido para escolher a abordagem certa em segundos", 14, "#868e96"))

# Decision tree as boxes
decisions = [
    ("Tarefa simples,\npadrão conhecido?", "SIM → RTF\n(3 linhas resolvem)", "#4c6ef5", "#e7f5ff"),
    ("Precisa de objetivo\nde negócio claro?", "SIM → CARE\n(contexto + resultado)", "#40c057", "#f0fff4"),
    ("Múltiplos passos,\nanálise complexa?", "SIM → RISE\n(steps + CoT)", "#7950f2", "#f3f0ff"),
    ("Precisa de estilo/tom/\nconvenção específica?", "Adicione Few-shot\nao framework escolhido", "#e64980", "#fff5f5"),
]

for i, (question, answer, color, bg) in enumerate(decisions):
    x = 40 + i * 230
    # Question box
    elements.append(rect(x, R3 + 140, 215, 120, bg, color, 2))
    elements.append(text(x + 10, R3 + 150, question, 12, "#1e1e1e"))
    # Arrow down
    elements.append(arrow(x + 100, R3 + 265, 0, 30, color, 1))
    # Answer box
    elements.append(rect(x, R3 + 300, 215, 100, "#ffffff", color, 1))
    elements.append(text(x + 10, R3 + 310, answer, 13, color))

# Dica de ouro
elements.append(rect(40, R3 + 430, 900, 60, "#f0fff4", "#b2f2bb", 1))
elements.append(text(60, R3 + 442, "💡 Dica de Ouro: Comece simples (Zero-shot + RTF). Só adicione complexidade se a resposta não for boa o suficiente.", 14, "#2f9e44"))

# Module summary
elements.append(rect(40, R3 + 510, 900, 80, "#ffffff", "#adb5bd", 1))
elements.append(text(60, R3 + 520, "Resumo Módulo 3:  1. 5 elementos (Role, Contexto, Instrução, Restrições, Formato)  2. Frameworks (RTF → CARE → RISE)  3. Técnicas (Zero-shot, Few-shot, CoT)  4. Evite: sobrecarga, vagueza, contradição, confiança cega", 12, "#1e1e1e"))

elements.append(slide_label(20, R3, "MÓDULO 3 — SLIDE 5"))

# ============================================================
# Assemble final document
# ============================================================

doc = {
    "type": "excalidraw",
    "version": 2,
    "source": "https://marketplace.visualstudio.com/items?itemName=pomdtr.excalidraw-editor",
    "elements": elements,
    "appState": {
        "viewBackgroundColor": "#ffffff",
        "gridSize": None,
        "scrollX": 0,
        "scrollY": 0,
        "zoom": {"value": 1},
        "viewModeEnabled": False,
        "zenModeEnabled": False,
        "objectsSnapModeEnabled": False,
        "activeTool": {"type": "selection", "customType": None, "locked": False, "lastActiveTool": None}
    },
    "files": {}
}

out_path = "/home/estrazulas/git/docs_capacitacao_ia/excalidraw/modulo-03-prompt-engineering.excalidraw"
with open(out_path, "w") as f:
    json.dump(doc, f, indent=2, ensure_ascii=False)

print(f"✅ {out_path}")
print(f"   {len(elements)} elementos em 5 slides")
