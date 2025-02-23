lista_num = [[], []]

for n in range(0, 7):
   numero = int(input(f"Digite o {n+1}° número: "))
   if numero % 2 == 0:
      lista_num[0].append(numero)
   elif numero % 2 != 0:
      lista_num[1].append(numero)

lista_num[0].sort()
lista_num[1].sort()

print("==" * 30)
print(f"Lista completa de forma crescente: {lista_num}")
print(f"Lista só com os números pares de forma crescente: {lista_num[0]}")
print(f"Lista só com os números ímpares de forma crescente: {lista_num[1]}")
print("==" * 30)

