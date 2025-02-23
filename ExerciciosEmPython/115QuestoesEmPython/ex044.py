print(f"{"LOJAS KANOHA":=^40}")
valor_compras = float(input("Digite o valor total das compras: "))
print('''

   (1) - Á VISTA DINHEIRO/CHEQUE - 10% DE DESCONTO
   (2) - Á VISTA NO CARTÃO - 5% DE DESCONTO
   (3) - EM ATÉ 12X NO CARTÃO - PREÇO NORMAL
   (4) - 3X MAIS NO CARTÃO - 20% DE JUROS

''')

forma_pagamento = int(input("Digite o número da forma de pagamento: "))

if forma_pagamento == 1:
   preco_final_compras = valor_compras - (valor_compras * 0.10)
   print(f"O preço no dinheiro/cheque com 10% de desconto vai ficar de: R${preco_final_compras:,.2f}")
elif forma_pagamento == 2:
   preco_final_compras = valor_compras - (valor_compras * 0.05)
   print(f"O preço no dinheiro/cheque com 5% de desconto vai ficar de: R${preco_final_compras:,.2f}")
elif forma_pagamento == 3:
   preco_final_compras = valor_compras
   valor_parcelas = preco_final_compras / 2
   print(f"O preço passando em até 2x no cartão vai ficar de R${valor_parcelas:,.2f}, portanto o preço final vai ser de: {preco_final_compras:,.2f}")
elif forma_pagamento == 4:
   qtde_parcelas = int(input("Digite a quantidade de parcelas: "))
   if qtde_parcelas >= 3:
      preco_final_compras = valor_compras + (valor_compras * 0.20)
      valor_parcelas = preco_final_compras / qtde_parcelas
      print(f"O presso passando no cartão em {qtde_parcelas}x vai ficar de R${valor_parcelas:,.2f}, portanto o preço final vai ser de: R${preco_final_compras:,.2f}")
   else:
      print("Erro, a quantidade de parcelas dessa forma de pagamento só pode ser acima 3 ou mais.")
else:
   print("Número da forma de pagamento inexistente!")
