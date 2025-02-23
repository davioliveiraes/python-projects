valor = qtde_valores = soma_valores = maior_valor = menor_valor = 0
media_valor = 0.0
continuar_dig_valor = "S"

while continuar_dig_valor in "Ss":
   valor = int(input("Digite um valor: "))
   qtde_valores += 1
   soma_valores += valor

   if qtde_valores == 1:
      maior_valor = menor_valor = valor
   else:
      if valor > maior_valor:
         maior_valor = valor
      if valor < menor_valor:
         menor_valor = valor
   
   continuar_dig_valor = str(input("Deseja continuar[S/N]: ")).upper().strip()[0]

media_valor = soma_valores / qtde_valores

print("==" * 15)
print(f"A média mediante os valores digitados é: {media_valor:.2f}")
print(f"O maior valor mediante os valores digitados é: {maior_valor}")
print(f"O menor valor mediante os valores digitados é: {menor_valor}")
print("==" * 15)
