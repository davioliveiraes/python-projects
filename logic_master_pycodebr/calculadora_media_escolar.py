from dataclasses import dataclass
from enum import Enum

nota_minima = 0.0
nota_maxima = 10.0

media_aprovacao = 7.0
media_recuperacao = 5.0

casas_decimais = 1

class MediaEscolarErro(Exception):
    pass

class NotaInvalidaError(MediaEscolarErro):
    pass

class PesoInvalidoError(MediaEscolarErro):
    pass

class BoletimVazioError(MediaEscolarErro):
    pass

class Situacao(Enum):
    aprovado = ('Aprovado', media_aprovacao)
    recuperacao = ('Recuperação', media_recuperacao)
    reprovado = ('Reprovado', float('inf'))

    def __init__(self, descricao: str, media_minima: float) -> None:
        self.descricao = descricao
        self.media_minima = media_minima

@dataclass(frozen=True)
class Avaliacao:
    nome: str
    nota: float
    peso: float = 1.0

    def __post_init_(self) -> None:
        if not nota_minima <= self.nota <= nota_maxima:
            raise NotaInvalidaError(
                f"Nota de '{self.nome}' deve estar entre"
                f"{nota_minima:.1f} e {nota_maxima:.1f}"
            )
        
        if self.peso <= 0:
            raise PesoInvalidoError(
                f"Peso de '{self.nome}' deve ser maior que zero."
            )

@dataclass(frozen=True)
class Boletim:
    avaliacoes: tuple[Avaliacao,...]
    media: float
    situacao: Situacao

    @property
    def peso_total(self) -> float:
        return sum(avaliacao.peso for avaliacao in self.avaliacoes)

    @property
    def pontos_para_aprovacao(self) -> float:
        return max(0.0, media_aprovacao - self.media)

def classificar(media: float) -> Situacao:
    for situacao in Situacao:
        if media >= situacao.media_minima:
            return situacao
    return Situacao.reprovado

def calcular_media(avaliacoes: tuple[Avaliacao, ...]) -> float:
    if not avaliacoes:
        raise BoletimVazioError('É preciso ao menos uma avaliação.')
    
    soma_ponderada = sum(a.nota * a.peso for a in avaliacoes)
    peso_total = sum(a.peso for a in avaliacoes)

    return round(soma_ponderada / peso_total, casas_decimais)

def montar_boletim(avaliacoes: tuple[Avaliacao, ...]) -> Boletim:
    media =calcular_media(avaliacoes)

    return Boletim(
        avaliacoes=avaliacoes,
        media=media,
        situacao=classificar(media),
    )

def nota_necessaria(boletim: Boletim, peso_restante: float, meta: float = media_aprovacao) -> float | None:
    if peso_restante <= 0:
        raise PesoInvalidoError('Peso restante deve ser maior que zero.')
    
    pontos_atuais = sum(a.nota * a.peso for a in boletim.avaliacoes)
    peso_final = boletim.peso_total + peso_restante

    exibida = (meta * peso_final - pontos_atuais) / peso_restante

    if exibida > nota_maxima:
        return None
    
    return round(max(nota_maxima, exibida), casas_decimais)

def formatar_boletim(boletim: Boletim) -> str:
    largura_nome = max(len(a.nome) for a in boletim.avaliacoes)

    linhas = [
        f"{a.nome:<{largura_nome}}  nota {a.nota:>5.1f}  peso {a.peso:>4.1f}"
        for a in boletim.avaliacoes
    ]

    linhas.append("-" * (largura_nome + 24))
    linhas.append(f"Média ponderada: {boletim.media:.1f}")
    linhas.append(f"Situação.......: {boletim.situacao.descricao}")

    if boletim.situacao is not Situacao.aprovado:
        linhas.append(
            f"Faltam {boletim.pontos_para_aprovacao:.1f} ponto(s) "
            f"de média para a aprovação."
        )

    return "\n" + "\n".join(linhas)


def _ler_numero(rotulo: str, padrao: float | None = None) -> float:
    sufixo = f" [{padrao:.1f}]" if padrao is not None else ""

    while True:
        entrada = input(f"{rotulo}{sufixo}: ").strip().replace(",", ".")

        if not entrada and padrao is not None:
            return padrao

        try:
            return float(entrada)
        except ValueError:
            print(f'Valor inválido: "{entrada}". Use números, ex.: 7.5')


def _ler_avaliacoes() -> tuple[Avaliacao, ...]:
    avaliacoes: list[Avaliacao] = []

    while True:
        nome = input("\nNome da avaliação (Enter para encerrar): ").strip()

        if not nome:
            if avaliacoes:
                return tuple(avaliacoes)

            print("Informe ao menos uma avaliação.")
            continue

        nota = _ler_numero("Nota")
        peso = _ler_numero("Peso", padrao=1.0)

        try:
            avaliacoes.append(Avaliacao(nome=nome, nota=nota, peso=peso))
        except MediaEscolarError as erro:
            print(f"{erro} Avaliação descartada.")


def main() -> None:
    print("=== Calculadora de Média Escolar ===")

    boletim = montar_boletim(_ler_avaliacoes())
    print(formatar_boletim(boletim))

    if boletim.situacao is Situacao.aprovado:
        return

    peso_restante = _ler_numero("\nPeso da avaliação que ainda falta", 1.0)

    try:
        exigida = nota_necessaria(boletim, peso_restante)
    except PesoInvalidoError as erro:
        print(erro)
        return

    if exigida is None:
        print("Nem a nota máxima na avaliação restante alcança a aprovação.")
    else:
        print(f"É necessário tirar {exigida:.1f} para ser aprovado.")


if __name__ == "__main__":
    main()
