sexo = ""
while sexo != "M" and sexo != "F":
   sexo = str(input("Digite o seu sexo[M/F]: "))
   if sexo in "MF":
      print(f"O sexo {sexo} foi registrado com sucesso!")
   else:
      print("DADOS INVÁLIDOS! Por favor, digite corretamente...")
      
print("==" * 30)

sexo1 = str(input("Digite seu sexo[M/F]: ")).strip().upper()[0]
while sexo1 not in "MmFf":
   sexo1 = str(input("Dados inválidos. Por favor, digite seu sexo corretamente[M/F]: ")).strip().upper()[0]
print(f"O sexo {sexo1} foi registrado com sucesso!")
