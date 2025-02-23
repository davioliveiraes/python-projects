largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

area_ser_pintada = largura * altura
litros_de_tinta = area_ser_pintada / 2

print(f"\nA quantidade de tinta necessária para pintar uma parede de {area_ser_pintada:.2f}m² é de: {litros_de_tinta:.2f}L")

