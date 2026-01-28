📺 TV 3.0 – Prova de Conceito (PoC)

Este projeto é uma Prova de Conceito (PoC) desenvolvida para o seminário da disciplina, com foco em TV 3.0, pensamento computacional e aplicações interativas baseadas em software.

A aplicação simula um servidor backend que disponibiliza informações e conteúdos para uma TV conectada, utilizando Python e FastAPI.
Para simplificação do protótipo, o sistema utiliza um único vídeo, evitando complexidade desnecessária na entrega do trabalho.

🧠 Objetivo do Projeto

Demonstrar o funcionamento de uma aplicação backend para TV 3.0

Aplicar conceitos de:

APIs REST

Comunicação cliente-servidor

Pensamento computacional

Prototipação de sistemas interativos

Servir como base conceitual para futuras expansões (personalização, proximidade, múltiplos conteúdos etc.)

🛠️ Tecnologias Utilizadas

Python 3.10 ou superior

FastAPI – framework para criação da API

Uvicorn – servidor ASGI

Git/GitHub – versionamento do código

📋 Pré-requisitos

Antes de rodar o projeto, é necessário ter instalado:

Python

Download: https://www.python.org/downloads/

Durante a instalação, marque a opção “Add Python to PATH”

Git

Download: https://git-scm.com/

📁 Estrutura do Projeto (resumo)
tv3-poc/
├── main.py              # Arquivo principal da aplicação
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação do projeto
├── venv/                # Ambiente virtual (não versionado)
└── .gitignore

🚀 Como Rodar o Projeto
1️⃣ Clonar o repositório
git clone https://github.com/mjjunior/Trabalho2_Seminario.git
cd Trabalho2_Seminario

2️⃣ Criar o ambiente virtual

No Windows:

python -m venv venv


No Linux / macOS:

python3 -m venv venv

3️⃣ Ativar o ambiente virtual

Windows (PowerShell):

venv\Scripts\Activate


Linux / macOS:

source venv/bin/activate

4️⃣ Instalar as dependências
pip install -r requirements.txt

5️⃣ Rodar a aplicação
uvicorn main:app --reload


Se tudo estiver correto, aparecerá algo como:

Uvicorn running on http://127.0.0.1:8000

🌐 Como Acessar a Aplicação
🔹 API principal
http://127.0.0.1:8000

🔹 Documentação automática da API (Swagger)
http://127.0.0.1:8000/docs


Essa página permite:

Ver todas as rotas disponíveis

Testar requisições diretamente pelo navegador

Entender os dados retornados pela API

📌 Observações Importantes

O projeto utiliza apenas um vídeo, de forma proposital, para:

Simplificar a implementação

Focar na arquitetura e nos conceitos

O diretório venv/ não deve ser enviado para o GitHub

Toda a lógica principal está concentrada no main.py