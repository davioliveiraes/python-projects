# Delivery MongoDB API

API REST em Flask para gerenciamento de pedidos de delivery, com persistência em
MongoDB e arquitetura em camadas.

## Finalidade

O projeto implementa o ciclo de vida de um pedido de delivery — cadastro,
consulta e atualização — servindo como estudo prático de bancos NoSQL orientados
a documentos aplicados a uma API de produção.

O foco não está apenas no CRUD, mas em como estruturá-lo: cada requisição
atravessa camadas com responsabilidades isoladas (rota → composer → use case →
repository → banco), o acesso ao MongoDB fica atrás de uma interface abstrata, e
regras de negócio são testadas sem tocar no banco real por meio de mocks.

### Endpoints

| Método  | Rota                       | Descrição                                   |
| ------- | -------------------------- | ------------------------------------------- |
| `POST`  | `/delivery/order`          | Registra um novo pedido (retorna `201`)     |
| `GET`   | `/delivery/order/<id>`     | Busca um pedido pelo `ObjectId`             |
| `PATCH` | `/delivery/order/<id>`     | Atualiza campos de um pedido existente      |

Exemplo de corpo para `POST /delivery/order`:

```json
{
  "data": {
    "name": "Harvey Specter",
    "address": "Bay-Adelaide Centre, Nova York",
    "cupom": false,
    "items": [
      { "item": "Café", "quantidade": 1 },
      { "item": "Rosquinha", "quantidade": 2 }
    ]
  }
}
```

Respostas de erro seguem um formato único, produzido por um handler central:

```json
{ "errors": [{ "title": "UnprocessableEntity", "detail": "..." }] }
```

Os status tratados são `422` (corpo inválido), `404` (pedido inexistente) e
`500` (erro não previsto).

## Tecnologias

| Tecnologia         | Uso no projeto                                              |
| ------------------ | ----------------------------------------------------------- |
| **Python 3.14**    | Linguagem base                                               |
| **Flask 3.1**      | Servidor HTTP e roteamento via Blueprints                    |
| **MongoDB 8.2**    | Banco de dados NoSQL orientado a documentos                  |
| **PyMongo 4.17**   | Driver oficial de conexão e operações no MongoDB             |
| **Cerberus 1.3**   | Validação declarativa do corpo das requisições               |
| **Pytest 9.0**     | Testes unitários com mocks das dependências externas         |
| **Docker Compose** | Provisionamento do MongoDB local com volumes persistentes    |
| **python-dotenv**  | Carga de variáveis de ambiente a partir do `.env`            |
| **Pylint**         | Análise estática de código                                   |

## Como executar

### Pré-requisitos

- Python 3.12 ou superior
- Docker Desktop em execução

### 1. Clone o repositório e crie o ambiente virtual

```powershell
git clone https://github.com/<seu-usuario>/delivery_mongodb_api.git
cd delivery_mongodb_api

python -m venv venv
.\venv\Scripts\Activate.ps1
```

> No Linux ou macOS, ative com `source venv/bin/activate`.

### 2. Instale as dependências

```powershell
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente

```powershell
Copy-Item .env.example .env
```

O `.env.example` traz credenciais de desenvolvimento local. Substitua-as antes
de usar o projeto fora da sua máquina.

| Variável                | Padrão                         | Descrição                    |
| ----------------------- | ------------------------------ | ---------------------------- |
| `MONGO_URI`             | `mongodb://localhost:27017/`   | URI do servidor MongoDB      |
| `MONGO_DATABASE`        | `rocket_db`                    | Nome do banco de dados       |
| `MONGO_ROOT_USERNAME`   | `admin`                        | Usuário root do container    |
| `MONGO_ROOT_PASSWORD`   | `password`                     | Senha root do container      |

### 4. Suba o banco de dados

```powershell
docker compose up -d
```

O container expõe a porta `27017` apenas em `127.0.0.1` e grava os dados no
volume `delivery_mongodb_api_mongodb_data`, que sobrevive a reinicializações.

Para inspecionar os documentos pelo MongoDB Compass, use a URI:

```text
mongodb://admin:password@localhost:27017/?authSource=admin
```

### 5. Inicie a API

```powershell
python run.py
```

A API sobe em `http://localhost:5000`. A conexão com o banco é verificada no
startup — se o MongoDB não estiver acessível, a aplicação falha imediatamente
com uma mensagem explícita, em vez de errar na primeira requisição.

### 6. Execute os testes

```powershell
python -m pytest -v
```

Os testes de integração em `repository_test.py` estão marcados com
`@pytest.mark.skip`, pois exigem um banco populado. Para rodá-los, suba o
MongoDB e remova as marcações.

## Conceitos Aprendidos

**Modelagem NoSQL orientada a documentos.** Um pedido é gravado como um único
documento com sua lista de itens aninhada, sem tabelas de junção. A ausência de
schema no banco desloca a responsabilidade pela integridade dos dados para a
camada de aplicação — daí a validação explícita com Cerberus.

**Operações do MongoDB via PyMongo.** `insert_one` e `insert_many` para escrita,
`find` e `find_one` para leitura, busca por `ObjectId`, filtros com operadores
`$exists`, atualizações parciais com `$set` e incrementais com `$inc`, além de
projeções para retornar apenas campos selecionados.

**Arquitetura em camadas com injeção de dependência.** A rota não sabe como um
pedido é salvo; o use case não sabe que o banco é MongoDB. Os composers em
`src/main/composer/` montam a cadeia de dependências, e os use cases recebem o
repositório pronto pelo construtor — o que torna possível substituí-lo por um
mock nos testes.

**Programação orientada a interfaces.** `OrdersRepositoryInterface` é uma classe
abstrata (`ABC`) que define o contrato de acesso a dados. Os use cases dependem
dessa abstração, não da implementação concreta, seguindo o princípio da inversão
de dependência.

**Tratamento centralizado de erros.** Use cases lançam exceções tipadas
(`HttpNotFoundError`, `HttpUnprocessableEntityError`) e um único `error_handler`
as converte em respostas HTTP. O formato de erro fica consistente em toda a API,
e exceções não previstas viram `500` sem vazar o stack trace.

**Padronização de entrada e saída.** As classes `HttpRequest` e `HttpResponse`
desacoplam os use cases do Flask: eles operam sobre objetos próprios, o que os
torna testáveis sem subir um servidor ou criar um contexto de requisição.

**Testes unitários com mocks.** Cada camada é testada isoladamente — mocks de
coleção do PyMongo verificam o repositório, mocks de repositório verificam os use
cases, e `unittest.mock.patch` cobre o handler de conexão. A suíte roda em menos
de um segundo sem banco de dados ativo.

**Containerização do ambiente de desenvolvimento.** O Docker Compose provisiona
o MongoDB com autenticação, healthcheck e volumes nomeados, garantindo que o
ambiente seja reproduzível em qualquer máquina.

## Referência

Projeto desenvolvido durante o **Nível 7 — NoSQL com MongoDB** da
**Trilha de Python da [Rocketseat](https://www.rocketseat.com.br/)**.
