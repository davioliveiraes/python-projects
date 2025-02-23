num = qtda_num_digitados = soma = 0

while True:
   num = int(input("Digite um número[999 para parar]: "))
   if num == 999:
      break
   qtda_num_digitados += 1
   soma += num

print(f"A quantidade de números digitados foi: {qtda_num_digitados} e a soma entre eles foi: {soma}.")
