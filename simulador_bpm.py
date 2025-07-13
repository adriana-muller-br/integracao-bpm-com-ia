import streamlit as st
import requests

API_URL = "http://localhost:8000/validar"

st.title("Simulador BPM - Validação de Justificativa de Mudança")

justificativa = st.text_area("Justificativa da mudança:", height=200)

if st.button("Enviar para validação IA"):
    if not justificativa.strip():
        st.warning("Preencha a justificativa antes de enviar.")
    else:
        with st.spinner("Enviando para validação..."):
            resposta = requests.post(API_URL, json={"justificativa": justificativa})
            if resposta.status_code == 200:
                parecer = resposta.json().get("parecer")
                st.success("Parecer da IA:")
                st.write(parecer)
            else:
                st.error(f"Erro: {resposta.text}")
