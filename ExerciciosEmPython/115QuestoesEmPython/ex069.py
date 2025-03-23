print("==" * 20)
print(f"{"CADASTRO DE PESSOAS":^40}")
print("==" * 20)

pessoas_mais_18 = homens_cadastrados = mulheres_menos_20 = 0

while True:
   idade = int(input("Digite sua idade: "))

   sexo = ' '
   while sexo not in "MF":
      sexo = str(input("Digite seu sexo[M/F]: ")).upper().strip()[0]

   if idade > 18:
      pessoas_mais_18 += 1
   if sexo == "M" or sexo == "m":
      homens_cadastrados += 1
   if idade < 20 and sexo == "F" or sexo == "f":
      mulheres_menos_20 += 1
   
   deseja_continuar = ' '
   while deseja_continuar not in 'SN':
      deseja_continuar = str(input("Deseja continuar[S/N]: ")).upper().strip()[0]
   if deseja_continuar == 'N':
      break

print("==" * 30)
print(f"A quantidade de pessoas com mais 18 anos cadastradas são: {pessoas_mais_18}")
print(f"A quantidade de homens cadastrados são: {homens_cadastrados}")
print(f"A quantidade de mulheres com menos de 20 anos cadastradas são: {mulheres_menos_20}")
print("==" * 30)