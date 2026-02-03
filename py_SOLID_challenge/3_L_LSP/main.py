from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import Optional

# Interface base - apenas o que TODOS os pagamentos fazem
class PaymentProcessor(ABC):
    
    @abstractmethod
    def process(self, value: float) -> dict:
        pass

    @abstractmethod
    def get_status(self, transaction_id: str) -> dict:
        pass

# Interface para pagamentos que suportam estorno
class PaymentReversed(ABC):

    @abstractmethod
    def reverse(self, transaction_id: str) -> dict:
        pass

# Interface para pagamentos que suportam parcelamento
class PaymentInInstallments(ABC):

    @abstractmethod
    def get_installments(self, value: float) -> list:
        pass

# Interface para pagamentos com instantâneos
class PaymentInstant(ABC):

    @abstractmethod
    def generate_qr_code(self, value: float) -> str:
        pass

# Interface para pagamentos com vencimento
class PaymentDueDate(ABC):

    @abstractmethod
    def set_due_date(self, days: int) -> datetime:
        pass

# Interface para pagamentos com taxa (ex - Pix Parcelado)
class PaymentWithFee(ABC):

    @abstractmethod
    def caculate_fee(self, value: float, **kwargs) -> float:
        pass

# Interface para pagamentos que usam fonte de recurso diferente
class PaymentWithAlternativeSource(ABC):

    @abstractmethod
    def define_payment_source(self, source: str) -> None:
        pass

# Implementações
class CreditCardPayment(PaymentProcessor, PaymentReversed, PaymentInInstallments):
    def process(self, value: float) -> dict:
        return {
            "status": "aprovado",
            "transacao_id": "CDC759",
            "valor": value,
            "metodo": "cartao_de_credito",
            "tipo":"credito_parcelavel"
        }

    def get_status(self, transaction_id: str) -> dict:
        return {"transacao_id": transaction_id, "status": "aprovado"}

    def reverse(self, transaction_id: str) -> dict:
        return {"status": "estornado", "transacao_id": transaction_id}

    def get_installments(self, value: float) -> list:
        return [
            {"parcelas": 1, "valor_parcela": value, "total": value},
            {"parcelas": 3, "valor_parcela": round(value / 3, 2), "total": value},
            {"parcelas": 6, "valor_parcela": round(value / 6, 2), "total": value},
            {"parcelas": 12, "valor_parcela": round(value / 12, 2), "total": value},
        ]

class PixPayment(PaymentProcessor, PaymentReversed, PaymentInstant):
    def process(self, value: float) -> dict:
        return {
            "status": "aprovado",
            "transacao_id": "PIX789",
            "valor": value,
            "metodo": "pix",
            "tipo": "instantaneo"
        }
    
    def get_status(self, transaction_id: str) -> dict:
        return {"transacao_id": transaction_id, "status": "aprovado"}

    def reverse(self, transaction_id: str) -> dict:
        return {"status": "estornado", "transacao_id": transaction_id}

    def generate_qr_code(self, value: float) -> str:
        return f"12039812908628br.gov.bcb.pix0912{value}"

class PixPaymentInInstallments(PaymentProcessor, PaymentReversed, PaymentInInstallments, PaymentInstant, PaymentWithFee):
    monthly_interest_rate = 0.0299 # 2.99% a.m
    max_installments = 12

    def process(self, value: float, installments: int = 1) -> dict:
        total_fee = self.caculate_fee(value, installments=installments)
        total_amount = value + total_fee

        return {
            "status": "aprovado",
            "transacao_id": "PIXPARC123",
            "valor_original": value,
            "valor_total": round(total_amount, 2),
            "parcelas": installments,
            "valor_parcela": round(total_amount / installments, 2), 
            "taxa_total": round(total_fee, 2),
            "metodo": "pix_parcelado",
            "tipo": "parcelado_juros",
            "destinatario_recebe": "parcelado"
        }
    
    def get_status(self, transaction_id: str) -> dict:
        return {"transacao_id": transaction_id, "status": "aprovado"}
    
    def reverse(self, transaction_id: str) -> dict:
        return {
            "status": "estorno_parcial",
            "transacao_id": transaction_id,
            "observacao": "Parcelas não pagas serão canceladas"
        }
    
    def get_installments(self, value: float) -> list:
        options = []
        for num_installments in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12]:
            if num_installments > self.max_installments:
                break

            total_fee = self.caculate_fee(value, installments=num_installments)
            total_amount = value + total_fee
        
            options.append({
                "parcelas": num_installments,
                "valor_parcela": round(total_amount / num_installments, 2),
                "valor_total": round(total_amount, 2),
                "taxa_total": round(total_fee, 2),
                "taxa_percentual": round((total_fee / value) * 100, 2)
            })

        return options

    def generate_qr_code(self, value: float) -> str:
        return f"109719723120232br.gov.bcb.pix.parcelado0123{value}"
    
    def caculate_fee(self, value: float, installments: int = 1, **kwargs) -> float:
        if installments == 1:
            return 0.0
        amount = value * ((1 + self.monthly_interest_rate) ** installments)
        return amount - value


