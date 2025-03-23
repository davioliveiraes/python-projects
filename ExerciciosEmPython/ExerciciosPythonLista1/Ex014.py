km_percorrido = float(input("Digite a quantidade de KM percorridos: "))
dias_alugado = int(input("Digite a quantidade de dias que o carro foi alugado: "))
valor_total = (dias_alugado * 90) + (km_percorrido * 0.20)

print(f"Valor do aluguel do carro: R${dias_alugado * 90:,.2f}")
print(f"Valor do KM percorrida: R${km_percorrido * 0.20:,.2f}")
print(f"\nO valor total a ser pago pelo aluguel do carro é: R${valor_total:,.2f}")
