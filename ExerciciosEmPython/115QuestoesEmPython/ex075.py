tupla_numeros = (int(input("Digite um número: ")), int(input("Digite outro número: ")), int(input("Digite uum outro número: ")), int(input("Digite mais um número: ")))

print(f"A tupla gerada: {tupla_numeros}")
print(f"O número 9 apareceu: {tupla_numeros.count(9)} vezes")

if 3 in tupla_numeros:
   print(f"O número 3 aparece na: {tupla_numeros.index(3)+1}ª posição")
else:
   print(f"O número 3 não foi encontrado!")

print("Os números pares da tupla são: ", end=' ')
for num in tupla_numeros:
   if num % 2 == 0:
      print(num, end=' ')