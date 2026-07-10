# Ollama vs llama.cpp vs vLLM — Explicação para Leigos

> Diagrama: `vllm-vs-llamacpp.excalidraw`

---

## 1. llama.cpp — o "motorzinho"

Imagina que o modelo de IA é um **motor de carro**. O llama.cpp é um motor 1.0 — ele faz o carro andar, mas foi feito para ser **leve e simples**. Você instala no seu notebook, dá partida, e ele anda. Só que ele só leva **1 pessoa por vez**. Se chegar outra, espera.

**Por que existe?** Porque roda em CPU (sem placa de vídeo cara). Um modelo de 8 bilhões de parâmetros (~4.7 GB) roda até num MacBook Air.

**Não é um servidor.** É uma biblioteca C++ que carrega o modelo e processa um prompt por vez.

---

## 2. Ollama — a "carenagem bonita"

O llama.cpp é pelado — você precisaria compilar C++, baixar o modelo manualmente, configurar flags. O **Ollama** é uma carenagem que envolve o llama.cpp: você digita `ollama run llama3` e tudo acontece.

```
Usuário → Ollama (interface amigável) → llama.cpp (motor real) → Modelo
```

- Expõe API REST em `localhost:11434`
- Formato compatível com OpenAI (`/v1/chat/completions`)
- Baixa o modelo automaticamente do registro do Ollama
- **Feito para desenvolvimento local, não produção**

---

## 3. vLLM — o "motor de fábrica"

O vLLM também faz a IA responder, mas foi feito para **fábrica, não garagem**. Imagina uma montadora: 1000 pedidos chegando ao mesmo tempo.

### Tecnicalidades (explicadas para devs)

| Técnica | Problema que resolve | Analogia |
|---------|---------------------|----------|
| **Continuous Batching** | 1 requisição por vez desperdiça GPU | Em vez de fazer 1 hambúrguer por vez, grelha vários de uma vez |
| **PagedAttention** | Memória da GPU fragmenta | Memória virtual do SO — divide em páginas, evita buracos |
| **Tensor Parallelism** | Modelo não cabe em 1 GPU | Divide o modelo entre 2+ GPUs como `model.to(device)` no PyTorch |

### Como montar num datacenter (visão macro)

```
                        INTERNET
                           │
                           ▼
                ┌──────────────────┐
                │  NGINX / Envoy   │  ← Load Balancer
                │  (proxy reverso) │     Distribui tráfego
                └──────┬───────────┘
                       │
           ┌───────────┼───────────┐
           ▼           ▼           ▼
    ┌──────────┐ ┌──────────┐ ┌──────────┐
    │ vLLM #1  │ │ vLLM #2  │ │ vLLM #3  │  ← Servidores com GPU
    │ GPU 0,1  │ │ GPU 2,3  │ │ GPU 4,5  │     Cada um com
    │          │ │          │ │          │     cópia do modelo
    └──────────┘ └──────────┘ └──────────┘
           │           │           │
           └───────────┼───────────┘
                       │
                       ▼
             O MODELO É O MESMO
             (Llama 70B carregado
             em cada servidor)
```

| # | O que | Comando/Detalhe |
|---|-------|-----------------|
| 1 | Aluga GPUs | 2× NVIDIA A100 80GB no AWS (`p4d.24xlarge`) ou Lambda Labs |
| 2 | Instala vLLM | `pip install vllm` |
| 3 | Baixa o modelo | Hugging Face → `meta-llama/Llama-3.1-70B` |
| 4 | Sobe o vLLM | `vllm serve meta-llama/Llama-3.1-70B --tensor-parallel-size 2` |
| 5 | NGINX na frente | Distribui entre múltiplos servidores vLLM |
| 6 | **OpenCode conecta** | `"baseUrl": "http://vllm-server:8000/v1"` |

**Custo:** Uma A100 na cloud ~US$ 1-3/hora. Duas A100 24/7 ≈ US$ 3.000-5.000/mês.

---

## 4. OpenCode — conectando nos dois mundos

O ponto mais importante: **o código é o mesmo**. Tanto Ollama quanto vLLM expõem API compatível com OpenAI.

### Desenvolvimento (sua máquina)

```json
// ~/.config/opencode/config.json
{
  "ollama": {
    "baseUrl": "http://localhost:11434/v1",
    "model": "llama3.1:8b",
    "apiKey": "ollama"
  }
}
```

```bash
ollama pull llama3.1:8b   # uma vez
opencode                   # conecta no Ollama automaticamente
```

### Produção (datacenter)

```json
// ~/.config/opencode/config.json
{
  "vllm": {
    "baseUrl": "http://vllm-server.internal:8000/v1",
    "model": "llama-3.1-70b",
    "apiKey": "not-needed"
  }
}
```

```bash
# No servidor:
vllm serve meta-llama/Llama-3.1-70B \
  --tensor-parallel-size 2 \
  --max-model-len 8192 \
  --port 8000

# Na sua máquina:
opencode --provider vllm
```

### Por que isso importa

O dev testa local com Ollama (grátis, rápido, sem internet). Quando o prompt está pronto, sobe para produção com vLLM (escala, GPU, dezenas de devs simultâneos). **Zero mudança no código.**

---

## 5. Resumo de 1 frase

> **Ollama = `npm run dev` | vLLM = `nginx + gunicorn + workers` | Mesma API → mesmo código.**
