from dataclasses import dataclass, field
from decimal import ROUND_HALF_UP, Decimal
from enum import Enum

centavos = Decimal("0.01")

taxa_juros_mensal_padrao = Decimal("0.0149")
parcelas_permitidas = (12, 24, 36, 48, 60)

entrada_minima_percentual = Decimal("0.20")
desconto_extra_maximo = Decimal("0.05")
comissao_percentual = Decimal("0.012")

class VendaError(Exception):
    pass

class ValorInvalidoError(VendaError):
    pass

class DescontoInvalidoError(VendaError):
    pass

class EntradaInvalidaError(VendaError):
    pass

class ParcelamentoInvalidoError(VendaError):
    pass

def dinheiro(valor: Decimal | str | int) -> Decimal:
    return Decimal(valor).quantize(centavos, rounding=ROUND_HALF_UP)


class FormaPagamento(Enum):

    a_vista = ("À vista", Decimal("0.08"), False)
    cartao = ("Cartão de crédito", Decimal("0.03"), False)
    financiamento = ("Financiamento", Decimal("0.00"), True)

    def __init__(self, descricao: str, desconto_padrao: Decimal, gera_financiamento: bool) -> None:
        self.descricao = descricao
        self.desconto_padrao = desconto_padrao
        self.gera_financiamento = gera_financiamento


@dataclass(frozen=True)
class Opcional:

    nome: str
    preco: Decimal

    def __post_init__(self) -> None:
        if self.preco <= 0:
            raise ValorInvalidoError(
                f"Preço do opcional '{self.nome}' deve ser maior que zero."
            )


@dataclass(frozen=True)
class Veiculo:

    modelo: str
    ano: int
    preco_tabela: Decimal
    opcionais: tuple[Opcional, ...] = ()

    def __post_init__(self) -> None:
        if self.preco_tabela <= 0:
            raise ValorInvalidoError(
                f"Preço de tabela de '{self.modelo}' deve ser maior que zero."
            )

    @property
    def preco_opcionais(self) -> Decimal:
        return dinheiro(sum((o.preco for o in self.opcionais), Decimal("0")))

    @property
    def preco_cheio(self) -> Decimal:
        return dinheiro(self.preco_tabela + self.preco_opcionais)


@dataclass(frozen=True)
class Financiamento:

    valor_financiado: Decimal
    taxa_mensal: Decimal
    parcelas: int
    valor_parcela: Decimal

    @property
    def total_pago(self) -> Decimal:
        return dinheiro(self.valor_parcela * self.parcelas)

    @property
    def juros_totais(self) -> Decimal:
        return dinheiro(self.total_pago - self.valor_financiado)


@dataclass(frozen=True)
class Proposta:

    veiculo: Veiculo
    forma_pagamento: FormaPagamento
    desconto_total: Decimal
    valor_final: Decimal
    entrada: Decimal
    comissao: Decimal
    financiamento: Financiamento | None = field(default=None)

    @property
    def desembolso_total(self) -> Decimal:
        if self.financiamento is None:
            return self.valor_final

        return dinheiro(self.entrada + self.financiamento.total_pago)


def calcular_desconto(preco_cheio: Decimal, forma_pagamento: FormaPagamento, desconto_extra: Decimal = Decimal("0"),) -> Decimal:

    if not Decimal("0") <= desconto_extra <= desconto_extra_maximo:
        raise DescontoInvalidoError(
            "Desconto extra deve ficar entre 0% e " f"{desconto_extra_maximo:.1%}."
        )

    percentual = forma_pagamento.desconto_padrao + desconto_extra

    return dinheiro(preco_cheio * percentual)


def calcular_parcela(valor_financiado: Decimal, taxa_mensal: Decimal, parcelas: int,) -> Decimal:

    if parcelas not in parcelas_permitidas:
        raise ParcelamentoInvalidoError(
            f"Parcelas devem ser uma destas: {parcelas_permitidas}."
        )

    if taxa_mensal < 0:
        raise ValorInvalidoError("Taxa de juros não pode ser negativa.")

    if taxa_mensal == 0:
        return dinheiro(valor_financiado / parcelas)

    fator = 1 - (1 + taxa_mensal) ** -parcelas

    return dinheiro(valor_financiado * taxa_mensal / fator)


def validar_entrada(entrada: Decimal, valor_final: Decimal) -> None:
    minimo = dinheiro(valor_final * entrada_minima_percentual)

    if entrada < minimo:
        raise EntradaInvalidaError(
            f"Entrada mínima é {entrada_minima_percentual:.0%} do valor "
            f"({formatar_moeda(minimo)})."
        )

    if entrada >= valor_final:
        raise EntradaInvalidaError(
            "Entrada igual ou maior que o valor do veículo dispensa " "financiamento."
        )


