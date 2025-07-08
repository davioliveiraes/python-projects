# 💳 API de Pagamento PIX

Uma API completa para processamento de pagamentos via PIX, desenvolvida em Python com Flask, incluindo geração de QR Codes, confirmação de pagamentos e interface web moderna.

## 🎥 Demonstração

Assista à demonstração completa da API em funcionamento:

<video width="100%" controls>
  <source src="video_api_payment.mp4" type="video/mp4">
  Seu navegador não suporta vídeos HTML5. <a href="video_api_payment.mp4">Clique aqui para assistir</a>
</video>

## 📋 Funcionalidades

- ✅ Geração de pagamentos PIX com QR Code
- ✅ Interface web moderna e responsiva
- ✅ Confirmação automática de pagamentos
- ✅ WebSocket para atualizações em tempo real
- ✅ Páginas de sucesso e erro personalizadas
- ✅ Testes unitários abrangentes
- ✅ Banco de dados SQLite integrado

## 🗂️ Estrutura do Projeto

```
modulo_5_api_de_pagamento/
├── 📁 db_models/
│   └── payment.py          # Modelo de dados do pagamento
├── 📁 instance/
│   └── database.db         # Banco de dados SQLite
├── 📁 payments/
│   └── pix.py             # Lógica de pagamento PIX
├── 📁 repository/
│   └── database.py        # Configuração do banco
├── 📁 static/
│   ├── 📁 css/
│   │   ├── styles.css                    # Estilos página pagamento
│   │   ├── styles_confirmed_payment.css  # Estilos página confirmação
│   │   └── styles_error.css              # Estilos página erro
│   └── 📁 img/            # Imagens QR Codes gerados
├── 📁 templates/
│   ├── 404.html           # Página de erro 404
│   ├── confirmed_payment.html  # Página confirmação
│   └── payment.html       # Página de pagamento
├── 📁 tests/
│   ├── conftest.py        # Configuração dos testes
│   └── test_pix.py        # Testes unitários
├── 📁 venv/               # Ambiente virtual Python
├── .gitignore             # Arquivos ignorados pelo Git
├── app.py                 # Aplicação principal Flask
├── README.md              # Documentação do projeto
├── requirements.txt       # Dependências do projeto
└── video_api_payment.mp4  # Vídeo demonstração da API
```

## 🚀 Instalação e Configuração

### Pré-requisitos
- Python 3.8+
- pip
- virtualenv (recomendado)

### 1. Clone o repositório
```bash
git clone https://github.com/davioliveiraes/python-projects.git
cd python-projects/api_de_pagamento
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação
```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`

## 📡 Endpoints da API

### 🟡 POST `/payments/pix`
Criar um novo pagamento PIX

**Request Body:**
```json
{
  "value": 100.50
}
```

**Response:**
```json
{
  "message": "The payment has been created",
  "payment_id": 1,
  "qr_code_path": "qr_code_payment_uuid"
}
```

### 🟢 GET `/payments/pix/qr_code/<filename>`
Buscar QR Code do pagamento

**Response:** Imagem PNG do QR Code

### 🟡 POST `/payments/pix/confirmation`
Confirmar pagamento PIX

**Request Body:**
```json
{
  "bank_payment_id": "uuid-do-pagamento",
  "value": 100.50
}
```

**Response:**
```json
{
  "message": "The payment has been confirmed"
}
```

## 🎨 Interface Web

### Página de Pagamento
- Design moderno e responsivo
- QR Code gerado dinamicamente
- Timer de expiração (30 minutos)
- Atualizações em tempo real via WebSocket

### Página de Confirmação
- Animação de sucesso
- Detalhes do pagamento
- Próximos passos claros
- Botões de ação intuitivos

### Página de Erro
- Design amigável para erros 404
- Sugestões de solução
- Link para suporte

## 🧪 Testes

Execute os testes unitários:

```bash
# Todos os testes
python -m pytest tests/ -v

# Teste específico
python -m pytest tests/test_pix.py -v

# Com coverage
python -m pytest tests/ --cov=payments --cov-report=html
```

### Testes Implementados
- ✅ Criação de pagamento PIX
- ✅ Validação de UUID
- ✅ Geração de QR Code
- ✅ Formato de dados retornados

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python, Flask, SQLAlchemy
- **Frontend:** HTML5, CSS3, JavaScript
- **Banco de Dados:** SQLite
- **QR Code:** qrcode library
- **WebSocket:** Flask-SocketIO
- **Testes:** pytest
- **Estilo:** CSS moderno com gradientes e animações

## 📦 Dependências Principais

```txt
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Flask-SocketIO==5.3.6
qrcode==7.4.2
pytest==7.4.3
Pillow==10.0.1
```
## 🔧 Configuração do Banco de Dados

O projeto utiliza SQLite por padrão. Para inicializar o banco de dados:

### 1. Usando Flask Shell (Recomendado)
```bash
# Entrar no Flask Shell
flask shell

# Dentro do shell Python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
...     print("Banco de dados criado com sucesso!")
>>> exit()
```

### 2. Alternativa via Python
```bash
python -c "from app import app, db; app.app_context().push(); db.create_all(); print('Database created!')"
```

### Estrutura da Tabela Payment
```sql
CREATE TABLE payment (
    id INTEGER PRIMARY KEY,
    value FLOAT NOT NULL,
    paid BOOLEAN DEFAULT FALSE,
    bank_payment_id VARCHAR(200),
    qr_code VARCHAR(100),
    expiration_date DATETIME
);
```

### Verificar se o banco foi criado
Após executar os comandos acima, você deve ver o arquivo `instance/database.db` criado no seu projeto.

## 📱 Responsividade

A interface é totalmente responsiva, funcionando perfeitamente em:
- 📱 Mobile (320px+)
- 📟 Tablet (768px+)
- 💻 Desktop (1024px+)


## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

Desenvolvido durante o módulo 5 do curso Python da Rocketseat.