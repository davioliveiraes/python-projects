km_percorrido = int(input("Digite quantos KM foram percorridos: "))
dias_alugado = int(input("Digite quantos dias foi alugado: "))

preco_final = (dias_alugado * 60) + (km_percorrido * 0.15)
print(f"O preço final a pagar ser de: R${preco_final:.2f}")
