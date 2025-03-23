# Pergunta: Escreva um programa que possa calcular o fatorial de um dado número. Os resultados devem ser impressos em uma sequência separada por vírgulas em uma única linha. Suponha que a seguinte entrada seja fornecida ao programa: 8 Então, a saída deve ser: 40320

# Dicas: No caso de dados de entrada serem fornecidos à pergunta, deve-se presumir que seja uma entrada de console.

# Alternativa 1
def fatorial(num):
   if num == 0 or num == 1:
      return 1
   else:
      return num * fatorial(num - 1)

number = int(input("Digite um número inteiro: "))
result = fatorial(number)
print(f"Fatorial do número: {number} é: {result}")

print()

# Alternativa 2
def fatorial2(n):
   if n == 0 or n == 1:
      return 1
   else:
      return n * fatorial2(n - 1)

n = int(input("Digite um número inteiro: "))
print(fatorial2(n))

