velocidade_carro = int(input("Digite a velocidade do carro(km/h): "))
velocidade_permitida = 80
if velocidade_carro > velocidade_permitida:
    ultrapassagem_velocidade = velocidade_carro - velocidade_permitida
    multa = ultrapassagem_velocidade * 80
    print(
        f"Você foi multado por excesso de velocidade permitida! Ultrapassagem de: {ultrapassagem_velocidade:.2f}km/h, multa de: R${multa:,.2f}"
    )
else:
    print("Sem multas, você está na velocidade correta.")
