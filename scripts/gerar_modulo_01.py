#!/usr/bin/env python3
"""Gera modulo-01-llms-fundamentos.excalidraw — 6 slides (inclui pré-requisitos), 3 rows."""

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

def slide_label(x, y, txt):
    return text(x + 440, y + 7, txt, 12, "#868e96")

def nav_text(x, y, txt, fs=13):
    return text(x, y, txt, fs, "#495057")

elements = []

# Heights for this module
H1 = 620  # row 1 slides
H2 = 660  # row 2 slides (2x2 grid needs more room)
H3 = 660  # row 3 slides

# Row offsets
R1 = 20
R2 = R1 + H1 + 80  # 740
R3 = R2 + H2 + 80  # 1480

# ============================================================
# ROW 1: y=R1=20 — Slides 1.0 (Pré-req) + 1.1 (Autocomplete)
# ============================================================

# --- Slide 1.0: Pré-requisitos (left, y=20) ---
elements.append(slide_bg(20, R1, H1))
elements.append(text(60, R1 + 20, "Antes de Começar: Pré-requisitos", 28))
elements.append(text(60, R1 + 58, "O que você precisa ter instalado e configurado para acompanhar os laboratórios", 14, "#868e96"))

# Left column: Ferramentas
elements.append(rect(40, R1 + 100, 450, 480, "#e7f5ff", "#4c6ef5", 2))
elements.append(text(60, R1 + 115, "🛠 Ferramentas Necessárias", 18, "#4c6ef5"))
ferramentas = [
    "1. OpenCode instalado",
    "   ▶ Assinatura FREE (gratuita) ou",
    "   ▶ Plano Básico US$ 5 no primeiro mês",
    "",
    "2. Ollama instalado",
    "   ▶ Para Módulo 2 — modelos locais",
    "",
    "3. IDE com suporte a IA",
    "   ▶ Cursor, VS Code + Copilot, ou Claude Code",
    "",
    "4. Git e Docker instalados",
    "",
    "5. Conta no GitHub",
    "   ▶ Para laboratórios de MCP e SDD",
]
elements.append(text(60, R1 + 150, "\n".join(ferramentas), 12, "#1e1e1e"))

# Right column: Nivelamento
elements.append(rect(520, R1 + 100, 440, 480, "#f0fff4", "#b2f2bb", 2))
elements.append(text(540, R1 + 115, "📚 Nivelamento Recomendado", 18, "#2f9e44"))
nivelamento = [
    "Assistir os 3 vídeos do Plano de",
    "Nivelamento (~1h30 total):",
    "",
    "1. Roadmap de IA para DevOps",
    "   ▶ 20 min — Fundamentos essenciais",
    "",
    "2. Prompt Engineering — Guia Prático",
    "   ▶ 1h10 — Técnicas na prática",
    "",
    "3. SDD para Devs",
    "   ▶ 12 min — Método completo",
    "",
    "Não é obrigatório, mas acelera",
    "muito o aproveitamento do workshop.",
]
elements.append(text(540, R1 + 150, "\n".join(nivelamento), 12, "#1e1e1e"))

# Bottom banner
elements.append(rect(40, R1 + 600, 920, 28, "#ffffff", "#adb5bd", 1))
elements.append(text(60, R1 + 606, "💡 A única ferramenta obrigatória é o OpenCode. O resto instalamos juntos durante o workshop.", 12, "#495057"))

# Slide label
elements.append(text(480, R1 + 625, "MÓDULO 1 — SLIDE 0", 12, "#868e96"))

# --- Slide 1.1: O Grande Autocomplete (right, y=20) ---
elements.append(slide_bg(1100, R1, H1))
elements.append(text(1160, R1 + 20, "O Grande Autocomplete", 28))
elements.append(text(1160, R1 + 58, 'Uma LLM não "pensa" — ela completa padrões. É uma máquina de previsão estatística de tokens.', 14, "#868e96"))

# Large central concept card
elements.append(rect(1140, R1 + 100, 900, 230, "#e7f5ff", "#4c6ef5", 2))
elements.append(text(1160, R1 + 115, "O Modelo Mental", 20, "#4c6ef5"))
concept_lines = [
    "Autocomplete do celular: você digita \"bom...\" e ele sugere \"dia\", \"tarde\", \"noite\".",
    "A LLM faz a mesma coisa — mas em vez de 3 opções, escolhe entre milhões de tokens,",
    "calculando o próximo token mais provável dado TUDO que veio antes na conversa.",
    "",
    "Não tem intenção, opinião ou consciência. É estatística pura.",
]
elements.append(text(1160, R1 + 148, "\n".join(concept_lines), 13, "#1e1e1e"))

