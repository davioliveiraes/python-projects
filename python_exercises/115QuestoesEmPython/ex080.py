lista_valores_num = []
for count in range(0, 5):
   num = int(input("Digite um valor númerico inteiro: "))
   if count == 0 or num > lista_valores_num[len(lista_valores_num)-1]:
      lista_valores_num.append(num)
      print("Valor adicionado no final da lista...")
   else:
      pos = 0
      while pos < len(lista_valores_num):
         if num <= lista_valores_num[pos]:
            lista_valores_num.insert(pos, num)
            print(f"O valor foi adicionado na posição {pos}ª")
            break
         pos += 1
print("==" * 30)
print(f"A lista dos valores númericos ordenados vai ser: {lista_valores_num}")