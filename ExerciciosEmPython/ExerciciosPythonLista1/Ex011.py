valor_a = int(input("Digite um valor inteiro: "))

while valor_a == 0:
   print("O coeficiente 'a' não pode ser igual a zero.")
   valor_a = int(input("Digite um valor inteiro diferente de zero: "))

valor_b = int(input("Digite outro valor inteiro: "))
valor_c = int(input("Digite mais um valor inteiro: "))

delta = valor_b ** 2 - 4 * valor_a * valor_c
print(f"O valor de delta dentro os valores {valor_a}, {valor_b}, {valor_c} é de: {delta}")
