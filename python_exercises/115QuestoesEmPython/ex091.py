from random import randint
from time import sleep
from operator import itemgetter

jogadas = {
   "Jogador1": randint(1, 6),
   "Jogador2": randint(1, 6),
   "Jogador3": randint(1, 6),
   "Jogador4": randint(1, 6)
}

ranking = list()
print("  <<< SORTEANDO AS JOGADAS >>>  ")
for k, v in jogadas.items():
   print(f"{k} obteve o resultado {v} no dado!")
   sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

print("==" * 20)
print("  <<< RANKING DOS JOGADORES >>> ")
for i, v in enumerate(ranking):
   print(f"   {i+1}° lugar: {v[0]} com {v[1]} pontos")
   sleep(1)
print("==" * 20)
print("\n")
print("PROGRAMA FINALIZADO")