#!/usr/bin/env python3
"""Gera modulo-02-open-source.excalidraw — 4 slides, 2 rows."""

import json, uuid

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
        "startArrowhead": "arrow", "endArrowhead": "arrow" if w > 0 or h > 0 else None,
        "startBinding": None, "endBinding": None, "lastCommittedPoint": None,
        "points": [[0, 0], [w, h]],
        "angle": 0, "opacity": 100, "roughness": 0, "roundness": None,
        "boundElements": None, "groupIds": [], "frameId": None,
        "isDeleted": False, "locked": False, "seed": 1, "versionNonce": 1, "updated": 1,
        "backgroundColor": "transparent", "fillStyle": "solid"
    }

def slide_bg(x, y, h=620):
    return rect(x, y, 960, h, "#f8f9fa", "#dee2e6", 1)

elements = []

H = 640  # all slides slightly taller for dense content
R1, R2 = 20, 740

# ============================================================
# ROW 1: y=20 — Slides 2.1 + 2.2
# ============================================================

# --- Slide 2.1: Open-Source vs Proprietários (left) ---
elements.append(slide_bg(20, R1, H))
elements.append(text(60, R1 + 20, "Modelos Open-Source: As Receitas Públicas", 26))
elements.append(text(60, R1 + 56, "Open-source = soberania. Proprietário = conveniência. A escolha depende do caso.", 14, "#868e96"))

# Left: Open-Source
elements.append(rect(40, R1 + 100, 430, 450, "#f0fff4", "#b2f2bb", 2))
elements.append(text(60, R1 + 115, "🍳 Open-Source", 18, "#2f9e44"))
os_content = [
    "Receitas de bolo publicadas de graça —",
    "você pode usar, modificar e rodar na",
    "sua máquina sem pagar royalties.",
    "",
    "Modelos principais:",
    "• Llama (Meta) — família de modelos",
    "• Qwen (Alibaba) — forte em código",
    "• DeepSeek — eficiência e raciocínio",
    "• Mistral — performance em múltiplos idiomas",
    "",
    "Vantagens:",
    "✅ Soberania — sem depender de fornecedor",
    "✅ Privacidade — dados não saem da máquina",
    "✅ Customizável — fine-tuning possível",
    "",
    "Analogia: Cozinhar em casa com a receita."
]
elements.append(text(60, R1 + 148, "\n".join(os_content), 12, "#1e1e1e"))

# Right: Proprietários
elements.append(rect(510, R1 + 100, 430, 450, "#e7f5ff", "#4c6ef5", 2))
elements.append(text(530, R1 + 115, "🏪 Proprietários", 18, "#4c6ef5"))
prop_content = [
    "Restaurantes: a comida é ótima, mas você",
    "não tem acesso à receita nem controle",
    "sobre a cozinha.",
    "",
    "Modelos principais:",
    "• GPT-4o (OpenAI) — multi-modal",
    "• Claude (Anthropic) — raciocínio longo",
    "• Gemini (Google) — janela de 2M tokens",
    "",
    "Características:",
    "💰 API paga por token (input + output)",
    "🌐 Dados trafegam por servidores externos",
    "🔒 Sem controle sobre versão do modelo",
    "",
    "Analogia: Pedir delivery — prático, mas caro."
]
elements.append(text(530, R1 + 148, "\n".join(prop_content), 12, "#1e1e1e"))

# Bottom banner
elements.append(rect(40, R1 + 570, 900, 40, "#ffffff", "#adb5bd", 1))
elements.append(text(60, R1 + 580, "🔑 Para empresas com restrições de compliance, open-source muitas vezes é a única opção viável.", 13, "#495057"))

elements.append(text(480, R1 + 642, "MÓDULO 2 — SLIDE 1", 12, "#868e96"))

# --- Slide 2.2: Ollama + Hugging Face (right) ---
elements.append(slide_bg(1100, R1, H))
elements.append(text(1160, R1 + 20, "Ollama e Hugging Face: O Kit de Ferramentas", 26))
elements.append(text(1160, R1 + 56, "Em 5 minutos você roda um modelo localmente. Em 5 minutos acha um modelo especializado.", 14, "#868e96"))

