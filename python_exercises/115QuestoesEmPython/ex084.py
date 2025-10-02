lista_pessoas = []
dados = []
maior_peso = menor_peso = 0

while True:
   dados.append(str(input("Digite o nome da pessoa: ")))
   dados.append(float(input("Digite o peso da pessoa: ")))

   if len(lista_pessoas) == 0:
      maior_peso = menor_peso = dados[1]
   else:
      if dados[1] > maior_peso:
         maior_peso = dados[1]
      if dados[1] < menor_peso:
         menor_peso = dados[1]
   
   lista_pessoas.append(dados[:])
   dados.clear()

   resp = str(input("Deseja continuar[S/N]: "))
   if resp in "Nn":
      break

print("==" * 30)
print(f"A quantidade de pessoas cadastrados foram: {len(lista_pessoas)}")
print(f"O maior peso foi: {maior_peso}KG", end=' ')
for i, pessoa in enumerate(lista_pessoas):
   if pessoa[1] == maior_peso:
      print(f"[{pessoa[0]}]", end='')
print(f"O menor peso foi: {menor_peso}KG", end=' ')
for i, pessoa in enumerate(lista_pessoas):
   if pessoa[1] == menor_peso:
      print(f"[{pessoa[0]}]", end=' ')
print("\n", "==" * 30)

print(f"Lista de todos os cadastrados: {lista_pessoas}")