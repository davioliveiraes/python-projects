largura = float(input("Digite a largura da parede (m): "))
altura = float(input("Digite a altura da parede (m): "))

area = largura * altura
qtde_litros_tinta = area / 2

print(f"A dimensão da parede é {largura} x {altura}, dando assim {area}m² e mediante a essa medida a quantidade de litros para pinta é de: {qtde_litros_tinta} litros.")
