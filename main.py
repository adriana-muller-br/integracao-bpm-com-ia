from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

# Inicializa o cliente OpenAI com a chave da API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI(title="Validador IA de Justificativas")

class SolicitacaoMudanca(BaseModel):
    justificativa: str

PROMPT_BASE = """
Você é um analista de qualidade responsável por validar justificativas de mudança de software. A justificativa precisa ser:
- Clara e objetiva
- Explicar o motivo da mudança
- Informar o impacto e o benefício esperado
- Estar escrita de forma técnica e profissional

A seguir, avalie a justificativa fornecida e diga se está adequada. Se não estiver, sugira melhorias.

Justificativa: "{justificativa}"
"""

@app.post("/validar")
async def validar_justificativa(dados: SolicitacaoMudanca):
    prompt = PROMPT_BASE.format(justificativa=dados.justificativa)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um analista de validação de mudanças."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
            max_tokens=300
        )
        parecer = response.choices[0].message.content.strip()
        return {"status": "ok", "parecer": parecer}

    except Exception as e:
        return {"status": "erro", "detalhe": str(e)}
