numeros = list()
while True:
   num = int(input("Digite um número inteiro: "))
   if num not in numeros:
      numeros.append(num)
      print("O número foi adicionado com sucesso.")
   else:
      print("O número já foi adicionado, não vai ser colocado.")
   
   resp = str(input("Deseja continuar[S/N]: "))
   if resp == 'n' or resp == 'N':
      break

print("==" * 30)
numeros.sort()
print(f"A lista crescente dos valores únicos digitados é: {numeros}")