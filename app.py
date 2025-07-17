# app.py

import streamlit as st
import pandas as pd
import joblib

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Decision - IA para Recrutamento",
    page_icon="🤖",
    layout="centered"
)

# 2. CARREGAMENTO DO MODELO
@st.cache_resource
def load_model(model_path):
    try:
        model = joblib.load(model_path)
        return model
    except FileNotFoundError:
        st.error(f"Erro: Arquivo do modelo '{model_path}' não encontrado.")
        st.error("Por favor, execute o notebook de treinamento para gerar o arquivo do modelo.")
        return None

model = load_model('recruitment_model.joblib')

# 3. INTERFACE DO USUÁRIO (UI)
st.title("🤖 Análise Preditiva de Match Vaga-Candidato")
st.markdown("""
Esta ferramenta utiliza Inteligência Artificial para calcular a probabilidade de um candidato ser compatível com uma vaga, com base nos dados históricos de sucesso da **Decision**.
1. Preencha os dados na barra lateral à esquerda.
2. Cole o currículo do candidato.
3. Clique em **Verificar Match**!
""")

st.sidebar.header("Insira os Dados para Análise")

def user_input_features():
    st.sidebar.subheader("Sobre a Vaga")
    vaga_nivel_profissional = st.sidebar.selectbox('Nível Profissional:', ('Analista', 'Sênior', 'Especialista', 'Consultor', 'Gerente', 'Diretor', 'Estagiário', 'Não informado'))
    remuneracao_cleaned = st.sidebar.number_input('Remuneração (R$)', min_value=0, max_value=50000, value=5000, step=500)
    recrutador = st.sidebar.selectbox('Recrutador:', ('Ana Lívia Moreira', 'Elisa Nunes', 'Maria Eduarda Cassiano', 'Laura Pacheco', 'Outro'))

    st.sidebar.subheader("Sobre o Candidato")
    applicant_nivel_academico = st.sidebar.selectbox('Nível Acadêmico:', ('Ensino Superior Completo', 'Pós-graduação', 'Ensino Superior Incompleto', 'Ensino Médio', 'Mestrado', 'Doutorado', 'Não informado'))
    
    st.sidebar.subheader("Currículo (CV)")
    cv_pt = st.sidebar.text_area("Cole aqui o CV completo do candidato...", height=250)

    data = {
        'remuneracao_cleaned': remuneracao_cleaned,
        'tempo_processo_dias': 10,
        'vaga_nivel_profissional': vaga_nivel_profissional,
        'applicant_nivel_academico': applicant_nivel_academico,
        'recrutador': recrutador,
        'cv_pt': cv_pt
    }
    
    features = pd.DataFrame(data, index=[0])
    return features, cv_pt

input_df, cv_text = user_input_features()

# 4. LÓGICA DE PREDIÇÃO E EXIBIÇÃO
if st.sidebar.button('Verificar Match', type="primary"):
    if model is not None and cv_text.strip():
        prediction_proba = model.predict_proba(input_df)
        prob_success = prediction_proba[0][1]

        st.subheader("Resultado da Análise Preditiva")
        
        if prob_success > 0.65:
            st.success(f"Potencial de Match: ALTO ({prob_success:.2%})")
            st.markdown("✅ **Recomendação:** Priorizar para entrevista.")
        elif prob_success > 0.40:
            st.warning(f"Potencial de Match: MÉDIO ({prob_success:.2%})")
            st.markdown("⚠️ **Recomendação:** Considerar para as próximas fases.")
        else:
            st.error(f"Potencial de Match: BAIXO ({prob_success:.2%})")
            st.markdown("❌ **Recomendação:** Manter em banco de talentos.")

        st.progress(prob_success, text=f"Score de Compatibilidade: {prob_success:.0%}")

        with st.expander("Ver detalhes dos dados inseridos"):
            st.dataframe(input_df)

    elif not cv_text.strip():
        st.error("Por favor, cole o currículo do candidato para realizar a análise.")
else:
    st.info("Aguardando inserção de dados na barra lateral para iniciar a análise.")