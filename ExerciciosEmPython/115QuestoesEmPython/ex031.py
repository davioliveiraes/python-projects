distancia_viagem = float(input("Digite a distância da sua viagem(KM): "))
preco_via_longa = distancia_viagem * 0.45
preco_via_curta = distancia_viagem * 0.50

if distancia_viagem < 200:
   print(f"A passagem para sua viagem é R${preco_via_curta:,.2f}")
if distancia_viagem >= 200:
   print(f"A passagem para sua viagem é R${preco_via_longa:,.2f}")
