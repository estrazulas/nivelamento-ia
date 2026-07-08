#!/usr/bin/env python3
"""Gera modulo-04-rag-embeddings.excalidraw — 5 slides, 3 rows."""

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
    if w is None: w = max_line * fs * 0.58
    if h is None: h = len(lines) * fs * 1.35
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

H1 = 620  # R1: 4.1, 4.2
H2 = 660  # R2: 4.3, 4.4 (more content)
H3 = 620  # R3: 4.5

R1, R2, R3 = 20, 740, 1460

# ============================================================
# ROW 1: Slides 4.1 + 4.2
# ============================================================

# --- Slide 4.1: RAG — O Conceito (left) ---
elements.append(slide_bg(20, R1, H1))
elements.append(text(60, R1 + 20, "RAG: A Cola na Prova", 28))
elements.append(text(60, R1 + 58, "Em vez de confiar na memória da IA, você entrega os trechos relevantes do seu material", 14, "#868e96"))

# Left: Sem RAG
elements.append(rect(40, R1 + 100, 430, 400, "#fff5f5", "#ffc9c9", 1))
elements.append(text(60, R1 + 115, "❌ Sem RAG — Confia na Memória", 17, "#e03131"))
sem_rag = [
    "Fluxo:",
    "  Pergunta → LLM (memória interna)",
    "           → Resposta",
    "",
    "⚠️ Problemas:",
    "• Pode alucinar — não tem fonte externa",
    "• Informação desatualizada",
    "• Não conhece dados do seu domínio",
    "• Não consegue citar fontes",
    "",
    "Analogia:",
    "Aluno fazendo prova sem consulta —",
    "confia só no que lembra. Se não",
    "lembrar, chuta (alucina)."
]
elements.append(text(60, R1 + 148, "\n".join(sem_rag), 12, "#1e1e1e"))

# Right: Com RAG
elements.append(rect(510, R1 + 100, 430, 400, "#f0fff4", "#b2f2bb", 1))
elements.append(text(530, R1 + 115, "✅ Com RAG — Contexto Relevante", 17, "#2f9e44"))
com_rag = [
    "Fluxo:",
    "  Pergunta → Busca docs relevantes",
    "          → LLM (com contexto)",
    "          → Resposta baseada em fontes",
    "",
    "✅ Vantagens:",
    "• Respostas baseadas em dados reais",
    "• Fontes citáveis e auditáveis",
    "• Atualização fácil (reindexa, não retreina)",
    "• Domínio específico sem fine-tuning",
    "",
    "Analogia:",
    "Aluno com livro aberto na página certa —",
    "consulta a fonte e responde com precisão."
]
elements.append(text(530, R1 + 148, "\n".join(com_rag), 12, "#1e1e1e"))

# Bottom comparison
elements.append(rect(40, R1 + 520, 900, 70, "#f0fff4", "#b2f2bb", 2))
elements.append(text(60, R1 + 530, "🔑 RAG resolve 95% dos casos corporativos: FAQ, documentação interna, base de conhecimento, manuais técnicos.", 13, "#2f9e44"))
elements.append(text(60, R1 + 555, "💰 Mais barato que Fine-Tuning • Mais rápido • Mais fácil de atualizar • Mudou a documentação? Reindexa. Não precisa retreinar.", 12, "#1e1e1e"))

elements.append(text(480, R1 + 622, "MÓDULO 4 — SLIDE 1", 12, "#868e96"))

# --- Slide 4.2: Pipeline RAG em 5 Etapas (right) ---
elements.append(slide_bg(1100, R1, H1))
elements.append(text(1160, R1 + 20, "O Pipeline RAG em 5 Etapas", 28))
elements.append(text(1160, R1 + 58, "Da fragmentação do documento à resposta contextualizada", 14, "#868e96"))

steps = [
    ("1. Chunks", "Quebrar docs em\npedaços coerentes\n(500-1000 tokens).\nManual 500p →\ncentenas de fichas.", "#4c6ef5"),
    ("2. Embeddings", "Transformar cada\nchunk em vetor\nnumérico.\n\"Coordenadas no\nespaço semântico.\"", "#40c057"),
    ("3. Vector DB", "Armazenar vetores\nem banco otimizado.\nChroma, Pinecone,\npgvector.", "#fd7e14"),
    ("4. Similaridade", "Pergunta → embedding.\nBD acha os 3-5 chunks\nmais próximos\n(distância cosseno).", "#7950f2"),
    ("5. Injeção", "Chunks viram contexto\nno prompt. Modelo\nresponde baseado\nneles, não na memória.", "#e64980"),
]