class PixPaymentWithCreditCard(PaymentProcessor, PaymentReversed, PaymentInstant, PaymentWithFee, PaymentWithAlternativeSource):

    advance_fee = 0.0389 # 3.89% (taxa de antecipação)
    
    def __init__(self):
        self.__payment_source = "cartao_credito"
        self.__card_number: Optional[str] = None
    
    def define_payment_source(self, source: str) -> None:
        self.__payment_source = source
    
    def process(self, value: float) -> dict:
        fee = self.caculate_fee(value)
        amount_debited_card = value + fee

        return {
            "status": "aprovado",
            "transacao_id": "PIXCDC888",
            "valor_enviado_pix": value,
            "valor_debitado_cartao": round(amount_debited_card, 2),
            "taxa_antecipacao": round(fee, 2),
            "metodo": "pix_via_cartao_credito",
            "tipo": "antecipacao_com_taxa",
            "fonte_pagamento": self.__payment_source,
            "destinatario_recebe": "instantaneo_integral",
            "observacao": "Pix enviado instantaneamente. Taxa cobrado no cartão"
        }
    
    def get_status(self, transaction_id: str) -> dict:
        return {"transacao_id": transaction_id, "status": "aprovado"}
    
    def reverse(self, transaction_id: str) -> dict:
        return {
            "status": "estornado",
            "transacao_id": transaction_id,
            "observao": "Taxa de antecipação será estornada também"
        }
    
    def generate_qr_code(self, value: float) -> str:
        return f"980987192392br.gov.bcb.pix0320{value}"
    
    def caculate_fee(self, value: float, **kwargs) -> float:
        return value * self.advance_fee

class BankSlipPayment(PaymentProcessor, PaymentDueDate):
    def process(self, value: float) -> dict:
        return {
            "status": "pendente",
            "transacao_id": "BOL654",
            "valor": value,
            "metodo": "boleto",
            "tipo": "pagamento_com_vencimento",
            "linha_digital": "23793.38128 60000.000003 00000.000400 1 84340000012345",
        }
    
    def get_status(self, transaction_id: str) -> dict:
        return {"transacao_id": transaction_id, "status": "aguardando pagamento"}
    
    def set_due_date(self, days: int) -> datetime:
        return datetime.now() + timedelta(days=days)

class DebitCardPayment(PaymentProcessor, PaymentReversed, PaymentInstant):
    def process(self, value: float) -> dict:
        return {
            "status": "aprovado",
            "transacao_id": "CDD901",
            "valor": value,
            "metodo": "carta de debito"
        }
    
    def get_status(self, transaction_id: str) -> dict:
        return {"transacao_id": transaction_id, "status": "aprovado"}
    
    def reverse(self, transaction_id: str) -> dict:
        return {"status": "estornado", "transacao_id": transaction_id}
    
    def generate_qr_code(self, value: float) -> str:
        return f"DEBITO-QR-{value}"

