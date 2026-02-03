# Princípio de Substituição de Liskov (LSP)

Sistema de processamento de pagamentos demonstrando o terceiro princípio SOLID.

---

## Sobre o Projeto

Implementação de um sistema de pagamentos para e-commerce que demonstra a **violação** e **aplicação correta** do LSP, mostrando como hierarquias de classes bem projetadas garantem substituição segura entre classes base e derivadas.

---

## Benefícios do LSP

| Benefício | Descrição |
|-----------|-----------|
| **Type Safety** | Erros detectados em tempo de desenvolvimento |
| **Previsibilidade** | Sem exceções inesperadas em runtime |
| **Manutenibilidade** | Novos métodos de pagamento sem quebrar código existente |
| **Testabilidade** | Cada interface testada isoladamente |

---

## Funcionalidades

**Métodos de Pagamento:**
- 💳 **Cartão de Crédito** - Parcelamento até 12x, estorno automático
- 📱 **PIX** - QR Code, processamento instantâneo
- 📄 **Boleto** - Linha digitável, definição de vencimento
- 💸 **Cartão de Débito** - QR Code, estorno automático

**Serviços:** Processar pagamento | Parcelamento | Estorno | QR Code | Vencimento

---

## Tecnologias

Python 3.13.8 | ABC | Type Hints | Datetime

---

## Como Executar

```bash
git clone https://github.com/davioliveiraes/python-projects.git
cd python-projects/py_SOLID_challenge/3_L_LSP
python main.py
```

---

## Estrutura

```
3_L_LSP/
├── main.py       # Implementação do sistema
└── README.md     # Documentação
```

---

## Conceito LSP

> "Objetos de uma classe derivada devem poder substituir objetos da classe base sem alterar o comportamento do programa." - Barbara Liskov

### ❌ Violação

```python
class PaymentProcess(ABC):
    def get_installments(self, valor: float): pass  # Nem todos suportam!

class PaymentPix(PaymentProcess):
    def get_installments(self, value: float):
        raise NotImplementedError("PIX não suporta!")  # 💥 QUEBRA!
```

### ✅ Aplicação Correta

```python
class PaymentProcess(ABC):
    def process(self, value: float): pass  # Apenas o que TODOS fazem

class PaymentInInstallments(ABC):
    def get_installments(self, value: float): pass  # Apenas quem suporta

class PaymentPix(PaymentProcess):  # Não herda Parcelavel
    pass
```

---

## Aprendizados

1. Não Force Comportamentos Inexistentes

PIX tradicional não tem parcelas? Então não implemente get_installments(). Crie PixPaymentInInstallments separado.

2. Interfaces Pequenas e Específicas

Melhor ter PaymentInInstallments, PaymentInstant, PaymentWithFee separadas do que uma interface gigante. Cada classe implementa só o que realmente faz.

3. Funcionalidades Parecidas ≠ Mesma Classe

Pix via Cartão e Pix Parcelado são diferentes. Não use flags ou condicionais, crie classes distintas.

4. Teste de Substituição

"Posso trocar PixPayment por CreditCardPayment sem quebrar?" Se sim, LSP está correto.

5. Type Safety Previne Erros

IDE detecta erros antes de executar. Tentar chamar view_installments() com PixPayment já avisa o erro.

6. Evolução Segura

Adicionamos Pix Parcelado e Pix via Cartão sem modificar código existente. Sistema escala sem quebrar.

7. Evite isinstance()

Se precisa verificar tipo do objeto, provavelmente está violando LSP. Use polimorfismo.

Resumo: LSP = subclasses substituem classes base sem surpresas. Resultado: código extensível, seguro e manutenível.

---

👨‍💻 **Autor:** Davi Oliveira - Software Engineer