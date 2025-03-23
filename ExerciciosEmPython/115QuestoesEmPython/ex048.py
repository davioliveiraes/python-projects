print("Os números múltiplos de 3 no intervalo de 1 a 500 é: ")
soma_multi_3 = 0
cont_multi_3 = 0
for count in range(1, 501):
   if count % 3 == 0:
      print(".", end="")
      print(count, end="")
      soma_multi_3 += count
      cont_multi_3 += 1
print("\n")
print(f"A quantidade de números é: {cont_multi_3}")
print(f"A soma de todos esses números é: {soma_multi_3}")