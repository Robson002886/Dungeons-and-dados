# 🧙‍♂️ Dungeons and Dados - Backend

Este é o backend do **Dungeons and Dadosr**, uma aplicação feita para gerenciar fichas de personagens, anotações e progresso dos jogadores em uma campanha de RPG. O projeto foi desenvolvido com **Python** e **MongoDB**, utilizando operações diretas via `pymongo`.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.10+**
- **MongoDB**
- **pymongo** – biblioteca para comunicação com o MongoDB em Python

---

## 📁 Estrutura do Projeto
backend/
├── campanhas.py # Funções relacionadas a campanhas e suas sessões
├── main.py # Script principal para testes e execuções
├── sessões.ipynb # Notebook interativo para controle de sessões e testes
└── pycache/ # Arquivos compilados do Python

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

## Instalações necessarias
pip install pymongo

## Crie o seu Host e linque ele ao seu codigo
client = MongoClient("mongodb://localhost:27017/")

🧠 Funcionalidades Atuais
Criar, listar e consultar campanhas

Adicionar e gerenciar sessões

Testes interativos via Jupyter Notebook (sessões.ipynb)

🚀 Próximas Etapas
Implementar sistema de fichas de personagem

Criar endpoints para servir os dados (REST API ou interface web)

Autenticação básica para jogadores e mestre

🤝 Contribuições
Sinta-se à vontade para abrir issues ou fazer pull requests com melhorias!

