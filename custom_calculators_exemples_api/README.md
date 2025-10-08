# Exemplos de Calculadoras Personalizadas

API REST desenvolvida em Python para realizar cálculos matemáticos personalizados através de diferentes calculadoras especializadas.

## 📋 Finalidade

Aplicação construída durante o curso de Python da Rocketseat para demonstrar boas práticas de desenvolvimento web, incluindo Clean Architecture, design patterns e tratamento de erros.

## ⚙️ Funcionalidades

- **Calculator 1**: Divisão por 3, processamento matemático complexo com elevação ao quadrado
- **Calculator 2**: Processamento de múltiplos números com cálculo de desvio padrão
- **Calculator 3**: Validação através de variância e multiplicação
- **Calculator 4**: Cálculo de média aritmética simples

## 🗂️ Estrutura do Projeto

```
├── src/
│   ├── calculators/          # Lógica das calculadoras e testes
│   ├── drivers/              # Handlers (NumPy)
│   │   └── interfaces/       # Interfaces dos drivers
│   ├── errors/               # Tratamento de erros HTTP
│   ├── main/                 # Configuração principal
│   │   ├── factories/        # Factory Pattern
│   │   ├── routes/           # Definição de rotas
│   │   └── server/           # Configuração Flask
│   └── __init__.py           # Inicialização do pacote
├── .gitignore                # Arquivos ignorados pelo Git
├── errors_raw.py             # Definições de erros brutos
├── interface_raw.py          # Interfaces brutas
├── README.md                 # Documentação do projeto
├── requirements.txt          # Dependências do projeto
└── run.py                    # Arquivo principal de execução
```

## 🚀 Como Executar

### Instalação

```bash
# Clone o repositório
git clone https://github.com/davioliveiraes/python-projects.git

# Entre no diretório
cd python-projects/custom_calculators_exemples_api

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### Configuração

```bash
# Execute o servidor
python run.py
```

O servidor estará disponível em `http://localhost:3000`

## 📡 Endpoints

### POST /calculator_1
Processa um número através de operações matemáticas complexas.
```json
{
  "number": 10
}
```

**Resposta:**
```json
{
  "data": {
    "Calculator": 1,
    "result": 123.45
  }
}
```

### POST /calculator_2
Calcula o inverso do desvio padrão de números processados.
```json
{
  "numbers": [2, 4, 6, 8, 10]
}
```

**Resposta:**
```json
{
  "data": {
    "Calculator": 2,
    "result": 0.08
  }
}
```

### POST /calculator_3
Valida se a variância é menor que a multiplicação dos números.
```json
{
  "numbers": [1, 2, 3, 4]
}
```

**Resposta (Sucesso):**
```json
{
  "data": {
    "Calculator": 3,
    "value": 1.25,
    "Success": true
  }
}
```

**Resposta (Falha):**
```json
{
  "error": "Falha no processo: Variância menor que multiplicação"
}
```

### POST /calculator_4
Retorna a média aritmética dos números fornecidos.
```json
{
  "numbers": [10, 20, 30, 40]
}
```

**Resposta:**
```json
{
  "data": {
    "Calculator": 4,
    "result": 25.0
  }
}
```

## 🧪 Testes

Execute os testes com Pytest:

```bash
# Rodar todos os testes
pytest

# Rodar com cobertura
pytest --cov=src

# Rodar testes específicos
pytest src/calculators/test_calculator_1.py
```

## 🛠️ Tecnologias

- Python 3.x
- Flask
- NumPy
- Pytest

---

**Desenvolvido no curso de Python da Rocketseat** 🚀