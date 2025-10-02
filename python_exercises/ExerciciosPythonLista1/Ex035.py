def menu():
   return """
   
      ALUGUEL DE CARRO
      (1) - Carro de Luxo - R$150,00
      (2) - Carro Popular - R$90,00
   
   """
   
print(menu())

tipo_carro_alugado = int(input("Escolha o número do tipo de carro que deseja: "))
qtde_dias_aluguel = int(input("Digite a quantidade de dias do aluguel: "))
qtde_km = int(input("Digite a quantidade de KM percorrido: "))

pagar_dia_popular = qtde_dias_aluguel * 90
pagar_dia_luxo = qtde_dias_aluguel * 150

if tipo_carro_alugado == 1:
   if 0 > qtde_km <= 100:
      print(f"Preço à pagar: R${pagar_dia_popular + (qtde_km * 0.30):,.2f}")
   else:
      print(f"Preço à pagar R${pagar_dia_luxo +  (qtde_km * 0.25):,.2f}")

elif tipo_carro_alugado == 2:
    if 0 > qtde_km <= 200:
        print(f"Preço à pagar: R${pagar_dia_popular + (qtde_km * 0.20):,.2f}")
    else:
        print(f"Preço à pagar: R${pagar_dia_luxo + (qtde_km * 0.10):,.2f}")

else:
   print("OPÇÃO INVÁLIDA")

