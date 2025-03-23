from math import factorial
number = int(input("Digite um número inteiro: "))
fatorial = factorial(number)
print(f"O fatorial de {number} é: {fatorial}")

print("==" * 30)

number_1 = int(input("Digite um número inteiro: "))
count_fatorial = number_1
fatorial_1 = 1
while count_fatorial > 0:
   print(f"{count_fatorial}", end="")
   print(" X " if count_fatorial > 1 else " = ", end="")
   fatorial_1 *= count_fatorial
   count_fatorial -= 1
print(f"{fatorial_1}")

print("==" * 30)

number_2 = int(input("Digite um número inteiro: "))
fatorial_2 = 1
for count_fatorial_2 in range(1, number_2 + 1):
   fatorial_2 *= count_fatorial_2
for count_fatorial_2 in range(1, number_2 + 1):
   if count_fatorial_2 == number_2:
      print(f"{number_2}")
   else:
      print(f"{count_fatorial_2} X ", end="")
print(f" = {fatorial_2}", end="")