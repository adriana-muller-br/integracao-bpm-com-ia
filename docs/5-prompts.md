## ✅ **Quando 1 Prompt Único é Suficiente**

Um único prompt pode funcionar bem **quando o passo do fluxo é específico e isolado**, por exemplo:

> ➤ “Valide o campo *Justificativa da Mudança* de acordo com os critérios da política XYZ.”

Nesse caso, você coloca:

* O papel da IA (auditor, revisor, etc.)
* As instruções do que é aceitável
* Exemplos de boas e más justificativas (opcional)
* O campo em questão

🟢 **Vantagem**: mais simples de manter, fácil de testar e ajustar.

---

## 🔀 **Quando Múltiplos Prompts são Recomendados**

Se o seu fluxo envolve validações diferentes, como:

1. **Campo "Justificativa"** → clareza e objetividade
2. **Campo "Plano de Rollback"** → existência de etapas técnicas coerentes
3. **Evidências em anexo** → se o conteúdo confirma a homologação
4. **Ambiente selecionado** → se segue o processo correto

A recomendação é criar **prompts separados**, algo como:

```text
[PROMPT_1] Avalie a justificativa da mudança conforme os critérios da política ABC.
[PROMPT_2] Avalie o plano de rollback e se ele cobre os riscos principais.
[PROMPT_3] Analise o PDF anexo e verifique se apresenta evidência de execução de testes em ambiente de homologação.
```

Esses prompts são chamados de **“modularizados por tarefa”**.

🟢 **Vantagem**:

* Clareza e foco em cada validação
* Permite reaproveitar em outros fluxos ou contextos
* Melhor controle de erro e ajuste fino

---

## 🧠 Estratégia híbrida (Recomendada)

Você pode usar um **prompt genérico como controlador**, que invoca sub-prompts conforme o passo do fluxo. Exemplo:

```text
Você é um assistente de validação de mudanças de software.
Com base no tipo de etapa abaixo, aplique os critérios específicos:
- Se for "justificativa", siga o conjunto de regras A.
- Se for "rollback", siga o conjunto B.
...
A seguir, o tipo de etapa é: "justificativa"
Texto a ser avaliado: ...
```

Ou então, estruturar isso no código:

```python
if etapa == "justificativa":
    prompt = PROMPT_JUSTIFICATIVA
elif etapa == "rollback":
    prompt = PROMPT_ROLLBACK
```

---

## 📌 Conclusão

| Situação                                 | Melhor estratégia                |
| ---------------------------------------- | -------------------------------- |
| Validação simples e única                | 1 prompt customizado             |
| Etapas variadas com critérios diferentes | Prompts por tipo de passo        |
| Escalabilidade e controle fino           | Prompts modularizados por tarefa |

---