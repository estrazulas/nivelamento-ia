#!/usr/bin/env python3
"""Build the vLLM vs llama.cpp comparison diagram with OpenCode integration."""

import json, os

NOW = "2026-07-09T14:30:00.000Z"
FONT = 2  # Helvetica

_seed = [200000]
_vn = [300000]

def _ns():
    _seed[0] += 1; return _seed[0]
def _nv():
    _vn[0] += 1; return _vn[0]

def _base(t, x, y):
    return {"type":t,"x":x,"y":y,"angle":0,"opacity":100,"roundness":None,
            "boundElements":None,"groupIds":[],"frameId":None,"isDeleted":False,
            "locked":False,"seed":_ns(),"versionNonce":_nv(),"updated":NOW,
            "createdAt":NOW,"version":1}

def rect(x, y, w, h, bg, sc="#1e1e1e", sw=1):
    el = _base("rectangle", x, y)
    el.update({"width":w,"height":h,"fillStyle":"solid","strokeWidth":sw,
               "strokeColor":sc,"backgroundColor":bg,"roughness":0})
    return el

def text(x, y, txt, fs=16, sc="#1e1e1e", ta="left"):
    lines = txt.split("\n")
    mc = max(len(l) for l in lines) if lines else 0
    w = mc * fs * 0.58 + 16
    h = len(lines) * fs * 1.35 + 8
    el = _base("text", x, y)
    el.update({"width":round(w),"height":round(h),"fontFamily":FONT,"fontSize":fs,
               "text":txt,"textAlign":ta,"verticalAlign":"top","autoResize":True,
               "lineHeight":1.25,"strokeColor":sc})
    return el

def arrow(x, y, pts, sc="#333", sw=1):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    el = _base("arrow", x, y)
    el.update({"width":max(max(xs)-min(xs),1),"height":max(max(ys)-min(ys),0),
               "points":pts,"startArrowhead":None,"endArrowhead":"arrow",
               "startBinding":None,"endBinding":None,"lastCommittedPoint":None,
               "strokeColor":sc,"backgroundColor":"transparent","fillStyle":"solid",
               "strokeWidth":sw,"roughness":0})
    return el

def ctext(rx, ry, rw, rh, txt, fs=16, sc="#1e1e1e"):
    """Center text inside a rectangle."""
    lines = txt.split("\n")
    mc = max(len(l) for l in lines) if lines else 0
    tw = mc * fs * 0.58 + 16
    th = len(lines) * fs * 1.35 + 8
    return text(round(rx+(rw-tw)/2), round(ry+(rh-th)/2), txt, fs, sc,
                "center" if len(lines)==1 else "left")

# ═══════════════════════════════════════════════════════════════════════════
# LAYOUT
# ═══════════════════════════════════════════════════════════════════════════

L = 50   # Left column x
R = 630  # Right column x
COL_W = 520
BG_H = 780  # Taller to fit OpenCode section

elements = []

# ╔══════════════════════════════════════════════════════════════════════════
# ║ LEFT — DESENVOLVIMENTO
# ╚══════════════════════════════════════════════════════════════════════════

elements.append(rect(L, 50, COL_W, BG_H, "#e8f5e9", "#2e7d32", 2))
elements.append(text(L+40, 70, "🏠 SUA MÁQUINA (Desenvolvimento)", 22, "#2e7d32"))

# ── Terminal ──
elements.append(text(L+25, 115, "$ opencode", 15, "#555"))
elements.append(text(L+25, 137, '  → provider: "ollama"', 14, "#888"))
elements.append(text(L+25, 157, '  → model: "llama3.1:8b"', 14, "#888"))

# Arrow from terminal to Ollama
elements.append(arrow(L+260, 145, [[0,0],[55,0]], "#666"))

# ── Ollama box ──
ox, oy, ow, oh = L+150, 200, 200, 50
elements.append(rect(ox, oy, ow, oh, "#c8e6c9", "#388e3c", 1))
elements.append(ctext(ox, oy, ow, oh, "Ollama", 18, "#2e7d32"))

# Arrow
elements.append(arrow(L+250, 250, [[0,0],[0,40]], "#666"))
elements.append(text(L+265, 258, "empacota →", 12, "#888"))

# ── llama.cpp ──
lx, ly, lw, lh = L+150, 290, 200, 50
elements.append(rect(lx, ly, lw, lh, "#ffe0b2", "#f57c00", 1))
elements.append(ctext(lx, ly, lw, lh, "llama.cpp (motor)", 17, "#e65100"))

# Arrow
elements.append(arrow(L+250, 340, [[0,0],[0,40]], "#666"))

