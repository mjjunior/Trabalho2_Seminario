# 📺 TV 3.0 — Prova de Conceito (POC)

Este projeto é uma **Prova de Conceito (POC)** desenvolvida para a disciplina de **Seminário / Pensamento Computacional**, com o objetivo de simular conceitos da **TV 3.0**, integrando:

- Perfis de usuário
- Contexto de uso da TV
- Recomendação inteligente de conteúdo
- Regras determinísticas + Machine Learning
- API REST com FastAPI
- Interface web simples simulando uma TV inteligente

---

## 🎯 Objetivo do Projeto

Demonstrar, de forma prática e didática, como tecnologias modernas podem ser aplicadas em um cenário de **TV inteligente**, explorando:

- Personalização de conteúdo
- Uso de Inteligência Artificial para recomendação
- Separação entre regras simbólicas e aprendizado de máquina
- Comunicação entre backend (API) e frontend (interface web)

O projeto **não tem foco comercial**, sendo exclusivamente educacional.

---

## 🧠 Visão Geral da Arquitetura

O sistema é dividido em quatro camadas principais:

- **Frontend**  
  Interface web que simula a TV, exibindo o vídeo e as informações da IA.

- **Backend (FastAPI)**  
  API responsável por fornecer perfis, contexto da TV e recomendações.

- **Módulo de IA**
  - Regras simbólicas (idade, preferências, restrições)
  - Modelo de Machine Learning (Decision Tree)

- **Conteúdo Estático**
  - Vídeo único servido localmente
  - Arquivos JSON simulando dados

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **Scikit-learn**
- **Pandas**
- **HTML, CSS e JavaScript**
- **Git & GitHub**

---

## 📂 Estrutura do Projeto

```text
tv3-poc/
│
├── backend/
│   ├── ia.py              # Lógica de decisão da IA
│   ├── ia_ml.py           # Modelo de Machine Learning
│   └── profile_manager.py # Gerenciamento de perfis
│
├── data/
│   └── conteudo.json      # Dados simulados de conteúdo
│
├── frontend/
│   └── index.html         # Interface da TV
│
├── static/
│   └── video.mp4          # Vídeo único servido pela aplicação
│
├── main.py                # Arquivo principal da API
├── requirements.txt       # Dependências do projeto
├── .gitignore
└── README.md

Como Funciona a Inteligência Artificial

A decisão do conteúdo segue três camadas:

1️⃣ Regras Simbólicas

Crianças recebem prioridade para conteúdo infantil

Preferências explícitas do usuário são respeitadas

Restrições são aplicadas antes do ML

2️⃣ Machine Learning

Modelo: Decision Tree

Entradas:

Idade

Gênero de conteúdo

Saída:

Tipo de conteúdo recomendado

3️⃣ Fallback Seguro

Caso algo falhe, a IA sempre retorna um conteúdo válido.

🚀 Como Executar o Projeto
1️⃣ Clonar o repositório
git clone https://github.com/mjjunior/Trabalho2_Seminario.git
cd Trabalho2_Seminario

2️⃣ Criar o ambiente virtual

Windows

python -m venv venv


Linux / macOS

python3 -m venv venv

3️⃣ Ativar o ambiente virtual

Windows (PowerShell)

.\venv\Scripts\Activate


Linux / macOS

source venv/bin/activate

4️⃣ Instalar as dependências
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

5️⃣ Executar a aplicação

 uvicorn backend.main:app --reload


Se tudo estiver correto, a seguinte mensagem será exibida no terminal:

Uvicorn running on http://127.0.0.1:8000

🌐 Como Acessar a Aplicação

Após iniciar o servidor:

Aplicação (API):
http://127.0.0.1:8000

Documentação automática da API (Swagger):
http://127.0.0.1:8000/docs

Interface da TV (Frontend):
Abra o arquivo frontend/index.html no navegador
(ou sirva via Live Server / servidor simples)

Para sair do modo venv basta rodar o seguinte comando : deactivate