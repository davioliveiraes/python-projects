from random import randint
computador = randint(0, 10)
print("=========== JOGO DE ADVINHAÇÃO ===========")

acertou = False
qtde_de_tentativas = 0
while not acertou:
   jogador = int(input("Digite o seu palpite entre 0 a 10: "))
   qtde_de_tentativas += 1
   if jogador == computador:
      acertou = True
   else:
      if jogador > computador:
         print("Errou, é menor...")
      elif jogador < computador:
         print("Errou, é maior...")
print(f"PARABÉNS, VOCÊ ACERTOU! O NÚMERO É {computador} E COM {qtde_de_tentativas} TENTATIVAS!")