# Ollama card
elements.append(rect(1140, R1 + 100, 430, 450, "#e7f5ff", "#4c6ef5", 2))
elements.append(text(1160, R1 + 115, "🦙 Ollama: O Eletrodoméstico", 18, "#4c6ef5"))
ollama = [
    "Ollama está pra LLM assim como Docker",
    "está pra aplicação — baixa e roda com",
    "um comando, sem depender de internet.",
    "",
    "Instalação:",
    "  brew install ollama  (macOS)",
    "  apt-get install ollama  (Linux)",
    "",
    "Uso:",
    '  ollama run llama3.2',
    '  ollama run qwen2.5:7b',
    "",
    "Vantagens:",
    "✅ Sem API key — execução 100% local",
    "✅ Dados não saem da máquina",
    "✅ Ideal para testar e comparar modelos",
    "",
    "Analogia: Docker pull + run, mas pra LLMs."
]
elements.append(text(1160, R1 + 148, "\n".join(ollama), 12, "#1e1e1e"))

# Hugging Face card
elements.append(rect(1610, R1 + 100, 430, 450, "#f0fff4", "#b2f2bb", 2))
elements.append(text(1630, R1 + 115, "🤗 Hugging Face: O GitHub dos Modelos", 17, "#2f9e44"))
hf = [
    "Maior repositório de IA do mundo —",
    "milhares de modelos pré-treinados,",
    "datasets e fine-tunings da comunidade.",
    "",
    "O que você encontra:",
    "• Modelos especializados (SQL, contratos)",
    "• Benchmarks e comparações públicas",
    "• Fine-tunings da comunidade",
    "• Datasets para treinamento",
    "",
    "Regra de ouro:",
    "Antes de pensar em treinar qualquer",
    "coisa, procure no Hugging Face.",
    "Provavelmente alguém já fez algo similar.",
    "",
    "Analogia: GitHub — repositório público,",
    "comunidade ativa, versões, forks."
]
elements.append(text(1630, R1 + 148, "\n".join(hf), 12, "#1e1e1e"))

elements.append(text(1560, R1 + 642, "MÓDULO 2 — SLIDE 2", 12, "#868e96"))

# --- Row 1 navigation ---
elements.append(text(800, R1 + H + 10, "Arraste com o mouse para a direita → Slide 2", 14, "#495057"))
elements.append(arrow(1050, R1 + H + 15, 50, 0, "#adb5bd", 1))

# ============================================================
# ROW 2: y=740 — Slides 2.3 + 2.4
# ============================================================

# --- Slide 2.3: Parâmetros — Mais Nem Sempre é Melhor (left) ---
elements.append(slide_bg(20, R2, H))
elements.append(text(60, R2 + 20, "Parâmetros: Mais Nem Sempre é Melhor", 28))
elements.append(text(60, R2 + 58, "Modelos menores e especializados entregam 80% da qualidade por 10% do custo", 14, "#868e96"))

# Two comparison cards
elements.append(rect(40, R2 + 100, 430, 220, "#e7f5ff", "#4c6ef5", 2))
elements.append(text(60, R2 + 115, "🚛 LLMs Grandes", 18, "#4c6ef5"))
llm_big = [
    "GPT-4o, Claude Opus, Gemini Ultra",
    "Centenas de bilhões de parâmetros.",
    "",
    "• Capacidade máxima de raciocínio",
    "• Custo alto por token",
    "• Latência maior (modelos pesados)",
    "",
    "Analogia: Caminhão — leva tudo,\nmas gasta muito combustível."
]
elements.append(text(60, R2 + 148, "\n".join(llm_big), 12, "#1e1e1e"))

elements.append(rect(510, R2 + 100, 430, 220, "#f0fff4", "#b2f2bb", 2))
elements.append(text(530, R2 + 115, "🏍️ SLMs (Small Language Models)", 18, "#2f9e44"))
slm = [
    "Phi-3, Llama 8B, Qwen 7B, Gemma",
    "Poucos bilhões de parâmetros.",
    "",
    "• 80% da qualidade por 10% do custo",
    "• Latência mínima (roda local)",
    "• Custo zero de API",
    "• Ideal para: sumarização, classificação,",
    "  parsing, autocomplete, código simples",
    "",
    "Analogia: Moto — ágil, econômica,\nresolve 80% dos trajetos."
]
elements.append(text(530, R2 + 148, "\n".join(slm), 12, "#1e1e1e"))

