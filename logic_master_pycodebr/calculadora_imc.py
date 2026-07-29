from dataclasses import dataclass
from enum import Enum

peso_minimo_kg = 2.0
peso_maximo_kg = 650.0
altura_minima_m = 0.5
altura_maxima_m = 2.75

imc_saudavel_minima = 18.5
imc_saudavel_maximo= 24.9

class ImcError(Exception):
    pass

class MedidaInvalidaError(ImcError):
    pass

class Classificacao(Enum):
    abaixo_peso = ('Abaixo do peso', 18.5)
    peso_normal = ('Peso normal', 25.0)
    sobrepeso = ('Sobrepeso', 30.0)
    obesidade_grau_1 = ('Obsidade grau I', 35.0)
    obesidade_grau_2 = ('Obsidade grau II', 40.0)
    obesidade_grau_3 = ('Obsidade grau III', float('inf'))

    def __init__(self, descricao: str, limite_superior: float) -> None:
        self.descricao = descricao
        self.limite_superior = limite_superior
    
@dataclass(frozen=True)
class ResultadoImc:
    peso_kg: float
    altura_m: float
    imc: float
    classificacao: Classificacao

    @property
    def peso_ideal_minimo(self) -> float:
        return imc_saudavel_minima * self.altura_m**2
    
    @property
    def peso_ideal_maximo(self) -> float:
        return imc_saudavel_maximo * self.altura_m**2
    
def validar_medidas(peso_kg: float, altura_m: float) -> None:
    if not peso_minimo_kg <= peso_kg <= peso_maximo_kg:
        raise MedidaInvalidaError(
            f'Peso deve estar entre {peso_minimo_kg}kg e {peso_maximo_kg}kg.'
        )
    
    if not altura_minima_m <= altura_m <= altura_maxima_m:
        raise MedidaInvalidaError(
            f'Altura deve estar entre {altura_minima_m}m e {altura_maxima_m}m'
        )

def classificar(imc: float) -> Classificacao:
    for faixa in Classificacao:
        if imc < faixa.limite_superior:
            return faixa

    return Classificacao.obesidade_grau_3

def calcular_imc(peso_kg: float, altura_m: float) -> ResultadoImc:
    validar_medidas(peso_kg, altura_m)
    imc = peso_kg / altura_m**2

    return ResultadoImc(
        peso_kg = peso_kg,
        altura_m = altura_m,
        imc = imc,
        classificacao = classificar(imc),
    )

def formatar_resultado(resultado: ResultadoImc) -> str:
    return (
        f"\nPeso informado..: {resultado.peso_kg:.1f}"
        f"\nAltura informada: {resultado.altura_m:.2f}"
        f"\nIMC.............: {resultado.imc:.2f}"
        f"\nClassificação...: {resultado.classificacao.descricao}"
        f"\nPeso ideal......: "
        f"{resultado.peso_ideal_minimo:.1f}kg a"
        f"{resultado.peso_ideal_maximo:.1f} kg"
    )

def _ler_medida(rotulo: str) -> float:
    while True:
        entrada = input(f"{rotulo}: ").strip().replace(',', '.')

        try:
            return float(entrada)
        except ValueError:
            print(f"Valor inálido: '{entrada}'. Use números, ex.: 1.75")
        
def main() -> None:
    print('=== Calculadora de IMC ===')

    while True:
        peso = _ler_medida('Peso em kg')
        altura = _ler_medida('Altura em metros')

        try:
            resultado = calcular_imc(peso, altura)
        except MedidaInvalidaError as erro:
            print(f"\n{erro}\n")
            continue
        print(formatar_resultado(resultado))
        break

if __name__ == '__main__':
    main()