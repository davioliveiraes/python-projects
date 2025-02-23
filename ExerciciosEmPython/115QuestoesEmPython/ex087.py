matriz = [0,0,0], [0,0,0], [0,0,0]
soma_pares = soma_3_coluna = maior_2_linha = 0
for l in range(0, 3):
   for c in range(0, 3):
      matriz[l][c] = int(input(f"Digite um número na posição[{l}, {c}]: "))
print("==" * 30)
for l in range(0, 3):
   for c in range(0, 3):
      print(f"[{matriz[l][c]:^3}]", end='')
      if matriz[l][c] % 2 == 0:
         soma_pares += matriz[l][c]
   print()
print("==" * 30)
for l in range(0, 3):
   soma_3_coluna += matriz[l][2]
for c in range(0, 3):
   if c == 0:
      maior_2_linha = matriz[l][2]
   elif matriz[1][c] > maior_2_linha:
      maior_2_linha = matriz[1][c]
print("==" * 30)
print(f"A soma dos valores pares é: {soma_pares}")
print(f"A soma dos valores da terceira coluna é: {soma_3_coluna}")
print(f"O maior valor da segunda linha é: {maior_2_linha}")
print("==" * 30)