for i, (title, desc, color) in enumerate(steps):
    x = 1140 + i * 175
    elements.append(rect(x, R1 + 105, 160, 150, "#ffffff", color, 2))
    elements.append(text(x + 8, R1 + 112, title, 14, color))
    elements.append(text(x + 8, R1 + 145, desc, 11, "#1e1e1e"))
    if i < 4:
        elements.append(arrow(x + 163, R1 + 175, 12, 0, color, 1))

# Below steps: debugging
elements.append(rect(1140, R1 + 280, 900, 130, "#fff5f5", "#ffc9c9", 1))
elements.append(text(1160, R1 + 292, "🔧 Debugging: Resposta ruim? Verifique:", 15, "#e03131"))
debug = [
    "• Chunk mal dimensionado (muito grande → perde precisão; muito pequeno → perde contexto)",
    "• Embedding de baixa qualidade (modelo errado para o domínio)",
    "• Threshold de similaridade errado (chunks irrelevantes sendo injetados)",
    "• Top-K mal calibrado (poucos chunks → falta contexto; muitos chunks → poluição)"
]
elements.append(text(1160, R1 + 320, "\n".join(debug), 11, "#1e1e1e"))

# Analogy card
elements.append(rect(1140, R1 + 430, 900, 160, "#ffffff", "#adb5bd", 1))
elements.append(text(1160, R1 + 440, "📚 Analogia da Biblioteca", 15, "#1e1e1e"))
bib = [
    "Chunks = Fichas catalográficas        Embeddings = Coordenadas da estante",
    "Vector DB = Sistema de busca           Similaridade = Encontrar livros na mesma estante",
    "Injeção = Colocar os livros abertos na mesa do aluno"
]
elements.append(text(1160, R1 + 468, "\n".join(bib), 12, "#495057"))

elements.append(text(1560, R1 + 622, "MÓDULO 4 — SLIDE 2", 12, "#868e96"))

# --- Row 1 navigation ---
elements.append(text(800, R1 + H1 + 10, "Arraste com o mouse para a direita → Slide 2", 14, "#495057"))
elements.append(arrow(1050, R1 + H1 + 15, 50, 0, "#adb5bd", 1))

# ============================================================
# ROW 2: Slides 4.3 + 4.4
# ============================================================

# --- Slide 4.3: Embeddings (left) ---
elements.append(slide_bg(20, R2, H2))
elements.append(text(60, R2 + 20, "Embeddings: Coordenadas GPS do Significado", 27))
elements.append(text(60, R2 + 58, "Transformam palavras em números. Palavras com significado parecido = coordenadas parecidas.", 14, "#868e96"))

# Central concept
elements.append(rect(40, R2 + 100, 500, 300, "#e7f5ff", "#4c6ef5", 2))
elements.append(text(60, R2 + 115, "🗺️ O Espaço Semântico", 18, "#4c6ef5"))
mapa = [
    "Cada palavra/texto é transformado em uma",
    "lista de números (ex: 768 dimensões) —",
    "são COORDENADAS no espaço do significado.",
    "",
    "Num mapa 2D (após redução com PCA):",
    "",
    "   🐕 cachorro  🐈 gato     ← próximos (pets)",
    "   🚗 carro      🏍️ moto     ← próximos (veículos)",
    "",
    "   🐕 cachorro  ...longe...  🚗 carro",
    "",
    "   👑 rei    👸 rainha       ← próximos (realeza)",
    "   👨 homem  👩 mulher       ← próximos (gênero)",
    "                ↑ mas em outra região do mapa",
    "",
    "💡 Sem embeddings, a IA trataria",
    '"automóvel" e "carro" como palavras diferentes.'
]
elements.append(text(60, R2 + 148, "\n".join(mapa), 12, "#1e1e1e"))

