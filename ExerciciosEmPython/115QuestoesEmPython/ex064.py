count = soma = 0
valor = int(input("Digite um valor[999 para parar]: "))

while valor != 999:
   count += 1
   soma += valor
   valor = int(input("Digite um valor[999 para parar]: "))
print(f"A quantidade de números digitados foi {count} e a soma deles é {soma}.")