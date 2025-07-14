### Documentos:
https://github.com/adriana-muller-br/integracao-bpm-com-ia/blob/main/docs/1-llm.md


### Instale:

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

pip install fastapi uvicorn openai streamlit requests

```

### Abra um prompt e execute:
```bash
uvicorn main:app --reload
```

### Abra outro prompt e execute:
```bash
streamlit run simulador_bpm.py
```

### Acesse
http://localhost:8501/