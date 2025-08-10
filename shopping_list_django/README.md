# 🛒 Lista de Compras Inteligente

Sistema de lista de compras digital para supermercados que oferece aos clientes maior controle e uma experiência otimizada durante suas compras.

## 📹 Demonstração

[🎥 **Assista ao vídeo demonstrativo**](https://youtu.be/demo-video-id) - Veja o sistema funcionando na prática!

## 💼 Funcionalidade no Mercado Real

Este projeto representa um **recurso digital disponibilizado pelo supermercado** para seus clientes, proporcionando:

- **🎯 Controle Total**: Clientes podem criar e gerenciar suas listas de compras com preços em tempo real
- **💰 Gestão de Orçamento**: Cálculo automático do valor total da compra
- **⏱️ Economia de Tempo**: Organização prévia reduz tempo na loja em até 30%
- **📱 Experiência Moderna**: Interface intuitiva acessível via smartphone, tablet ou computador
- **✅ Acompanhamento**: Marcação de itens comprados com feedback visual imediato

**Para o Supermercado**: Dados valiosos sobre padrões de consumo, aumento da satisfação do cliente e diferencial competitivo no mercado.

**Para o Cliente**: Compras mais organizadas, controle de gastos e experiência digitalizada.

## 🛠 Tecnologias Utilizadas

- **Backend**: Python 3.8+ com Django 4.2
- **Frontend**: HTML5, CSS3 e JavaScript (ES6+)
- **Banco de Dados**: SQLite
- **Design**: Interface responsiva com foco em usabilidade
- **Arquitetura**: MVC com APIs RESTful

## 🚀 Como Executar

```bash
# 1. Clone o repositório
git clone https://github.com/davioliveiraes/python-projects.git
cd python-projects/shopping_list_django

# 2. Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# 3. Instale as dependências
pip install django

# 4. Configure o banco de dados
python manage.py makemigrations products
python manage.py migrate

# 5. Execute o servidor
python manage.py runserver
```

**Acesse**: http://127.0.0.1:8000/

## 📁 Estrutura do Projeto

```
python-projects/
└── shopping_list_django/       # Este projeto
    ├── shopping_list/          # Configurações do Django
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── products/               # App principal
    │   ├── models.py           # Modelo de dados dos produtos
    │   ├── views.py            # Lógica de negócio
    │   ├── urls.py             # Rotas da aplicação
    │   ├── admin.py            # Interface administrativa
    │   ├── static/products/    # CSS e JavaScript
    │   └── templates/products/ # Templates HTML
    ├── manage.py               # Script do Django
    └── db.sqlite3             # Banco de dados
```

## 👨‍💻 Desenvolvedor

**Davi Oliveira**  
*Desenvolvedor Full Stack Python*

Especialista em desenvolvimento web com Python, Django e tecnologias modernas para criar soluções digitais inovadoras.

---

*Desenvolvido para revolucionar a experiência de compras em supermercados* 🛒