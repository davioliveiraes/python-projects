# Opção 1
print("Os números pares desse intervalo é: ")
for count in range(1, 51):
   print(".", end="")
   if count % 2 == 0:
      print(count, end=" ")

# Opção 2
print("\n")
print("Os numéros pares desse intervalo é: ")
for i in range(2, 51, 2):
   print(".", end=" ")
   print(i, end=" ")

# Opção 3
print("\n")
ultimo_valor = int(input("Digite o último valor do intervalo: "))
print("OS NÚMEROS PARES DO INTERVALO:  ")
for count in range(1, ultimo_valor+1):
   print(".", end="")
   if count % 2 == 0:
      print(count, end="")
