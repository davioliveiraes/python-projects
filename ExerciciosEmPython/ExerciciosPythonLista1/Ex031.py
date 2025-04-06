from random import randint
from time import sleep

def jokenpo():
   print('''

   JOGO JOKENPÔ
         [1] - PEDRA
         [2] - PAPEL
         [3] - TESOURA
         [4] - SAIR DO JOGO

''')
   
   escolha_jogador = int(input('Escolha uma opção: '))
   if escolha_jogador == 4:
      print('Saindo do jogo...')
      return
   
   print('JO')
   sleep(1)
   print('KEN')
   sleep(1)
   print('PÔ')
   sleep(1)
   print("==" * 20)

   opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
   escolha_computador = randint(0, 2)
   print(f"Você escolheu: {opcoes[escolha_jogador - 1]}")
   print(f"O computador escolheu: {opcoes[escolha_computador]}")
   print("==" * 20)

   if escolha_jogador - 1 == escolha_computador:
      print("EMPATE!")
   elif (escolha_jogador == 1 and escolha_computador == 2) or \
        (escolha_jogador == 2 and escolha_computador == 0) or \
        (escolha_jogador == 3 and escolha_computador == 1):
      print("VOCÊ GANHOU!")
   else:
      print("VOCÊ PERDEU!")

   print("==" * 20)

   print("Deseja jogar novamente?")
   escolha_jogar_novamente = input("Digite [S] para sim ou [N] para não: ").strip().upper()
   if escolha_jogar_novamente == 'S':
      jokenpo()
   elif escolha_jogar_novamente == 'N':
      print("Saindo do jogo...")
   else:
      print("Opção inválida. Saindo do jogo...")

jokenpo()
   