# Bottom comparison
elements.append(rect(1140, R1 + 350, 430, 120, "#fff5f5", "#ffc9c9", 1))
elements.append(text(1160, R1 + 365, "❌ Mentalidade Errada", 15, "#e03131"))
elements.append(text(1160, R1 + 392, '"A IA é um oráculo que sabe tudo."\n"Ela pensa, tem opinião, entende."', 12, "#1e1e1e"))

elements.append(rect(1610, R1 + 350, 430, 120, "#f0fff4", "#b2f2bb", 1))
elements.append(text(1630, R1 + 365, "✅ Mentalidade Correta", 15, "#2f9e44"))
elements.append(text(1630, R1 + 392, '"A IA é um completador de padrões."\n"Preciso dar contexto de qualidade."', 12, "#1e1e1e"))

# Bottom insight
elements.append(rect(1140, R1 + 490, 900, 70, "#f0fff4", "#b2f2bb", 1))
elements.append(text(1160, R1 + 502, "💡 Por que isso importa: Muda como você escreve prompts e interpreta respostas. Você para de culpar a IA e começa a melhorar o contexto.", 13, "#2f9e44"))

# Analogy
elements.append(text(1160, R1 + 575, 'Analogia: É como um GPS que prevê sua próxima rua baseado em TODO o seu histórico de rotas, não só na última curva.', 12, "#495057"))

elements.append(text(1560, R1 + 625, "MÓDULO 1 — SLIDE 1", 12, "#868e96"))

# --- Row 1 navigation ---
elements.append(nav_text(800, R1 + H1 + 10, "Arraste com o mouse para a direita → Slide 1", 14))
elements.append(arrow(1050, R1 + H1 + 15, 50, 0, "#adb5bd", 1))

# ============================================================
# ROW 2: y=R2=740 — Slides 1.2 (Tokens+Multimodais) + 1.3 (4 Limitações)
# ============================================================

# --- Slide 1.2: Tokens + Modelos Multimodais (left, y=R2) ---
elements.append(slide_bg(20, R2, H2))
elements.append(text(60, R2 + 20, "Tokens e Modelos Multimodais", 28))
elements.append(text(60, R2 + 58, "A unidade de processamento e a expansão dos sentidos da IA", 14, "#868e96"))

# Top strip: Tokens
elements.append(rect(40, R2 + 100, 900, 260, "#e7f5ff", "#4c6ef5", 2))
elements.append(text(60, R2 + 115, "💰 Tokens: A Moeda da IA", 18, "#4c6ef5"))
token_lines = [
    "Token = unidade de processamento. Cada palavra ou fragmento que o modelo lê ou gera.",
    '"Inteligência artificial" pode ser 2 tokens. Toda API cobra por token (input + output).',
    "",
    "📊 Escala: Conversa típica de dev → 2K-20K tokens. Gemini 1.5 Pro → 2M tokens (≈ 3 livros).",
    "",
    "⚠️ Pegadinha: Se lotar a janela de contexto, o modelo começa a \"esquecer\" coisas no meio.",
    "",
    "Analogia: Token = kilowatt (moeda de consumo). Janela de contexto = RAM (enche, mas degrada)."
]
elements.append(text(60, R2 + 148, "\n".join(token_lines), 12, "#1e1e1e"))

# Bottom strip: Multimodais
elements.append(rect(40, R2 + 380, 900, 260, "#f0fff4", "#b2f2bb", 2))
elements.append(text(60, R2 + 395, "🎯 Modelos Multimodais", 18, "#2f9e44"))
multi_lines = [
    "Modelos que entendem texto, imagem, áudio e vídeo — tudo processado junto.",
    "GPT-4o, Gemini e Claude processam múltiplos formatos simultaneamente.",
    "",
    "📸 Exemplos práticos:",
    "  • Print de bug → diagnóstico e sugestão de fix",
    "  • Wireframe rabiscado → código gerado",
    "  • Áudio de reunião → ata com ações e responsáveis",
    "  • Vídeo de comportamento → análise de UX",
    "",
    "💡 Expande o que você pode delegar para a IA."
]
elements.append(text(60, R2 + 428, "\n".join(multi_lines), 12, "#1e1e1e"))

elements.append(text(480, R2 + 662, "MÓDULO 1 — SLIDE 2", 12, "#868e96"))

