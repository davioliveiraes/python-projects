# Pergunta: Escreva um programa que encontre todos os números que são divisíveis por 7, mas não são múltiplos de 5, entre 2000 e 3200 (ambos incluídos). Os números obtidos devem ser impressos em uma sequência separada por vírgulas em uma única linha.

# Dicas: Considere usar o método range(#begin, #end)

# Alterntiva 1
lista = []
for num in range(2000, 3201):
   if num % 7 == 0 and not num % 5 == 0:
      lista.append(str(num))

print(",".join(lista))

print()

# Alternativa 2
lista2 = []
for num in range(2000, 3201):
   if (num%7==0) and (num%5!=0):
      lista2.append(str(num))

print(",".join(lista))
