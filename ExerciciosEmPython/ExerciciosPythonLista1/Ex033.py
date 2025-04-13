valor_casa = float(input("Qual é o valor da casa: R$ "))
salario_comprador = float(input("Qual é o seu salário: R$ "))
anos_pagamento = int(input("Em quantos anos você pretende pagar: "))
prestacao_mensal = valor_casa / (anos_pagamento * 12)
minimo = salario_comprador * 0.30

if prestacao_mensal <= minimo:
   print("==" * 30)
   print(f"Valor casa: R$ {valor_casa:.2f}")
   print(f"Salário: R$ {salario_comprador:.2f}")
   print(f"Prazo: {anos_pagamento} anos")
   print(f"Prestação mensal: R$ {prestacao_mensal:.2f}")
   print(f"Valor minimo: R$ {minimo:.2f}")
   print("Empréstimo aprovado!")
else:
   print("==" * 30)
   print(f"Valor casa: R$ {valor_casa:,.2f}")
   print(f"Salário: R$ {salario_comprador:,.2f}")
   print(f"Prazo: {anos_pagamento} anos")
   print(f"Prestação mensal: R$ {prestacao_mensal:,.2f}")
   print(f"Valor minimo: R$ {minimo:,.2f}")
   print("Empréstimo negado!")

