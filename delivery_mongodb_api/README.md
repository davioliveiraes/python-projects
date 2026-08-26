# Delivery MongoDB API

API Flask para registrar pedidos no MongoDB.

## Banco local e MongoDB Compass

O MongoDB Compass e a API se conectam ao mesmo servidor MongoDB local executado
com Docker. O banco usado pela API e `rocket_db` e a colecao e `orders`.

1. Inicie o Docker Desktop.
2. Na raiz do projeto, execute:

   ```powershell
   docker compose up -d
   ```

3. No MongoDB Compass, use a URI (somente para desenvolvimento local):

   ```text
   mongodb://admin:password@localhost:27017/?authSource=admin
   ```

4. Ative o ambiente virtual e execute a API:

   ```powershell
   .\venv\Scripts\Activate.ps1
   python run.py
   ```

Os dados ficam no volume Docker `delivery_mongodb_api_mongodb_data` e continuam
disponiveis quando o container e reiniciado.

## Configuracao opcional

A conexao pode ser alterada por variaveis de ambiente:

- `MONGO_URI`: URI do servidor. Padrao: `mongodb://localhost:27017/`.
- `MONGO_DATABASE`: nome do banco. Padrao: `rocket_db`.

O arquivo `.env.example` documenta os valores locais. A API carrega o arquivo
`.env` automaticamente com `python-dotenv`, e o Docker Compose usa o mesmo arquivo.
O `.env` esta ignorado pelo Git. Substitua essas credenciais antes de usar o projeto
fora de uma maquina de desenvolvimento local.
