<h1 align="center">API de Autenticação de Usuários</h1>

<p align="center">
  <img alt="Flask" src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/>
  <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
  <img alt="SQLAlchemy" src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white"/>
  <img alt="MySQL" src="https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white"/>
  <img alt="Docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white"/>
</p>

<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-principais-bibliotecas">Principais Bibliotecas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-executar">Como Executar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-endpoints">Endpoints</a>
</p>

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- **Python** - Linguagem de programação principal
- **Flask** - Framework web minimalista para Python
- **SQLAlchemy** - ORM para manipulação do banco de dados
- **MySQL** - Banco de dados relacional robusto
- **Docker** - Containerização do banco de dados
- **bcrypt** - Biblioteca para hash de senhas

## 📚 Principais Bibliotecas

- **Flask** - Framework principal para criação da API REST
- **Flask-SQLAlchemy** - Extensão que adiciona suporte ao SQLAlchemy no Flask
- **Flask-Login** - Gerenciamento de sessões e autenticação de usuários
- **bcrypt** - Para criptografia segura de senhas
- **PyMySQL** - Driver MySQL para Python
- **Werkzeug** - Biblioteca de utilitários WSGI

## 💻 Projeto

Esta é uma **API RESTful de autenticação de usuários** desenvolvida com Flask, criada durante o curso de Python da Rocketseat. O projeto implementa um sistema completo de autenticação e autorização com diferentes níveis de acesso.

A aplicação oferece funcionalidades essenciais de segurança:

- **Registro de usuários** com senhas criptografadas
- **Login/Logout** com sessões seguras
- **Controle de acesso** baseado em roles (admin/user)
- **Proteção de rotas** que exigem autenticação
- **Gerenciamento de usuários** com operações CRUD
- **Validação de permissões** para operações sensíveis

O projeto segue as melhores práticas de segurança, incluindo hash de senhas com bcrypt, validação de sessões e controle de acesso baseado em funções.

## 🔧 Como Executar

### Pré-requisitos
- Python 3.8+
- Docker e Docker Compose
- Git

### 1. Clone o repositório
```bash
git clone https://github.com/davioliveiraes/python-projects.git
cd python-projects/api_autenticacao_usuario
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

### 4. Configure o banco de dados MySQL com Docker
```bash
# Inicie o container MySQL
docker-compose up -d

# Aguarde alguns segundos para o banco inicializar
```

### 5. Configure as tabelas do banco
```bash
# Execute o Python para criar as tabelas
python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

### 6. Execute a aplicação
```bash
python app.py
```

A API estará disponível em `http://localhost:5000`

### 7. Para parar a aplicação
```bash
# Parar a aplicação Flask: Ctrl+C
# Parar o container MySQL
docker-compose down
```

## 🛣️ Endpoints

### Autenticação
| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| `POST` | `/login` | Realiza login do usuário | ❌ |
| `GET` | `/logout` | Realiza logout do usuário | ✅ |

### Usuários
| Método | Endpoint | Descrição | Autenticação | Permissão |
|--------|----------|-----------|--------------|-----------|
| `POST` | `/user` | Cadastra um novo usuário | ❌ | - |
| `GET` | `/user/<id>` | Busca um usuário por ID | ✅ | - |
| `PUT` | `/user/<id>` | Atualiza dados do usuário | ✅ | Próprio usuário ou Admin |
| `DELETE` | `/user/<id>` | Remove um usuário | ✅ | Apenas Admin |

### Exemplo de Uso

#### Criar usuário
```json
POST /user
{
  "username": "usuario_teste",
  "password": "senha123"
}
```

#### Login
```json
POST /login
{
  "username": "usuario_teste",
  "password": "senha123"
}
```

## 🔐 Níveis de Acesso

- **user**: Usuário padrão, pode gerenciar apenas seus próprios dados
- **admin**: Usuário administrador, pode gerenciar todos os usuários

<p align="center">Desenvolvido durante o curso Python da Rocketseat 🚀</p>