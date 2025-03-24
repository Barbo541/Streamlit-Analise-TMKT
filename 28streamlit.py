import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Configuração da Página
st.set_page_config(
    page_title='Análise de Telemarketing',
    page_icon='📊',
    layout='wide'
)
st.title("📊 Análise de Telemarketing")

# Sidebar para Upload do Arquivo
st.sidebar.header("📂 Carregar Dados")
uploaded_file = st.sidebar.file_uploader("Faça o upload do arquivo CSV", type=["csv"])

df = None  # Inicializa a variável df vazia

if uploaded_file is not None:
    with st.spinner("Carregando dados..."):
        df = pd.read_csv(uploaded_file, sep=';', low_memory=False)
    st.sidebar.success("✅ Dados carregados com sucesso!")

    # Sidebar para Filtros
    st.sidebar.header("🔎 Filtros")
    selected_job = st.sidebar.multiselect("Profissão", df["job"].unique(), default=[])
    selected_marital = st.sidebar.multiselect("Estado Civil", df["marital"].unique(), default=[])
    selected_education = st.sidebar.multiselect("Escolaridade", df["education"].unique(), default=[])

    # Botão para Resetar Filtros
    if st.sidebar.button("🔄 Resetar Filtros"):
        selected_job, selected_marital, selected_education = [], [], []

    # Aplicação dos Filtros
    df_filtered = df.copy()
    if selected_job:
        df_filtered = df_filtered[df_filtered["job"].isin(selected_job)]
    if selected_marital:
        df_filtered = df_filtered[df_filtered["marital"].isin(selected_marital)]
    if selected_education:
        df_filtered = df_filtered[df_filtered["education"].isin(selected_education)]

    # Exibição de Gráficos e Análises
    st.subheader("📈 Visualização dos Dados")
    col1, col2 = st.columns(2)

    # Gráfico de Distribuição de Idade
    with col1:
        fig = px.histogram(df_filtered, x="age", nbins=30, title="Distribuição de Idades")
        st.plotly_chart(fig, use_container_width=True)

    # Gráfico de Proporção de Aceitação
    with col2:
        fig2 = px.pie(df_filtered, names='y', title='Proporção de Aceitação')
        st.plotly_chart(fig2, use_container_width=True)

    # Seção de Dados Filtrados com Expander
    with st.expander("📋 Dados Filtrados"):
        st.dataframe(df_filtered)

        # Botão de Download dos Dados Filtrados
        st.download_button(
            label="📥 Baixar Dados Filtrados",
            data=df_filtered.to_csv(index=False).encode("utf-8"),
            file_name="dados_filtrados.csv",
            mime="text/csv"
        )
else:
    st.warning("⚠️ Faça o upload de um arquivo CSV para começar a análise.")