# Right side cards
elements.append(rect(570, R2 + 100, 410, 145, "#f0fff4", "#b2f2bb", 2))
elements.append(text(590, R2 + 115, "🌐 Aplicações Práticas", 16, "#2f9e44"))
apps = [
    "• Busca semântica em código e documentos",
    "• Recomendação de docs/base de conhecimento",
    "• Detecção de duplicatas e similaridade",
    "• Agrupamento de tickets/issues similares"
]
elements.append(text(590, R2 + 145, "\n".join(apps), 12, "#1e1e1e"))

elements.append(rect(570, R2 + 260, 410, 140, "#fff4e6", "#fd7e14", 2))
elements.append(text(590, R2 + 275, "🧪 Laboratório Prático", 16, "#fd7e14"))
lab = [
    "1. Gerar embeddings de 20 palavras",
    "2. Reduzir dimensionalidade com PCA",
    "3. Plotar em gráfico 2D",
    "4. Observar agrupamentos: animais,",
    "   objetos, profissões, verbos..."
]
elements.append(text(590, R2 + 305, "\n".join(lab), 12, "#1e1e1e"))

# Bottom
elements.append(rect(40, R2 + 420, 940, 60, "#ffffff", "#adb5bd", 1))
elements.append(text(60, R2 + 432, "💡 Embeddings são a BASE INVISÍVEL de quase toda aplicação prática de IA: busca, recomendação, classificação, agrupamento.", 13, "#495057"))

# Visualization guide
elements.append(rect(40, R2 + 500, 940, 140, "#f0fff4", "#b2f2bb", 1))
elements.append(text(60, R2 + 512, "📊 Como Visualizar (PCA): Embeddings têm 768+ dimensões → PCA reduz para 2D preservando distâncias relativas → Visualize padrões!", 13, "#2f9e44"))

elements.append(text(480, R2 + 662, "MÓDULO 4 — SLIDE 3", 12, "#868e96"))

# --- Slide 4.4: Graph RAG vs RAG Tradicional (right) ---
elements.append(slide_bg(1100, R2, H2))
elements.append(text(1160, R2 + 20, "Graph RAG: Quando Similaridade Não Basta", 27))
elements.append(text(1160, R2 + 58, "RAG tradicional busca por similaridade. Graph RAG navega por conexões entre entidades.", 14, "#868e96"))

# RAG Tradicional
elements.append(rect(1140, R2 + 100, 430, 280, "#fff4e6", "#fd7e14", 2))
elements.append(text(1160, R2 + 115, "📄 RAG Tradicional", 18, "#fd7e14"))
trad = [
    "Busca por similaridade de texto.",
    'Ex: "Quanto custa o plano X?"',
    "  → Encontra trecho com:",
    '    "plano X", "preço", "R$"',
    "",
    "✅ Funciona bem para:",
    "• FAQs e perguntas factuais",
    "• Documentação linear",
    "• Busca em manuais e guias",
    "",
    "❌ Falha em:",
    "• Perguntas com conexões complexas",
    '  "Quantos clientes do plano X',
    '   também usam o produto Y?"',
    "",
    'Analogia: Buscar "restaurante italiano"',
    "no Google."
]
elements.append(text(1160, R2 + 148, "\n".join(trad), 12, "#1e1e1e"))

# Graph RAG
elements.append(rect(1610, R2 + 100, 430, 280, "#f3f0ff", "#7950f2", 2))
elements.append(text(1630, R2 + 115, "🕸️ Graph RAG", 18, "#7950f2"))
graph = [
    "Monta um grafo de conhecimento:",
    "  • Entidades = nós",
    "  • Relacionamentos = arestas",
    "  • Navega com Cypher (Neo4j)",
    "",
    "✅ Funciona bem para:",
    "• Domínios com muitas conexões",
    "• Catálogos com dependências",
    "• APIs com compatibilidade",
    "• Grafos de conhecimento corporativos",
    "",
    'Ex: "Restaurantes italianos a menos de',
    '1km, abertos agora, nota > 4.5"',
    "  → Cada condição é uma aresta no grafo",
    "",
    "Analogia: Busca multi-hop em um mapa",
    "de conexões."
]
elements.append(text(1630, R2 + 148, "\n".join(graph), 12, "#1e1e1e"))

