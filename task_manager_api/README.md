<h1 align="center">API de Gerenciamento de Tarefas</h1>
<p align="center">
  <img alt="Flask" src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/>
  <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
  <img alt="SQLAlchemy" src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white"/>
</p>
<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-principais-bibliotecas">Principais Bibliotecas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-executar">Como Executar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#️-endpoints">Endpoints</a>
</p>

## 🚀 Tecnologias
Esse projeto foi desenvolvido com as seguintes tecnologias:
- **Python** - Linguagem de programação principal
- **Flask** - Framework web minimalista para Python
- **SQLAlchemy** - ORM para manipulação do banco de dados
- **SQLite** - Banco de dados relacional leve

## 📚 Principais Bibliotecas
- Flask - Framework principal para criação da API REST
- Flask-SQLAlchemy - Extensão que adiciona suporte ao SQLAlchemy no Flask
- Flask-CORS - Para permitir requisições cross-origin
- Marshmallow - Para serialização e validação de dados
- Flask-RESTful - Para criação de APIs RESTful de forma mais simples
- Pytest - Framework de testes para Python

## 💻 Projeto
Esta é uma **API RESTful de gerenciamento de tarefas** desenvolvida com Flask, criada durante o curso de Python da Rocketseat. O projeto implementa um sistema completo de CRUD (Create, Read, Update, Delete) para gerenciar tarefas pessoais ou profissionais.

A aplicação oferece uma interface simples e eficiente para:
- Criar novas tarefas com título, descrição
- Listar todas as tarefas cadastradas
- Visualizar detalhes de uma tarefa específica
- Atualizar informações de tarefas existentes
- Excluir tarefas 

O projeto segue as melhores práticas de desenvolvimento de APIs REST, com estrutura organizada, tratamento de erros e respostas em formato JSON.

## 🔧 Como Executar

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)
- Git

### 1. Clone o repositório
```bash
git clone https://github.com/davioliveiraes/python-projects.git
cd python-projects/api_gerenciamento_tarefas
```

### 2. Crie e ative o ambiente virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados
```bash
# Execute o Python para criar as tabelas
python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

### 5. Execute a aplicação
```bash
python app.py
```

A API estará disponível em `http://localhost:5000`

### 6. Para parar a aplicação
```bash
# Pressione Ctrl+C no terminal onde a aplicação está rodando
```

## 🛣️ Endpoints

### Tarefas
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/tasks` | Lista todas as tarefas |
| `GET` | `/tasks/<id>` | Busca uma tarefa por ID |
| `POST` | `/tasks` | Cria uma nova tarefa |
| `PUT` | `/tasks/<id>` | Atualiza uma tarefa existente |
| `DELETE` | `/tasks/<id>` | Remove uma tarefa |

### Exemplo de Uso

#### Criar tarefa
```json
POST /tasks
{
  "title": "Minha nova tarefa",
  "description": "Descrição da tarefa"
}
```

#### Listar todas as tarefas
```bash
GET /tasks
```

#### Buscar tarefa específica
```bash
GET /tasks/1
```

#### Atualizar tarefa
```json
PUT /tasks/1
{
  "title": "Tarefa atualizada",
  "description": "Nova descrição"
}
```

#### Excluir tarefa
```bash
DELETE /tasks/1
```

<p align="center">Desenvolvido durante o curso Python da Rocketseat 🚀</p>