def montar_proposta(
    veiculo: Veiculo,
    forma_pagamento: FormaPagamento,
    desconto_extra: Decimal = Decimal("0"),
    entrada: Decimal = Decimal("0"),
    parcelas: int | None = None,
    taxa_mensal: Decimal = taxa_juros_mensal_padrao,
) -> Proposta:

    desconto = calcular_desconto(veiculo.preco_cheio, forma_pagamento, desconto_extra)
    valor_final = dinheiro(veiculo.preco_cheio - desconto)
    comissao = dinheiro(valor_final * comissao_percentual)

    if not forma_pagamento.gera_financiamento:
        return Proposta(
            veiculo=veiculo,
            forma_pagamento=forma_pagamento,
            desconto_total=desconto,
            valor_final=valor_final,
            entrada=valor_final,
            comissao=comissao,
        )

    if parcelas is None:
        raise ParcelamentoInvalidoError("Financiamento exige o número de parcelas.")

    validar_entrada(entrada, valor_final)

    valor_financiado = dinheiro(valor_final - entrada)

    financiamento = Financiamento(
        valor_financiado=valor_financiado,
        taxa_mensal=taxa_mensal,
        parcelas=parcelas,
        valor_parcela=calcular_parcela(valor_financiado, taxa_mensal, parcelas),
    )

    return Proposta(
        veiculo=veiculo,
        forma_pagamento=forma_pagamento,
        desconto_total=desconto,
        valor_final=valor_final,
        entrada=entrada,
        comissao=comissao,
        financiamento=financiamento,
    )


def formatar_moeda(valor: Decimal) -> str:
    
    inteiro, _, centavos = f"{valor:,.2f}".partition(".")
    inteiro = inteiro.replace(",", ".")

    return f"R$ {inteiro},{centavos}"


def formatar_proposta(proposta: Proposta) -> str:
    veiculo = proposta.veiculo

    linhas = [
        f"Veículo........: {veiculo.modelo} ({veiculo.ano})",
        f"Preço de tabela: {formatar_moeda(veiculo.preco_tabela)}",
    ]

    for opcional in veiculo.opcionais:
        linhas.append(f"  + {opcional.nome:<20} {formatar_moeda(opcional.preco)}")

    linhas += [
        f"Pagamento......: {proposta.forma_pagamento.descricao}",
        f"Desconto.......: -{formatar_moeda(proposta.desconto_total)}",
        f"Valor final....: {formatar_moeda(proposta.valor_final)}",
    ]

    if proposta.financiamento is not None:
        fin = proposta.financiamento
        linhas += [
            f"Entrada........: {formatar_moeda(proposta.entrada)}",
            f"Financiado.....: {formatar_moeda(fin.valor_financiado)}",
            f"Parcelas.......: {fin.parcelas}x de "
            f"{formatar_moeda(fin.valor_parcela)}",
            f"Juros ({fin.taxa_mensal:.2%} a.m.): "
            f"{formatar_moeda(fin.juros_totais)}",
            f"Desembolso.....: {formatar_moeda(proposta.desembolso_total)}",
        ]

    linhas.append(f"Comissão.......: {formatar_moeda(proposta.comissao)}")

    return "\n" + "\n".join(linhas)


def _ler_decimal(rotulo: str, padrao: Decimal | None = None) -> Decimal:
    sufixo = f" [{padrao}]" if padrao is not None else ""

    while True:
        entrada = input(f"{rotulo}{sufixo}: ").strip().replace(",", ".")

        if not entrada and padrao is not None:
            return padrao

        try:
            return Decimal(entrada)
        except ArithmeticError:
            print(f'Valor inválido: "{entrada}". Use números, ex.: 89900.00')


def _ler_opcao(rotulo: str, opcoes: tuple[str, ...]) -> int:
    for indice, opcao in enumerate(opcoes, start=1):
        print(f"  {indice}) {opcao}")

    while True:
        escolha = input(f"{rotulo}: ").strip()

        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            return int(escolha) - 1

        print(f"Escolha um número de 1 a {len(opcoes)}.")


def _ler_opcionais() -> tuple[Opcional, ...]:
    opcionais: list[Opcional] = []

    while True:
        nome = input("\nOpcional (Enter para encerrar): ").strip()

        if not nome:
            return tuple(opcionais)

        preco = _ler_decimal("Preço do opcional")

        try:
            opcionais.append(Opcional(nome=nome, preco=preco))
        except VendaError as erro:
            print(f"{erro} Opcional descartado.")


def main() -> None:
    print("=== Calculadora de Venda de Carros ===\n")

    veiculo = Veiculo(
        modelo=input("Modelo: ").strip(),
        ano=int(_ler_decimal("Ano")),
        preco_tabela=_ler_decimal("Preço de tabela"),
        opcionais=_ler_opcionais(),
    )

    print()
    formas = tuple(FormaPagamento)
    forma = formas[_ler_opcao("Forma de pagamento", tuple(f.descricao for f in formas))]

    desconto_extra = _ler_decimal(
        f"Desconto extra (0 a {desconto_extra_maximo})", Decimal("0")
    )

    entrada = Decimal("0")
    parcelas = None

    if forma.gera_financiamento:
        entrada = _ler_decimal("Entrada")
        print()
        parcelas = parcelas_permitidas[
            _ler_opcao("Parcelas", tuple(f"{p}x" for p in parcelas_permitidas))
        ]

    try:
        proposta = montar_proposta(
            veiculo=veiculo,
            forma_pagamento=forma,
            desconto_extra=desconto_extra,
            entrada=entrada,
            parcelas=parcelas,
        )
    except VendaError as erro:
        print(f"\nProposta recusada: {erro}")
        return

    print(formatar_proposta(proposta))


if __name__ == "__main__":
    main()
