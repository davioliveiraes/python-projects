from random import randint

print("==" * 20)
print(f"{"VAMOS JOGAR PAR OU ÍMPAR":^40}")
print("==" * 20)

vitorias = 0
while True:
   jogador = int(input("Digite um número que vai jogar: "))
   computador = randint(0, 11)
   total = jogar + computador
   tipo_numero = ''

   while tipo_numero not in "PI":
      tipo_numero = str(input("Você escolhe PAR ou ÍMPAR: ")).upper().strip()[0]
   print(f"Você jogou {jogador} e o computador jogou {computador}. E o total foi: {total}.")

   if tipo_numero == "P":
      if total % 2 == 0:
         print("Você venceu!")
         vitorias += 1
      else:
         print("O computador venceu!")
         break
   elif tipo_numero == "I":
      if total % 2 != 0:
         print("Você venceu!")
      else:
         print("O computador venceu!")
         break
   print("Vamos jogar novamente...")
   print("==" * 20)

