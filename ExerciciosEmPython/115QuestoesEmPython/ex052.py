num = int(input("Digite um número inteiro: "))
tot_vezes = 0
for count in range(1, num+1):
   if num % count == 0:
      print("\033[32m", end=" ")
      tot_vezes += 1
   else:
      print("\033[31m", end=" ")
   print(f"{count}", end=" ")
print(f"\n\033[m0 número {num} ele foi divisível por {tot_vezes}")
if tot_vezes == 2:
   print(f"Portanto ele é um número primo!")
else:
   print("Portanto ele não é um número primo!")
