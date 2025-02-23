from random import randint
from time import sleep
escolha_computador = randint(0, 2)
itens = ("PEDRAS", "PAPEL", "TESOURA")
print(f"{"GAME JOKEMPÔ":=^40}")
print(f"{"PEDRA-PAPEL-TESOURA":=^40}")
print('''

   (0) - PEDRA
   (1) - PAPEL
   (2) - TESOURA

''')

escolha_usuario = int(input("Faça sua escolha digitando o número correspondente: "))

sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!")

if escolha_computador == escolha_usuario:
   print("DEU EMPATE!")
elif escolha_computador == 0 and escolha_usuario == 2 or escolha_computador == 1 and escolha_usuario == 0 or escolha_computador == 3 and escolha_usuario == 0:
   print(f"Você perdeu!!!, Escolha do computador: {escolha_computador} - Sua escolha: {escolha_usuario}")
else:
   print(f"Você ganhou!!!, Escolha do computador:  {escolha_computador} - Sua escolha: {escolha_usuario}")
