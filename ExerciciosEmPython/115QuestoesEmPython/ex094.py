pessoa = dict()
sociedade = list()
soma_idades = 0

while True:
   pessoa.clear()
   pessoa['Nome'] = str(input("Digite o nome da pessoa: "))
   while True:
      pessoa['Sexo'] = str(input("Digite o sexo da pessoa[M/F]: ")).upper()[0]
      if pessoa['Sexo'] in 'MF':
         break
      print("ERRO!, Por favor digite apenas M(Masculino) ou F(Feminino).")
   pessoa['Idade'] = int(input("Digite a idade da pessoa: "))
   soma_idades += pessoa['Idade']
   sociedade.append(pessoa.copy())
   while True:
      resp = str(input("Deseja cadastrar uma nova pessoa[S/N]: ")).upper()[0]
      if resp in 'SN':
         break
   if resp == 'N':
      break

print("==" * 50)
print(f"Lista de pessoas cadastradas: {sociedade}")
print(f"A) Quantidade de pessoas cadastradas: {len(sociedade)}")
media_idade = soma_idades / len(sociedade)
print(f"B) Média de idade das pessoas cadastradas: {media_idade}")
print(f"C) Lista de mulheres: ", end=' ')
for p in sociedade:
   if p['Sexo'] in "Ff":
      print(f"{p['Nome']},", end=' ')
print()
print("D) Lista de pessoas com a idade acimda média: ")
if p in sociedade:
   if p['Idade'] >= media_idade:
      # print(f"{p['Nome']}")
      print("            ")
      for k, v in p.items():
         print(f"{k}: {v};", end=' ')
      print()
print("   <<< PROGRAMA ENCERRADO >>>  ")