from datetime import date
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
sexo = str(input("Digite o seu sexo[M/F]: "))
ano_atual = date.today().year

idade = ano_atual - ano_nascimento
passou_alista = idade - 18
falta_alista = 18 - idade

ano_deveria_alistar = ano_atual - passou_alista
ano_vai_alistar = ano_atual + falta_alista

if sexo == "f" or sexo == "F":
   print("Olá, você não precisa está fazendo o alistamento.")

if sexo == "M" or sexo == "m":
   print(f"Quem nasceu em {ano_nascimento} vai ter {idade} anos em {ano_atual}")
if idade == 18 and (sexo == "M" or sexo == "m"):
   print("Você precisa se alista imediatamento!")
elif idade > 18 and (sexo == "M" or sexo == "m"):
   print(f"Você passou {passou_alista} anos para poder se alistar.")
   print(f"Você deveria ter se alistado em {ano_deveria_alistar}")
elif idade < 18 and (sexo == "M" or sexo == "m"):
   print(f"Você ainda falta {falta_alista} anos para poder se alista.")
   print(f"Você vai se alistar em {ano_vai_alistar}")
