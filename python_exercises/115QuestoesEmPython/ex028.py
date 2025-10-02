from random import randint
from time import sleep
computador = randint(0, 5)
print("==" * 35)
print("JOGO DA ADIVINHAÇÃO - O COMPUTADOR ELA VAI GERAR UM NÚMERO DE 0 A 5 - TENTE ADIVINHAR QUE NÚMERO É.")
print("==" * 35)
jogador = int(input("Digite um número: "))
print("PROCESSANDO...")
sleep(3)
if jogador == computador:
   print(f"Parabéns, você ganhou. Número: {computador}")
else:
   print(f"Você perdeu, o número era {computador}")