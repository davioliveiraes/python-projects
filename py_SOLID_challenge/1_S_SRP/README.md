# Sistema de Gerenciamento de Tarefas - SOLID (SRP)

Exemplo prático de aplicação do **Princípio de Responsabilidade Única (Single Responsibility Principle)** do SOLID.

## 🎯 Sobre o Projeto

Este projeto demonstra a refatoração de uma classe monolítica em múltiplas classes especializadas, cada uma com uma única responsabilidade bem definida.

## ✅ Benefícios da Refatoração

- **Manutenibilidade**: Alterações isoladas sem impacto em outras funcionalidades
- **Testabilidade**: Testes unitários mais simples e focados
- **Reusabilidade**: Componentes podem ser utilizados em diferentes contextos
- **Legibilidade**: Código mais limpo e autoexplicativo
- **Escalabilidade**: Facilita adição de novas funcionalidades

## 📦 Responsabilidades Separadas

| Classe | Responsabilidade |
|--------|-----------------|
| `APIConnector` | Gerenciar conexões com a API |
| `TaskRepository` | Operações CRUD de tarefas |
| `NotificationService` | Enviar notificações |
| `ReportGenerator` | Gerar relatórios em diferentes formatos |
| `ReportSender` | Enviar relatórios para destinatários |

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+**
- Bibliotecas nativas: `abc`, `typing`, `datetime`, `json`

## 🚀 Como Executar
```bash
# Clone o repositório
git clone https://github.com/davioliveiraes/python-projects.git

# Navegue até o diretório
cd python-projects/py_SOLID_challenge/1_S_SRP

# Execute o script
python3 main.py
```

## 📄 Estrutura do Código
```
.
├── main.py           # Aplicação completa com exemplos
└── README.md         # Este arquivo
```

## 💡 Exemplo de Saída
```
✓ Tarefa 'Implementar autenticação' criada com ID: 1
✓ Tarefa 'Escrever testes' criada com ID: 2
✓ Tarefa ID 1 atualizada

📧 Enviando notificação via email
   Para: dev@empresa.com
   Assunto: Tarefa Concluída
   Mensagem: A tarefa 'Implementar autenticação' foi concluída!

==================================================
RELATÓRIO DE TAREFAS
==================================================
Total de tarefas: 2
...
```

## 📚 Conceito SOLID - SRP

> "Uma classe deve ter apenas uma razão para mudar."

Este princípio garante que cada classe tenha apenas uma responsabilidade, tornando o código mais modular e fácil de manter.