# --- Slide 1.3: As 4 Grandes Limitações (right, y=R2) ---
elements.append(slide_bg(1100, R2, H2))
elements.append(text(1160, R2 + 20, "As 4 Grandes Limitações", 28))
elements.append(text(1160, R2 + 58, "Conhecer essas limitações separa quem culpa a IA de quem contorna com estratégia", 14, "#868e96"))

# Top banner analogy
elements.append(rect(1140, R2 + 90, 900, 40, "#ffffff", "#adb5bd", 1))
elements.append(text(1160, R2 + 100, 'Analogia: A IA é um estagiário brilhante mas com amnésia seletiva — inventa (alucina), não sabe o que aconteceu depois de contratado (corte),', 11, "#495057"))

limitacoes = [
    ("1. Alucinações", "A IA inventa resposta com toda confiança,\nmas ela é falsa.", 'Ex: Pedir artigos de um autor → ela cria\ntítulos que não existem.', "#e03131", "#fff5f5", "#ffc9c9"),
    ("2. Data de Corte", "Enciclopédia impressa em 2023. Não sabe\nnada depois, sem acesso externo.", "Ex: Perguntar sobre uma API ou\nframework lançado em 2025.", "#fd7e14", "#fff4e6", "#ffc9c9"),
    ("3. Sensibilidade ao Prompt", "Mudar uma palavra pode gerar resposta\ncompletamente diferente.", '"Explique RAG" vs "Explique RAG pra\numa criança de 10 anos".', "#4c6ef5", "#e7f5ff", "#4c6ef5"),
    ("4. Degradação com Contexto", "Quanto mais informação de uma vez,\nmais a IA se perde no meio.", "Ex: 50 requisitos num prompt → prioriza\no início, ignora o meio, alucina no final.", "#7950f2", "#f3f0ff", "#7950f2"),
]

for i, (title, problem, example, color, bg, border) in enumerate(limitacoes):
    col = i % 2
    row_idx = i // 2
    x = 1140 + col * 450
    y = R2 + 145 + row_idx * 240
    elements.append(rect(x, y, 430, 215, bg, border, 1))
    elements.append(text(x + 15, y + 15, title, 18, color))
    elements.append(text(x + 15, y + 48, problem, 12, "#1e1e1e"))
    elements.append(text(x + 15, y + 110, example, 11, "#868e96"))

elements.append(text(1560, R2 + 662, "MÓDULO 1 — SLIDE 3", 12, "#868e96"))

# --- Row 2 navigation ---
elements.append(nav_text(820, R2 + H2 + 10, "Arraste para baixo para ver os Slides 4 e 5", 13))
elements.append(arrow(960, R2 + H2 + 15, 0, 30, "#adb5bd", 1))

# ============================================================
# ROW 3: y=R3=1480 — Slides 1.4 (FT vs RAG) + 1.5 (Não usar + Resumo)
# ============================================================

# --- Slide 1.4: Pré-Treinamento, Fine-Tuning e RAG (left, y=R3) ---
elements.append(slide_bg(20, R3, H3))
elements.append(text(60, R3 + 20, "Pré-Treinamento, Fine-Tuning e a Regra dos 95%", 28))
elements.append(text(60, R3 + 58, "Para 95% dos casos, RAG resolve — sem retreinar nada. Fine-tuning é o impulso errado.", 14, "#868e96"))

# 3 columns
cols = [
    ("Pré-Treinamento", "Chef formado em\nculinária. Sabe\ncozinhar quase tudo.", "Milhões de dólares.\nSó os grandes fazem\n(GPT, Claude, Gemini).", "#4c6ef5", "#e7f5ff"),
    ("Fine-Tuning", "Chef faz curso\nespecializado de sushi.\nCaro e trabalhoso.", "Caro, lento, difícil\nde atualizar.\n~5% dos casos.", "#fd7e14", "#fff4e6"),
    ("RAG", "Entregar a receita\npro chef na hora.\nBarato, rápido.", "Só custo de embedding\n+ busca. Atualizável:\nmudou doc? Reindexa.", "#40c057", "#f0fff4"),
]

for i, (title, analogy, cost, color, bg) in enumerate(cols):
    x = 40 + i * 310
    elements.append(rect(x, R3 + 110, 290, 320, bg, color, 2))
    elements.append(text(x + 15, R3 + 125, title, 18, color))
    elements.append(text(x + 15, R3 + 165, analogy, 13, "#1e1e1e"))
    elements.append(text(x + 15, R3 + 270, "Custo:", 14, "#1e1e1e"))
    elements.append(text(x + 15, R3 + 292, cost, 12, "#495057"))
    # Arrows between columns
    if i < 2:
        elements.append(text(x + 295, R3 + 260, "→", 18, "#adb5bd"))