# ── Modelo ──
mx, my, mw, mh = L+150, 380, 200, 60
elements.append(rect(mx, my, mw, mh, "#e1bee7", "#6a1b9a", 1))
elements.append(ctext(mx, my, mw, mh, "Modelo\nLlama 3.1 8B (4.7 GB)", 14, "#4a148c"))
elements.append(text(L+365, 390, "→ sua RAM", 13, "#888"))

# ── API local ──
elements.append(arrow(L+250, 440, [[0,0],[0,30]], "#666"))
apix, apiy, apiw, apih = L+130, 473, 240, 40
elements.append(rect(apix, apiy, apiw, apih, "#c8e6c9", "#388e3c", 1))
elements.append(ctext(apix, apiy, apiw, apih, "localhost:11434 (API OpenAI-compat)", 14, "#2e7d32"))

# ── Request/Response ──
elements.append(text(L+25, 535, '📥 Prompt: "Explique SQL injection"', 14, "#333"))
elements.append(arrow(L+250, 555, [[0,0],[0,25]], "#666"))
elements.append(text(L+25, 583, '📤 Resposta: "SQL injection é um ataque..."', 14, "#333"))

# ── Limitações ──
limx, limy, limw, limh = L+10, 630, 500, 100
elements.append(rect(limx, limy, limw, limh, "#ffebee", "#c62828", 1))
elements.append(text(limx+15, limy+8, "⚠️ Limitações:", 15, "#c62828"))
elements.append(text(limx+15, limy+30, "• 1 requisição por vez — 2ª espera", 14, "#555"))
elements.append(text(limx+15, limy+52, "• Sem fila, sem prioridade, sem escala", 14, "#555"))
elements.append(text(limx+15, limy+74, "• Ideal para: testar prompts, desenvolver, brincar", 14, "#555"))

# ── OpenCode config (left) ──
ocx, ocy, ocw, och = L+10, 748, 500, 68
elements.append(rect(ocx, ocy, ocw, och, "#fff3e0", "#e65100", 1))
elements.append(text(ocx+15, ocy+6, "🔧 Config no OpenCode (~/.config/opencode/config.json):", 13, "#e65100"))
elements.append(text(ocx+15, ocy+28, '"ollama": { "baseUrl": "http://localhost:11434/v1",', 13, "#555"))
elements.append(text(ocx+15, ocy+48, '  "model": "llama3.1:8b", "apiKey": "ollama" }', 13, "#555"))

# ╔══════════════════════════════════════════════════════════════════════════
# ║ RIGHT — PRODUÇÃO
# ╚══════════════════════════════════════════════════════════════════════════

elements.append(rect(R, 50, COL_W, BG_H, "#e3f2fd", "#1565c0", 2))
elements.append(text(R+60, 70, "🏭 DATACENTER (Produção)", 22, "#1565c0"))

# ── Users ──
elements.append(text(R+60, 115, "👥 👥 👥 👥 👥  1000+ devs simultâneos", 15, "#555"))

# ── Load Balancer ──
lbx, lby, lbw, lbh = R+120, 160, 280, 45
elements.append(rect(lbx, lby, lbw, lbh, "#bbdefb", "#1565c0", 1))
elements.append(ctext(lbx, lby, lbw, lbh, "🌐 Load Balancer (NGINX)", 16, "#0d47a1"))

# Two arrows from LB to workers
elements.append(arrow(R+190, 205, [[0,0],[-60,80]], "#666"))
elements.append(arrow(R+330, 205, [[0,0],[60,80]], "#666"))

# ── vLLM Workers ──
w1x, w1y, w1w, w1h = R+50, 290, 180, 70
elements.append(rect(w1x, w1y, w1w, w1h, "#90caf9", "#1565c0", 1))
elements.append(ctext(w1x, w1y, w1w, w1h, "🖥️ vLLM Worker 1\nGPU 0", 15, "#0d47a1"))

w2x, w2y, w2w, w2h = R+270, 290, 180, 70
elements.append(rect(w2x, w2y, w2w, w2h, "#90caf9", "#1565c0", 1))
elements.append(ctext(w2x, w2y, w2w, w2h, "🖥️ vLLM Worker 2\nGPU 1", 15, "#0d47a1"))

# Arrows from workers to GPU model
elements.append(arrow(R+140, 360, [[0,0],[0,45]], "#666"))
elements.append(arrow(R+360, 360, [[0,0],[0,45]], "#666"))

