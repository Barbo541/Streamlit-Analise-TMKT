# 📊 Streamlit - Análise de Telemarketing

Este projeto é um **dashboard interativo** desenvolvido com **Streamlit**, que permite a **análise de campanhas de telemarketing** utilizando dados reais. Os usuários podem carregar um arquivo CSV, aplicar filtros e visualizar insights através de gráficos interativos.

## 🔥 Funcionalidades
✅ **Upload de arquivos CSV** 📂  
✅ **Filtros interativos** para segmentar os dados 🔍  
✅ **Gráficos dinâmicos** com Plotly 📊  
✅ **Download dos dados filtrados** 📥  
✅ **Deploy no Render** 🚀  

## 📂 Estrutura do Projeto
```
📂 Streamlit-Analise-TMKT/
├── 28streamlit.py         # Aplicativo Streamlit
├── bank-additional.csv    # Dataset de exemplo
├── requirements.txt       # Bibliotecas necessárias
├── README.md              # Documentação do projeto
```

## 🛠 Tecnologias Utilizadas
- **Python** (3.x)
- **Streamlit** (Interface)
- **Pandas** (Manipulação de dados)
- **Plotly** (Visualização gráfica)

## 🚀 Como Executar Localmente
1. Clone o repositório:
   ```bash
   git clone https://github.com/Barbo541/Streamlit-Analise-TMKT.git
   cd Streamlit-Analise-TMKT
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o app Streamlit:
   ```bash
   streamlit run 28streamlit.py
   ```
4. Acesse no navegador: `https://streamlit-analise-tmkt.onrender.com/`

## 🌍 Deploy no Render
O projeto está hospedado no **Render**. Para fazer o deploy:
1. Suba os arquivos para o **GitHub**.
2. Crie um **Web Service** no **Render**.
3. Configure o comando de execução:
   ```bash
   streamlit run 28streamlit.py --server.port $PORT
   ```
4. Render criará um link acessível para seu app.

## 📌 Contribuição
Se quiser contribuir, faça um **fork** do repositório, crie um **branch** e envie um **pull request**! 😃

---

💡 **Autor:** Barbo541  
📅 **Data:** Março/2025  
🚀 **Deploy via Render**
