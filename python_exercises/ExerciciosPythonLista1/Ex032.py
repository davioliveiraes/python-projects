from random import randint

escolha_computador = randint(1, 5)

while True:
   escolha_jogador = int(input("Escolha um número entre 1 e 5: "))
   if escolha_jogador < 1 or escolha_jogador > 5:
      print("Numero inválido! Tente novamente.")
   if escolha_jogador < escolha_computador:
      print("Você errou! O número é maior.")
   elif escolha_jogador > escolha_computador:
      print("Você errou! O número é menor.")
   elif escolha_jogador == escolha_computador:
      print(f"Você acertou! Parabéns! - Número sorteado: {escolha_computador}")
      break

print("FIM DE JOGO!")
   
   
