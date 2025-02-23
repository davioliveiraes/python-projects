def caixa_eletronico():
   notas = [100, 50, 5, 10, 1]
   while True:
      try:
         valor_saque = int(input("Digite o valor que quer sacar: "))
         if 10 <= valor_saque <= 600:
            break
         else:
            print("Valor inválido. Por favor insira um valor que seja entre R$10 e R$600")
      except ValueError:
         print("Entrada inválida. Por favor, insira um valor que seja númerico.")

   quantidade_notas = {nota: 0 for nota in notas}

   for nota in notas:
      if valor_saque >= nota:
         quantidade_notas[nota] = valor_saque // nota
         valor_saque %= nota
      
   print("Notas fornecidas: ")
   for nota, quantidade in quantidade_notas.items():
      if quantidade > 0:
            print(f"Notas de R${nota}: {quantidade}")

caixa_eletronico()
