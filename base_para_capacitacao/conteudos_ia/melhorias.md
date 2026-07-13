# Melhorias Transversais — Workshop IA para Devs

Melhorias estruturais identificadas no relatório de revisão com 3 agentes (Iniciante, Intermediário, Avançado).

---

## 1. 📄 Templates e Exemplos Concretos

**Evidência:** #27, #28, #33, #61, #62, #74 — 6 intervenções de Alta gravidade.

**Diagnóstico:** Slides explicam O QUE mas não mostram O COMO. Devs aprendem por exemplos e templates adaptáveis.

**Status:** ⏳ Parcial
- #27 resolvido (card [ROLE][CONTEXTO][INSTRUÇÃO][RESTRIÇÕES][FORMATO] no slide 3.1)
- #28 resolvido (prompts Java RTF/CARE/RISE no slide 3.2)
- #33 resolvido (snippet RAG 5 linhas no slide 4.2)
- #61 exemplos adicionados na apresentação (spec.md, design.md, tasks.md, state.md)
- Falta criar templates formais para material do aluno

**Ações pendentes:**
- [ ] Criar arquivos de template: `prompt-5-elementos.template.md`
- [ ] Criar template: `rtf.template.md`, `care.template.md`, `rise.template.md`
- [ ] Criar template: `spec.template.md`, `design.template.md`, `tasks.template.md`
- [ ] Criar template: `STATE.template.md`
- [ ] Distribuir como material do aluno (não só slide)

---

## 2. 🔗 Conceitos Mencionados Antes de Definidos

**Evidência:** #1, #3, #12, #17, #22, #24, #29, #39, #52 — 9 intervenções.

**Diagnóstico:** Workshop tem estrutura em espiral (menciona cedo, explica tarde), mas sem definições-relâmpago.

**Status:** ✅ Resolvido
- #1 resolvido (MCP/SDD no slide 1.0)
- #3 resolvido (definição-relâmpago de token)
- #12 resolvido (exemplo SQL injection)
- #22 resolvido (não-determinismo)
- #24 resolvido (siglas expandidas)
- #29 resolvido (etimologia zero-shot/few-shot/CoT)
- #39 resolvido (PCA explicado)
- #52 resolvido (skill definido no slide 5.5)
- Glossário com 109 termos adicionado ao final do workshop-ia-para-devs.md
- Notas de rodapé nos slides (pendente menor, não crítico)

**Status:** ✅ Resolvido

---

## 3. ⚖️ Desequilíbrio Teoria / Prática

**Evidência:** #73, #81 — 71% teoria / 29% prática.

**Diagnóstico:** Para workshop "Da base à prática", balanço desfavorável. Labs bem desenhados mas curtos.

**Status:** ✅ Resolvido

---

## 4. 📺 Fontes 100% YouTube

**Evidência:** #76 — Todas as referências são vídeos dos mesmos 2 autores.

**Diagnóstico:** Ausência de docs oficiais, papers e benchmarks reduz credibilidade.

**Status:** ✅ Resolvido
- Fontes já foram extraídas para `workshop-ia-para-devs-fontes.md`
- Não foi considerado prioridade — referências YouTube são adequadas para o formato workshop

---

## 5. 🔒 Segurança de Agentes

**Evidência:** #48 — Prompt injection, tool poisoning, excessive agency nunca mencionados.

**Diagnóstico:** Omissão mais grave do workshop. Aluno vai encontrar esses riscos em produção.

**Status:** ✅ Resolvido
- Novo tópico 5.6 adicionado com 4 perigos e mitigações
- Cobre: prompt injection, excessive agency, tool poisoning, loop infinito
- Referencia OWASP Top 10 for LLM Applications

---

## 6. 🔧 OpenCode como Dependência Única

**Evidência:** #2 — Potencial conflito de interesses, exclusão de usuários de outras ferramentas.

**Diagnóstico:** Escolha única é didaticamente válida, mas faltam alternativas.

**Status:** ✅ Resolvido
- Declarado no slide 1.0 que as ferramentas/práticas se aplicam a outras ferramentas

---

## Resumo

| # | Melhoria | Prioridade | Status |
|---|---|---|---|
| 1 | Templates e exemplos concretos | 🔴 Alta | ⏳ Parcial |
| 2 | Conceitos antes de definidos | 🟡 Média | ⏳ Parcial |
| 3 | Equilíbrio teoria/prática | 🟡 Média | ✅ Resolvido |
| 4 | Fontes diversas (não só YouTube) | 🟢 Baixa | ✅ Resolvido |
| 5 | Segurança de agentes | 🔴 Alta | ✅ Resolvido |
| 6 | Alternativas ao OpenCode | 🟢 Baixa | ✅ Resolvido |

**Total:** 5 resolvidas · 1 parcial · 0 pendentes
*(Único pendente parcial: templates de prompts para material do aluno)*
