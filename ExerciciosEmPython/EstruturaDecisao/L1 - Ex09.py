num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

lista_numeros = [num1, num2, num3]
lista_numeros.sort(reverse=True)
print(f"Números na ordem decrescente: {' '.join(map(str, lista_numeros))}")
