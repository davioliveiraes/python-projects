numero = int(input("Digite um número inteiro para gerar a tabuada: "))
print("===" * 5)
for count in range(0, 11):
   print(f"{numero} x {count} = {numero * count}")
print("===" * 5)