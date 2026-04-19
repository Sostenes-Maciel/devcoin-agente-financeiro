# DevCoin: O Mentor Financeiro do Estudante de TI

## Contexto

Estudantes de Análise e Desenvolvimento de Sistemas (ADS) e áreas de tecnologia lidam com um desafio constante: equilibrar o orçamento do dia a dia (transporte, alimentação) com os altos custos de investimento na carreira, como o pagamento de certificações Cloud, a compra de microcontroladores para projetos IoT (como o ESP32) ou o upgrade de hardware para rodar IDEs pesadas.

O DevCoin é um agente financeiro inteligente, construído com IA Generativa, focado exclusivamente neste público. Ele não é um gerente de banco genérico, mas um "Tech Lead financeiro" que ajuda a:

- Refatorar Gastos: Analisa o fluxo de caixa e sugere cortes inteligentes ("debug financeiro").
- Projetar Metas: Ajuda a planejar a compra de equipamentos e setups.
- Evitar Alucinações: Funciona estritamente dentro do escopo financeiro, sem inventar dados, baseando-se apenas nos arquivos de contexto.

---

## Tecnologias Utilizadas

- LLM: [Google Gemini 1.5 Flash](https://ai.google.dev/) (Rápido, eficiente e com alta janela de contexto).
- Interface: [Streamlit](https://streamlit.io/) (Criando um visual Retro-Futurista / Synthwave).
- Processamento de Dados: [Pandas](https://pandas.pydata.org/) (Para injeção dos CSVs diretamente no System Prompt).
- Linguagem: Python 3.x

---

## Estrutura do Repositório

```text
devcoin-agente-financeiro/
│
├── data/                             # Base de conhecimento do agente
│   ├── historico_atendimento.csv     # Interações passadas
│   ├── perfil_investidor.json        # Metas (Ex: Reserva e Setup)
│   ├── produtos_financeiros.json     # Onde investir a economia
│   └── transacoes.csv                # Histórico de gastos mensais
│
├── docs/                             # Documentação exigida pelo desafio
│   ├── 01-documentacao-agente.md     # Persona, arquitetura e segurança
│   ├── 02-base-conhecimento.md       # Estratégia de injeção de dados
│   ├── 03-prompts.md                 # System Instructions e Edge Cases
│   ├── 04-metricas.md                # Testes de resiliência e anti-alucinação
│   └── 05-pitch.md                   # Roteiro do pitch em vídeo
│
├── src/                              # Código-fonte da aplicação
│   ├── .env.example                  # Template para a chave da API do Google
│   ├── app.py                        # Front-end (Streamlit)
│   ├── agente.py                     # Back-end e integração com a API do Gemini
│   └── requirements.txt              # Dependências do projeto
│
├── .gitignore                        # Proteção de chaves e arquivos locais
└── README.md                         # Este arquivo
```
Como Executar o Projeto Localmente

Se você deseja rodar o DevCoin na sua máquina para testar as capacidades de análise do agente, siga os passos abaixo:

    Clone o repositório



git clone [https://github.com/SEU-USUARIO/devcoin-agente-financeiro.git](https://github.com/SEU-USUARIO/devcoin-agente-financeiro.git)
cd devcoin-agente-financeiro/src

    Configure a Chave da API
    Crie um arquivo chamado .env na pasta src/ (usando o .env.example como base) e adicione a sua chave do Google AI Studio:

Plaintext

GEMINI_API_KEY=sua_chave_api_do_google_aqui

    Instale as dependências
    É recomendado o uso de um ambiente virtual (venv).



pip install -r requirements.txt

    Rode a aplicação


streamlit run app.py

O terminal interativo será aberto automaticamente no seu navegador padrão, pronto para refatorar suas contas!