# Bottom banner
elements.append(rect(40, R3 + 450, 900, 70, "#f0fff4", "#b2f2bb", 2))
elements.append(text(60, R3 + 462, "🔑 Regra dos 95%: RAG resolve quase todos os usos corporativos — FAQ, docs internas, base de conhecimento.", 14, "#2f9e44"))
elements.append(text(60, R3 + 490, '⚠️ Fine-tuning é o primeiro impulso de todo dev quando a IA erra — mas quase sempre é a solução errada (cara e lenta).', 12, "#e03131"))

# Bottom summary
elements.append(rect(40, R3 + 540, 900, 100, "#ffffff", "#adb5bd", 1))
summary_lines = [
    "Pré-treinamento = Chef formado (base)    |    Fine-Tuning = Especialização cara em sushi    |    RAG = Receita na mão do chef",
    "",
    "Vantagens do RAG: Mais barato • Mais rápido • Mais fácil de atualizar • Sem retreino • Fácil de debugar"
]
elements.append(text(60, R3 + 552, "\n".join(summary_lines), 12, "#1e1e1e"))

elements.append(text(480, R3 + 662, "MÓDULO 1 — SLIDE 4", 12, "#868e96"))

# --- Slide 1.5: Quando NÃO Usar + Resumo do Módulo (right, y=R3) ---
elements.append(slide_bg(1100, R3, H3))
elements.append(text(1160, R3 + 20, "Quando NÃO Usar uma LLM + Resumo do Módulo", 28))
elements.append(text(1160, R3 + 58, "Saber quando NÃO usar IA é tão importante quanto saber usar", 14, "#868e96"))

# Top section: Quando NÃO usar
elements.append(rect(1140, R3 + 100, 900, 230, "#fff5f5", "#ffc9c9", 1))
elements.append(text(1160, R3 + 112, "❌ Tarefas que um Algoritmo Determinístico Resolve Melhor", 16, "#e03131"))
nao_usar = [
    "• Validação de formato — regex resolve, não precisa de IA",
    "• Parsing determinístico — JSON, XML, CSV: use parser nativo",
    "• Cálculos matemáticos — use funções, não LLM",
    "• Ordenação e filtros simples — SQL ou código direto",
    "• Tarefas com zero tolerância a erro — IA é probabilística, não determinística",
    "• Quando o custo da API supera o benefício — tarefa simples + LLM = martelo dourado",
    "",
    'Analogia: "Você não chama um arquiteto pra pendurar um quadro. Às vezes um prego e um martelo resolvem."'
]
elements.append(text(1160, R3 + 142, "\n".join(nao_usar), 12, "#1e1e1e"))

# Module summary
elements.append(rect(1140, R3 + 350, 900, 290, "#f0fff4", "#b2f2bb", 2))
elements.append(text(1160, R3 + 365, "📋 Resumo do Módulo 1", 18, "#2f9e44"))
resumo = [
    "1. LLM = autocomplete estatístico de tokens, não um oráculo consciente",
    "2. Token = moeda de consumo. Janela de contexto = RAM (degrada antes do limite).",
    "3. 4 limitações: Alucinações, Data de Corte, Sensibilidade ao Prompt, Degradação.",
    "4. Modelos multimodais expandem o que pode ser delegado (texto, imagem, áudio, vídeo).",
    "5. RAG resolve 95% dos casos. Fine-tuning é o último recurso, não o primeiro.",
    "6. Nem tudo precisa de IA. Algoritmos determinísticos são melhores, mais baratos e previsíveis.",
    "7. Contexto de qualidade > Modelo caro. O prompt e o contexto importam mais que o LLM.",
    "",
    "🧠 Regra de ouro: Trate a IA como completador de padrões que precisa de contexto de qualidade — não como oráculo."
]
elements.append(text(1160, R3 + 398, "\n".join(resumo), 12, "#1e1e1e"))

elements.append(text(1560, R3 + 662, "MÓDULO 1 — SLIDE 5", 12, "#868e96"))

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

out_path = "/home/estrazulas/git/docs_capacitacao_ia/excalidraw/modulo-01-llms-fundamentos.excalidraw"
with open(out_path, "w") as f:
    json.dump(doc, f, indent=2, ensure_ascii=False)

print(f"✅ {out_path}")
print(f"   {len(elements)} elementos em 6 slides (inclui pré-requisitos)")
