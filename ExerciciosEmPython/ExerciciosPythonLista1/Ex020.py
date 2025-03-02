try:
   numero = int(input("Digite um número inteiro: "))

   if numero % 2 == 0:
      print(f"O número {numero} ele é: PAR")
   elif numero % 2 != 0:
      print(f"O número {numero} ele é: ÍMPAR")

except ValueError:
   print("ERRO. Por favor digite um número inteiro.")
