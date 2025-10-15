# Sistema de Aprovação de Exames Veterinários - SOLID (OCP)

Exemplo prático de aplicação do **Princípio Aberto/Fechado (Open/Closed Principle)** do SOLID em uma clínica veterinária.

## 🎯 Sobre o Projeto

Sistema de aprovação de exames veterinários que demonstra como adicionar novos tipos de exames **sem modificar** o código existente, apenas **estendendo** funcionalidades.

## ✅ Benefícios do OCP

- **Estabilidade**: Código existente não é alterado, reduzindo riscos de bugs
- **Extensibilidade**: Novos exames adicionados facilmente através de herança
- **Manutenibilidade**: Cada tipo de exame tem suas próprias regras isoladas
- **Testabilidade**: Classes independentes facilitam testes unitários
- **Escalabilidade**: Sistema cresce sem aumentar complexidade

## 🏥 Funcionalidades

- ✅ Aprovação de diferentes tipos de exames veterinários
- ✅ Validação de condições específicas para cada exame
- ✅ Registro de exames aprovados e reprovados
- ✅ Geração de relatórios de aprovação
- ✅ Sistema extensível para novos tipos de exames

## 📋 Tipos de Exames Implementados

| Exame | Validações |
|-------|-----------|
| **Exame de Sangue** | Jejum mínimo de 8 horas |
| **Raio-X** | Sedação para áreas sensíveis |
| **Ultrassom** | Bexiga cheia e pelo raspado |
| **Exame de Urina** | Amostra recente e volume adequado |
| **Ecocardiograma** | Animal calmo e avaliação por idade |

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+**
- Bibliotecas nativas:
  - `abc` - Classes abstratas
  - `datetime` - Manipulação de datas
  - `typing` - Type hints

## 🚀 Como Executar
```bash
# Clone o repositório
git clone https://github.com/davioliveiraes/python-projects.git

# Navegue até o diretório
cd python-projects/py_SOLID_challenge/2_O_OCP

# Execute o script
python main.py
```

## 📄 Estrutura do Código
```
.
├── main.py    # Sistema completo com exemplos
└── README.md         # Este arquivo
```

## 💡 Adicionando um Novo Exame

Para adicionar um novo tipo de exame, basta criar uma nova classe:
```python
class TomographyExam(Exam):
    def check_conditions(self) -> bool:
        # Implementar validações específicas
        return True
    
    def get_type(self) -> str:
        return "Tomografia"
```

**Não é necessário modificar a classe `ApproveExam`!**

## 📊 Exemplo de Saída
```
🔍 Analisando: Exame de Sangue - Paciente: Rex (Labrador)
   Veterinário: Dr. Silva
   Data: 15/10/2025 14:30
  ✓ Jejum adequado: 10h
✅ Exame de Sangue APROVADO!

🔍 Analisando: Exame de Raio-X - Paciente: Bob (Bulldog)
   Veterinário: Dr. Costa
   Data: 15/10/2025 14:30
  ✗ Área coluna requer sedação
❌ Exame de Raio-X REPROVADO!

===============================================
RELATÓRIO FINAL
===============================================
✅ Exames aprovados: 5
❌ Exames reprovados: 2
📊 Total de exames: 7
```

## 📚 Conceito SOLID - OCP

> "Entidades de software devem ser abertas para extensão, mas fechadas para modificação."

Este princípio permite adicionar novas funcionalidades sem alterar o código existente, tornando o sistema mais robusto e menos propenso a erros.
