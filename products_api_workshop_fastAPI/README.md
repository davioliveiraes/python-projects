# Products API

API RESTful assíncrona para gerenciamento de produtos, desenvolvida com FastAPI e SQLAlchemy Async.

## Finalidade

Projeto de estudo demonstrando um CRUD completo de produtos com:

- Operações assíncronas (async/await)
- Validação de dados com Pydantic
- ORM SQLAlchemy 2.0 com suporte async
- Migrações com Alembic
- Validação de unicidade para nomes de produtos

## Tecnologias

- Python 3.13
- FastAPI
- SQLAlchemy 2.0 (async)
- Pydantic
- Alembic
- SQLite + aiosqlite
- Poetry
- Ruff

## Como Executar

### Preparar o ambiente (Linux)

```bash
# Instalar pipx e poetry
sudo apt install pipx
pipx ensurepath
pipx install poetry
pipx inject poetry poetry-plugin-shell

# Clonar e acessar o projeto
git clone https://github.com/davioliveiraes/python-projects.git
cd python-projects/products_api_workshop_fastAPI

# Configurar Python e dependências
poetry python install 3.13
poetry env use 3.13
poetry install
```

### Configurar banco de dados

```bash
# Criar arquivo .env
echo "DATABASE_URL='sqlite+aiosqlite:///products.db'" > .env

# Executar migrações
poetry run alembic upgrade head
```

### Executar a API

```bash
poetry run fastapi dev products_api/app.py
```

Acesse: http://localhost:8000/docs

## Autor

Workshop de FastAPI apresentado e ministrado pela PyCodeBr(https://www.instagram.com/pycodebr/)

Primeiro contato com a framework FastAPI do Python.
