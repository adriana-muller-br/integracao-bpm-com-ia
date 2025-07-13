## 📘 O que é uma LLM (Large Language Model)?

**LLM (Large Language Model)** é um modelo de linguagem treinado com uma enorme quantidade de textos (livros, sites, artigos, etc.) para **entender, gerar e manipular linguagem natural**. Exemplos famosos são o **GPT (da OpenAI)**, o **Claude (da Anthropic)** e o **Gemini (do Google)**.

### Características:

* Usa **técnicas de deep learning**, especialmente redes neurais transformadoras (Transformers).
* **Gera texto** em linguagem natural com coerência, podendo responder perguntas, criar conteúdo, traduzir, resumir e muito mais.
* Funciona **por previsão de próxima palavra/token**, ajustando seu output com base no contexto da conversa ou instrução.

### Exemplos de uso:

* Chatbots conversacionais (ex: ChatGPT)
* Assistentes de escrita e resumo
* Análise semântica de textos
* Automação de atendimento ao cliente
* Extração de insights em grandes volumes de documentos

---

## 🧠 O que é um agente de IA?

Um **agente de IA** é uma entidade (software/sistema) que:

1. **Percebe** o ambiente (inputs),
2. **Toma decisões** com base em regras, lógica, ou IA,
3. **Executa ações** para atingir um objetivo.

Quando falamos de **agentes com LLMs**, entramos no campo dos **Agentes Autônomos de IA**, ou simplesmente **IA Agente**, que combinam uma LLM com ferramentas e memória para **executar tarefas complexas por conta própria**.

### Exemplo de Agente com LLM:

Imagine um assistente virtual com as seguintes capacidades:

* Recebe uma tarefa: *"Analisar e resumir 10 PDFs de relatórios financeiros"*
* Decide como realizar (abrir PDFs, ler, extrair dados relevantes, resumir)
* Usa ferramentas externas (API de leitura de PDF, armazenamento em nuvem)
* Se necessário, pede ajuda ao humano (por meio de prompts)
* Entrega o resumo final em formato Word e envia por e-mail

### Componentes típicos de um agente de IA:

* **LLM (como cérebro)**: geração de texto, planejamento, tomada de decisões
* **Ferramentas (plugins, APIs, bancos de dados)**: para agir no mundo externo
* **Memória**: para lembrar de interações passadas ou estados persistentes
* **Objetivos**: definidos por humanos ou inferidos do contexto

---

## 🔁 Diferença entre LLM e Agente de IA

| Aspecto    | LLM                             | Agente de IA                                                |
| ---------- | ------------------------------- | ----------------------------------------------------------- |
| Papel      | Núcleo de linguagem             | Executor inteligente de tarefas                             |
| Foco       | Entendimento e geração de texto | Planejamento e ação                                         |
| Depende de | Dados de texto                  | LLM + ferramentas + memória                                 |
| Exemplo    | ChatGPT básico                  | Agente autônomo que agenda reuniões e envia e-mails sozinho |

---