# Decision guidance
elements.append(rect(1140, R2 + 400, 900, 80, "#f0fff4", "#b2f2bb", 2))
elements.append(text(1160, R2 + 412, "🎯 Quando Usar Cada Um:", 15, "#2f9e44"))
elements.append(text(1160, R2 + 438, "RAG Tradicional → FAQs, manuais, documentação linear.    |    Graph RAG → Catálogos com dependências, APIs interligadas, grafos corporativos.", 12, "#1e1e1e"))

elements.append(rect(1140, R2 + 500, 900, 140, "#ffffff", "#adb5bd", 1))
elements.append(text(1160, R2 + 512, "📈 Tendência: Sistemas híbridos usam RAG tradicional para busca inicial + Graph RAG para navegação entre entidades relacionadas.", 12, "#495057"))

elements.append(text(1560, R2 + 662, "MÓDULO 4 — SLIDE 4", 12, "#868e96"))

# --- Row 2 navigation ---
elements.append(text(820, R2 + H2 + 10, "Arraste para baixo para ver o Slide 5", 13, "#495057"))
elements.append(arrow(960, R2 + H2 + 15, 0, 30, "#adb5bd", 1))

# ============================================================
# ROW 3: Slide 4.5 — Engenharia de Contexto (left only)
# ============================================================

elements.append(slide_bg(20, R3, H3))
elements.append(text(60, R3 + 20, "Engenharia de Contexto e a Regra dos 40%", 28))
elements.append(text(60, R3 + 58, "A qualidade do contexto impacta mais que o modelo ou o prompt escolhido", 14, "#868e96"))

# Strip 1: Contexto é o maior diferencial
elements.append(rect(40, R3 + 100, 920, 140, "#f0fff4", "#b2f2bb", 2))
elements.append(text(60, R3 + 115, "🎯 Contexto é o Maior Diferencial", 18, "#2f9e44"))
elements.append(text(60, R3 + 148, "Mais que o modelo escolhido. Contexto RUIM + GPT-4o perde para contexto BOM + GPT-3.5.\nO contexto certo transforma a mesma pergunta e o mesmo modelo em resultados completamente diferentes.", 13, "#1e1e1e"))

# Strip 2: Regra dos 40%
elements.append(rect(40, R3 + 260, 920, 140, "#e7f5ff", "#4c6ef5", 2))
elements.append(text(60, R3 + 275, "📏 A Regra dos 40%", 18, "#4c6ef5"))
elements.append(text(60, R3 + 308, "Use no MÁXIMO 40% da janela de contexto. Se o modelo suporta 200K tokens, mantenha abaixo de 80K.\nAcima disso, o modelo degrada — igual você tentando ler 10 livros ao mesmo tempo.\nO modelo começa a \"esquecer\" informações no meio e prioriza o início e o fim do contexto.", 13, "#1e1e1e"))

# Strip 3: Progressive Disclosure
elements.append(rect(40, R3 + 420, 920, 140, "#fff4e6", "#fd7e14", 2))
elements.append(text(60, R3 + 435, "🔍 Progressive Disclosure", 18, "#fd7e14"))
elements.append(text(60, R3 + 468, "Carrega só o necessário, só quando necessário. Como um garçom que traz só o prato, não o cardápio inteiro.\nComece com contexto mínimo → se a resposta não for boa, adicione mais detalhes → itere até a qualidade ideal.\nIsso mantém o contexto enxuto e a qualidade alta.", 13, "#1e1e1e"))

# Analogy
elements.append(rect(40, R3 + 580, 920, 40, "#ffffff", "#adb5bd", 1))
elements.append(text(60, R3 + 590, "🪑 Analogia da Mesa de Trabalho: 50 documentos = caos (IA alucina). 3 documentos relevantes = foco total (IA acerta).", 13, "#495057"))

elements.append(text(480, R3 + 622, "MÓDULO 4 — SLIDE 5", 12, "#868e96"))

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

out_path = "/home/estrazulas/git/docs_capacitacao_ia/excalidraw/modulo-04-rag-embeddings.excalidraw"
with open(out_path, "w") as f:
    json.dump(doc, f, indent=2, ensure_ascii=False)

print(f"✅ {out_path}")
print(f"   {len(elements)} elementos em 5 slides")