# Serviços
class ServicoCheckout:
    def process_payment(self, processor: PaymentProcessor, value: float) -> dict:
        result = processor.process(value)
        method = result['metodo'].replace('_', ' ').title()

        print(f"Pagamento processado: {method}")
        print(f"Tipo: {result.get('tipo', 'N/A')}")

        if result.get('metodo') == 'pix_via_cartao_credito':
            print(f"  Valor enviado (Pix): R${result['valor_enviado_pix']:.2f}")
            print(f"  Debitado do cartão: R${result['valor_debitado_cartao']:.2f}")
            print(f"  Taxa de antecipação: R${result['taxa_antecipacao']:.2f}")
            print(f"  {result['observacao']}")
        elif result.get('metodo') == 'pix_parcelado':
            print(f"  Valor original: R${result['valor_original']:.2f}")
            print(f"  Total a pagar: R${result['valor_total']:.2f}")
            print(f"  Taxa de juros: R${result['taxa_total']:.2f}")
            print(f"  Parcelas: {result['parcelas']}x de R${result['valor_parcela']:.2f}")
        else:
            print(f"  Valor: R${result.get('valor', value):.2f}")

        return result

    def view_fee_comparison(self, pix_card: PixPaymentWithCreditCard, pix_installments: PixPaymentInInstallments, value: float):
        print(f"\n{'='*60}")
        print(f"  COMPARAÇÃO: Pix via Cartão vs Pix Parcelado")
        print(f"Valor: R${value:.2f}")
        print(f"{'='*60}\n")

        card_fee = pix_card.caculate_fee(value)
        card_total = value + card_fee

        print(" PIX VIA CARTÃO DE CRÉDITO")
        print(f"  - Destinatário recebe: R${value:.2f} (instantâneo)")
        print(f"  - Você paga no cartão: R${card_total:.2f}")
        print(f"  - Taxa: R${card_fee:.2f} ({(card_fee/value)*100:.2f}%)")
        print(f"  - Pode parcelar depois na fatura do cartão\n")

        installments_12x = pix_installments.get_installments(value)[-1]
        print("   PIX PARCELADO (12x)")
        print(f"  Você paga: {installments_12x['parcelas']}x de R${installments_12x['valor_parcela']:.2f}")
        print(f"  Total: R${installments_12x['valor_total']:.2f} ({installments_12x['taxa_percentual']:.2f}%)\n")

        print(f"{"=" * 60}\n")

    def view_installments(self, processor: PaymentInInstallments, value: float) -> list:
        installments = processor.get_installments(value)
        print(f"Opcões de parcelamento disponíveis: ")
        for option in installments:
            print(f" - {option['parcelas']}x de R${option['valor_parcela']:.2f}")
        return installments

    def process_reverse(self, processor: PaymentReversed, transacao_id: str) -> dict:
        result = processor.reverse(transacao_id)
        print(f"Estorno realizado: {transacao_id}")
        return result

    def generate_instant_payment(self, processor: PaymentInstant, value: float) -> str:
        qrcode = processor.generate_qr_code(value)
        print(f"QR Code gerado para pagamento instantâneo")
        return qrcode

# Uso
if __name__ == "__main__":
    checkout = ServicoCheckout()

    # Cartão de Crédito 
    print("=" * 50)
    print("CARTÃO DE CRÉDITO")
    print("=" * 50)
    card = CreditCardPayment()
    checkout.process_payment(card, 1000.00)
    checkout.view_installments(card, 1000.00)
    checkout.process_reverse(card, "CDC123")

    print()

    # Pix
    print("=" * 60)
    print("PIX TRANDICIONAL (Á VISTA)")
    print("=" * 60)
    pix = PixPayment()
    checkout.process_payment(pix, 500.0)

    print()

    print("=" * 60)
    print("PIX VIA CARTÃO DE CRÉDITO (Á vista com taxa)")
    print("=" * 60)
    pix_card = PixPaymentWithCreditCard()
    pix_card.define_payment_source("Nubank **** 12032")
    checkout.process_payment(pix_card, 500.0)

    print()

    print("=" * 60)
    print("PIX PARCELADO (Com juros)")
    print("=" * 60)
    pix_installments = PixPaymentInInstallments()
    result = pix_installments.process(1200.00, installments=12)
    print(f"Pagamento Processado: Pix Parcelado")
    print(f"Tipo: {result['tipo']}")
    print(f"  Valor original: R${result['valor_original']:.2f}")
    print(f"  Total a pagar: R${result['valor_total']:.2f}")
    print(f"  Taxa de juros: R${result['taxa_total']:.2f}")
    print(f"  Parcelas: {result['parcelas']}x de R${result['valor_parcela']:.2f}")

    # Comparação
    checkout.view_fee_comparison(pix_card, pix_installments, 1000.0)

    print()

    # Boleto
    print("=" * 60)
    print("BOLETO")
    print("=" * 60)
    bank_slip = BankSlipPayment()
    checkout.process_payment(bank_slip, 750.0)
    due_date = bank_slip.set_due_date(3)
    print(f"Vencimento: {due_date.strftime('%d/%m/%Y')}")
