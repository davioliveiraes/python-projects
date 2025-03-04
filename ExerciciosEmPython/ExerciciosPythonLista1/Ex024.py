distancia_percorrido_km = float(input("Digite a distância que deseja percorrer em KM: "))

if distancia_percorrido_km <= 200:
   preco_passagem = distancia_percorrido_km * 0.50
elif distancia_percorrido_km > 200:
   preco_passagem = distancia_percorrido_km * 0.45

print(f"Valor cobrado pela corrida: R${preco_passagem:,.2f}")
   