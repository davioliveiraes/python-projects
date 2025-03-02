nome = str(input("Digite o seu nome: "))
sexo = str(input("Digite o seu sexo[M - Masculino; F - Feminino]: ")).upper()
valor_compras = float(input("Digite o valor das compras: R$"))

if sexo == "M":
   valor_cobrado = valor_compras - (valor_compras * 0.05)
   print(f"Olá {nome} você ganhou 5% de desconto em suas compras. Valor cobrado: R${valor_cobrado:,.2f}")
elif sexo == "F":
   valor_cobrado = valor_compras - (valor_compras * 0.13)
   print(f"Olá {nome} você ganhou 13% de desconto em suas compras. Valor cobrado: R${valor_cobrado:,.2f}")

print("OBRIGADO!!!")