# Key insight
elements.append(rect(40, R2 + 340, 900, 50, "#f3f0ff", "#7950f2", 2))
elements.append(text(60, R2 + 352, "🔬 Pesquisas recentes mostram que REMOVER parâmetros às vezes MELHORA o modelo — como tirar \"sujeira\" do cérebro.", 13, "#7950f2"))

# Decision matrix
elements.append(rect(40, R2 + 410, 900, 210, "#ffffff", "#adb5bd", 1))
elements.append(text(60, R2 + 420, "Quando Usar Cada Um:", 16, "#1e1e1e"))
matrix = [
    "SLM Local (latência mínima, custo zero):",
    "  • Sumarização de logs e documentos    • Classificação de tickets e e-mails",
    "  • Parsing de dados estruturados        • Autocomplete e sugestões simples",
    "  • Extração de entidades",
    "",
    "LLM Cloud (raciocínio complexo, pontual):",
    "  • Design de arquitetura de software    • Debugging multi-arquivo",
    "  • Geração de documentação técnica     • Análise de vulnerabilidades",
    "  • Tradução e refatoração complexa"
]
elements.append(text(60, R2 + 450, "\n".join(matrix), 12, "#1e1e1e"))

elements.append(text(480, R2 + 642, "MÓDULO 2 — SLIDE 3", 12, "#868e96"))

# --- Slide 2.4: Critérios de Escolha — Nuvem vs Local (right) ---
elements.append(slide_bg(1100, R2, H))
elements.append(text(1160, R2 + 20, "Critérios de Escolha: Nuvem vs Local", 28))
elements.append(text(1160, R2 + 58, "Times maduros montam arquiteturas híbridas — SLM local + API cloud", 14, "#868e96"))

# 2x2 grid
criterios = [
    ("💰 Custo", "API cobra por token (input + output).\nLocal sai de graça depois do setup.", "SLM local: custo zero de API.\nAPI cloud: pay-as-you-go.", "#fd7e14", "#fff4e6"),
    ("⚡ Latência", "Local é mais rápido para tarefas\nsimples — sem round-trip de rede.", "Local: resposta instantânea.\nCloud: latência de rede + servidor.", "#4c6ef5", "#e7f5ff"),
    ("🔒 Privacidade", "Local = dados não saem da máquina.\nEssencial para compliance e LGPD.", "Dados sensíveis nunca trafegam\npor APIs de terceiros.", "#7950f2", "#f3f0ff"),
    ("🧠 Capacidade", "Nuvem tem modelos maiores para\nraciocínio complexo e multi-step.", "Local é limitado pelo hardware.\nGPU potente = modelos maiores.", "#40c057", "#f0fff4"),
]

for i, (title, desc, insight, color, bg) in enumerate(criterios):
    col = i % 2
    row = i // 2
    x = 1140 + col * 450
    y = R2 + 100 + row * 240
    elements.append(rect(x, y, 430, 215, bg, color, 2))
    elements.append(text(x + 15, y + 15, title, 20, color))
    elements.append(text(x + 15, y + 50, desc, 12, "#1e1e1e"))
    elements.append(text(x + 15, y + 130, f"💡 {insight}", 12, "#495057"))

# Hybrid architecture callout
elements.append(rect(1140, R2 + 600, 900, 40, "#f0fff4", "#b2f2bb", 2))
elements.append(text(1160, R2 + 610, "🏗️ Arquitetura Híbrida Ideal: SLM local para alto volume/baixo risco + API cloud para tarefas complexas/pontuais.", 13, "#2f9e44"))

elements.append(text(1560, R2 + 642, "MÓDULO 2 — SLIDE 4", 12, "#868e96"))

# ============================================================
# Assemble
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

out_path = "/home/estrazulas/git/docs_capacitacao_ia/excalidraw/modulo-02-open-source.excalidraw"
with open(out_path, "w") as f:
    json.dump(doc, f, indent=2, ensure_ascii=False)

print(f"✅ {out_path}")
print(f"   {len(elements)} elementos em 4 slides")
