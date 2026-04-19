import streamlit as st
from agente import DevCoinAgent

# Configuração da página com tema escuro
st.set_page_config(page_title="DevCoin - Terminal Financeiro", page_icon="📟", layout="centered")

# CSS para a estética Retro-Futurista (Neon & Purple)
st.markdown("""
    <style>
    .stApp {
        background-color: #0d0221;
        color: #bc13fe;
    }
    .stChatMessage {
        background-color: #1a1a2e;
        border: 1px solid #bc13fe;
        box-shadow: 0 0 10px #bc13fe;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    h1 {
        color: #05ffa1 !important;
        text-shadow: 0 0 15px #05ffa1;
        font-family: 'Courier New', Courier, monospace;
    }
    .stChatInputContainer {
        border-top: 2px solid #05ffa1;
    }
    div[data-testid="stMarkdownContainer"] p {
        color: #e0e0e0;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📟 DevCoin OS v1.0")
st.subheader("Bora refatorar esse orçamento, Dev?")

# Inicializa o agente
if "agente" not in st.session_state:
    st.session_state.agente = DevCoinAgent()

# Inicializa o histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "🚀 **SISTEMA INICIALIZADO.**\n\nOlá, Dev! Sou o DevCoin. Vi que você está focado em dar um upgrade no setup e tirar aquelas certificações. O kernel das suas finanças está carregado. Como posso te ajudar a debugar seus gastos hoje?"
        }
    ]

# Exibe as mensagens do histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do usuário
if prompt := st.chat_input("Digite um comando financeiro..."):
    # Adiciona mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gera resposta do assistente
    with st.chat_message("assistant"):
        with st.spinner("Processando requisição no mainframe..."):
            resposta = st.session_state.agente.responder(prompt)
            st.markdown(resposta)
    
    # Adiciona resposta ao histórico
    st.session_state.messages.append({"role": "assistant", "content": resposta})