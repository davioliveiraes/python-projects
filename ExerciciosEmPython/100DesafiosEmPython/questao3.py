# Pergunta: Com um número inteiro n dado, escreva um programa para gerar um dicionário que contenha (i, i*i) tal que seja um número integral entre 1 e n (ambos incluídos). e então o programa deve imprimir o dicionário. Suponha que a seguinte entrada seja fornecida ao programa: 8 Então, a saída deve ser: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# Dicas: No caso de dados de entrada serem fornecidos à pergunta, deve-se presumir que seja uma entrada de console. Considere usar dict()

# Alternativa 1
num = int(input("Digite um número inteiro: "))
dic = dict()

for n in range(1, num+1):
   dic[n] = n*n

print(dic)

print()

def gerar_dicionario(n):
   dicionario = {i: i * i for i in range(1, n+1)}
   return dicionario

n = int(input("Digite um número inteiro: "))
result = gerar_dicionario(n)
print(f"Dicionário: {result}")