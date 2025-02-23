num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

if num1 > num2 and num1 > num3:
   print(f"O maior número é: {num1}")
elif num2 > num1 and num2 > num3:
   print(f"O maior número é: {num2}")
elif num3 > num1 and num3 > num2:
   print(f"O maior número é: {num3}")

if num1 < num2 and num1 < num3:
   print(f"O menor número é: {num1}")
elif num2 < num1 and num2 < num3:
   print(f"O menor número é: {num2}")
elif num3 < num1 and num3 < num2:
   print(f"O menor número é: {num3}")

print("==" * 30)

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

maior_numero = n1
if n2 > n1 and n2 > n3:
   maior_numero = n2
if n3 > n1 and n3 > n2:
   maior_numero = n3

menor_numero = n1
if n2 > n1 and n2 > n3:
   menor_numero = n2
if n3 > n1 and n2 > n3:
   menor_numero = n3

print(f"O maior número digitado é: {maior_numero}")
print(f"O menor número digitado é: {menor_numero}")