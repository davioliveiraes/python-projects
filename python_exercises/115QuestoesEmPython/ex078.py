print("==" * 25)
print(f"{'DIGITANDO 5 VALORES - MAIOR OU MENOS':^50}")
print("==" * 25)

lista_numeros = []
for count in range(0, 5):
   lista_numeros.append(int(input(f"Digite um número na posição {count}ª: ")))
   if count == 0:
      maior_numero = menor_numero = lista_numeros[count]
   else:
      if lista_numeros[count] > maior_numero:
         maior_numero = lista_numeros[count]
      if lista_numeros[count] < menor_numero:
         menor_numero = lista_numeros[count]

print("==" * 25)
print(f"A lista de números digitados é: {lista_numeros}")
print("==" * 25)

print(f"O maior número digitado é: {maior_numero} nas posições: ", end='')
for pos, num in enumerate(lista_numeros):
   if num == maior_numero:
      print(f"{pos}ª...", end='')
print("\n", "==" * 25)

print(f"O menor número digitado é: {menor_numero} nas posições: ", end='')
for pos, num in enumerate(lista_numeros):
   if num == menor_numero:
      print(f"{pos}ª...", end='')