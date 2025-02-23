lista_valores_num = []
while True:
   num = int(input("Digite um valor númerico inteiro: "))
   lista_valores_num.append(num)

   resp = str(input("Deseja continuar[S/N]: "))
   if resp == 'n' or resp == 'N':
      break

print("==" * 30)
qtde_num = len(lista_valores_num)
print(f"A quantidade de elementos que foi digitado: {qtde_num}")
lista_valores_num.sort(reverse=True)
print("==" * 30)

if 5 in lista_valores_num:
   print("O valor 5 foi encontrado, portanto está na lista!")
else:
   print("O valor 5 não foi encontrado, portanto não está na lista.")

print("==" * 30)
print(f"A lista dos valores númericos em uma ordem decrescente: {lista_valores_num}")