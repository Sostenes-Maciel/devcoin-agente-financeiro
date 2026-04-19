import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class DevCoinAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.contexto = self._carregar_dados()
        
        # 1. Descobre automaticamente os modelos disponíveis para a sua chave
        modelos_disponiveis = [
            m.name for m in genai.list_models() 
            if 'generateContent' in m.supported_generation_methods
        ]
        
        # 2. Escolhe o melhor modelo disponível de forma inteligente
        modelo_escolhido = None
        preferencias = ['models/gemini-1.5-flash', 'models/gemini-1.5-pro', 'models/gemini-pro']
        
        for pref in preferencias:
            if pref in modelos_disponiveis:
                modelo_escolhido = pref
                break
                
        # Se não achar os preferidos, pega o primeiro que a sua chave permitir
        if not modelo_escolhido and modelos_disponiveis:
            modelo_escolhido = modelos_disponiveis[0]

        print(f"🔌 Conectado com sucesso ao modelo: {modelo_escolhido}")

        # 3. Guardamos as instruções para enviar junto com a mensagem (evita erros em modelos antigos)
        self.instrucoes_sistema = f"""
        Você é o DevCoin, mentor financeiro para estudantes de TI. Use analogias de programação e tecnologia.
        Baseie suas respostas financeiras estritamente nos dados abaixo. Não invente transações.
        Se o usuário pedir ajuda com código de programação, diga que seu escopo é APENAS financeiro.
        
        {self.contexto}
        """
        
        self.model = genai.GenerativeModel(model_name=modelo_escolhido)

    def _carregar_dados(self):
        try:
            # Tenta ler o CSV (sobe um nível de src para data)
            df = pd.read_csv('../data/transacoes.csv')
            return f"--- DADOS DE TRANSAÇÕES ---\n{df.to_string()}"
        except Exception as e:
            return "Sem dados locais disponíveis."

    def responder(self, pergunta):
        try:
            # 4. Injeta as regras e os dados diretamente junto com a pergunta do usuário
            prompt_completo = f"{self.instrucoes_sistema}\n\nMensagem do Usuário: {pergunta}"
            
            response = self.model.generate_content(
                prompt_completo,
                generation_config=genai.types.GenerationConfig(temperature=0.3)
            )
            return response.text
        except Exception as e:
            return f"Erro ao gerar resposta: {e}"