# ── GPU Model ──
gx, gy, gw, gh = R+70, 410, 360, 80
elements.append(rect(gx, gy, gw, gh, "#e1bee7", "#6a1b9a", 1))
elements.append(ctext(gx, gy, gw, gh,
    "🧠 Modelo carregado nas GPUs\nLlama 3.1 70B — 40 GB — 2× A100 80GB\nCompartilhado entre todos os workers", 14, "#4a148c"))

# ── API endpoint ──
elements.append(arrow(R+250, 490, [[0,0],[0,30]], "#666"))
ap2x, ap2y, ap2w, ap2h = R+90, 523, 320, 40
elements.append(rect(ap2x, ap2y, ap2w, ap2h, "#bbdefb", "#1565c0", 1))
elements.append(ctext(ap2x, ap2y, ap2w, ap2h, "vllm-server:8000/v1 (API OpenAI-compat)", 14, "#0d47a1"))

# ── Batching explanation ──
elements.append(text(R+40, 580, "Requisições chegam: A, B, C, D, E, F...", 14, "#555"))
elements.append(arrow(R+250, 600, [[0,0],[0,30]], "#666"))

batx, baty, batw, bath = R+30, 635, 460, 130
elements.append(rect(batx, baty, batw, bath, "#c8e6c9", "#2e7d32", 1))
elements.append(text(batx+15, baty+8, "✅ Continuous Batching", 15, "#2e7d32"))
elements.append(text(batx+15, baty+30, "vLLM junta requisições compatíveis (A+C) e processa em paralelo.", 13, "#555"))
elements.append(text(batx+15, baty+50, "✅ PagedAttention", 15, "#2e7d32"))
elements.append(text(batx+15, baty+72, "Memória da GPU dividida em páginas → sem fragmentação → + throughput.", 13, "#555"))
elements.append(text(batx+15, baty+92, "✅ Respostas fora de ordem (C, A, E, B...) mas cada cliente recebe no socket certo.", 13, "#555"))

# ── OpenCode config (right) ──
oc2x, oc2y, oc2w, oc2h = R+10, 780, 500, 50
elements.append(rect(oc2x, oc2y, oc2w, oc2h, "#fff3e0", "#e65100", 1))
elements.append(text(oc2x+15, oc2y+6, "🔧 Config no OpenCode (~/.config/opencode/config.json):", 13, "#e65100"))
elements.append(text(oc2x+15, oc2y+28, '"vllm": { "baseUrl": "http://vllm-server:8000/v1", "model": "llama-3.1-70b", "apiKey": "not-needed" }', 13, "#555"))

# ╔══════════════════════════════════════════════════════════════════════════
# ║ BOTTOM — RESUMO
# ╚══════════════════════════════════════════════════════════════════════════

sy = BG_H + 70
sx, sw, sh = L, 1100, 130
elements.append(rect(sx, sy, sw, sh, "#fff9c4", "#f9a825", 2))
elements.append(text(sx+20, sy+8, "🔑 A DIFERENÇA CENTRAL", 18, "#333"))
elements.append(text(sx+20, sy+35, "llama.cpp = MOTOR. Roda o modelo. 1 requisição por vez. Feito para CPU. Ótimo para testar local.", 14, "#555"))
elements.append(text(sx+20, sy+57, "Ollama    = EMPACOTADOR do llama.cpp. Torna fácil com 1 comando. Uso: desenvolvimento.", 14, "#555"))
elements.append(text(sx+20, sy+79, "vLLM      = MOTOR + ORQUESTRADOR. Gerencia GPU, fila, memória, paralelismo. 1000x mais vazão. Uso: produção.", 14, "#555"))
elements.append(text(sx+20, sy+101, "OpenCode  = conecta nos DOIS. Basta trocar a URL no config. Mesma API → mesmo código.", 14, "#e65100"))

# ── Write ────────────────────────────────────────────────────────────────

doc = {
    "type": "excalidraw", "version": 2,
    "source": "https://excalidraw.com",
    "elements": elements,
    "appState": {
        "viewBackgroundColor": "#ffffff", "gridSize": None,
        "scrollX": 0, "scrollY": 0,
        "zoom": {"value": 0.62},
        "activeTool": {"type":"selection","customType":None,"locked":False,"lastActiveTool":None},
    },
    "files": {},
}

out = os.path.join(os.path.dirname(__file__), "vllm-vs-llamacpp.excalidraw")
with open(out, "w", encoding="utf-8") as f:
    json.dump(doc, f, indent=2, ensure_ascii=False)

counts = {}
for e in elements: counts[e["type"]] = counts.get(e["type"], 0) + 1
print(f"✅ Saved {len(elements)} elements to {out}")
print(f"   Types: {counts}")
