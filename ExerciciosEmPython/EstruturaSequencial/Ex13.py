areaPintada = float(input("Digite o tamanho em M² da área a ser pintada: "))
quantLatas = (areaPintada / 18) / 3
precoTotal = quantLatas * 80
print(f"A quantidade de latas a ser comprada: {quantLatas}")
print(f"O preço total a ser pago é: R${precoTotal}")
