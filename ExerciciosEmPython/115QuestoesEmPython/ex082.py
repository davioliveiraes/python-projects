lista_num = []
pares = []
impares = []

while True:
   lista_num.append(int(input("Digte um número: ")))

   resp = str(input("Deseja continuar[S/N]: "))
   if resp in "Nn":
      break

for i, num in enumerate(lista_num):
   if num % 2 == 0:
      pares.append(num)
   elif num % 2 != 0:
      impares.append(num)

lista_num.sort()
pares.sort()
impares.sort()

print("==" * 30)
print(f"A lista completa dos números digitados em ordem crescente: {lista_num}")
print(f"Lista só com os números pares: {pares}")
print(f"Lista só com os números ímpares: {impares}")
print("==" * 30)