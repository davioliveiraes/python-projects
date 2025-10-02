soma_idade = 0
media_idade = 0
maior_idade_h = 0
nome_maior_idade_h = 0
qtde_menos_idade_20M = 0

for p in range(1, 5):
   print(f"===== {p}º Pessoa =====")
   nome = str(input("Digite o nome: "))
   idade = int(input("Digite a idade: "))
   sexo = str(input("Digite o sexo[M/F]: ")).upper()
   soma_idade += idade
   media_idade = soma_idade / 4

   if p == 1 and sexo in "M":
      maior_idade_h = idade
      nome_maior_idade_h = nome
   else:
      if idade > maior_idade_h and sexo in "M":
         maior_idade_h = idade
         nome_maior_idade_h = nome

   if idade < 20 and sexo in "F":
      qtde_menos_idade_20M += 1

print("=" * 30)
print(f"A média de idade do grupo é: {media_idade}")
print(f"O homem mais velho é: {nome_maior_idade_h}")
print(f"A quantidade de mulheres abaixo de 20 anos é: {qtde_menos_idade_20M}")