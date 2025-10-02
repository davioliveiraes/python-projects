count_pares = 0
soma_pares = 0
for num in range(1, 7):
   num = int(input(f"Digite o número {num}°: "))
   if num % 2 == 0:
      count_pares += 1 
      soma_pares += num
print(f"A quantidade de números pares digitados é: {count_pares}")
print(f"A soma dos números pares mediante os números digitados é: {soma_pares}")
