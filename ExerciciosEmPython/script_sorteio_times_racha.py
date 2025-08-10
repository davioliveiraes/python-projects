import random

num_times = 8
num_jogadores = 16

jogadores_originais = []

for i in range(num_jogadores):
   nome = str(input(f"NOME DO JOGADOR {i + 1}: "))
   habilidade = int(input(f"HABILIDADE DO JOGADOR {i+1}(1a5): "))
   jogadores_originais.append((nome, habilidade))

for sorteio in range(4):
   jogadores = jogadores_originais.copy()
   habilidades = [j[1] for j in jogadores]
   times = [[]for _ in range(num_times)]

   while habilidades:
      random.shuffle(times)
      for i in range(num_times):
         if not habilidades:
            break
         if len(times[i]) < num_jogadores // num_times:
            jogador = jogadores[habilidades.index(max(habilidades))]
            times[i].append(jogador)
            habilidades.remove(jogador[1])
            jogadores.remove(jogador)
   
   print(f"SORTEIO {sorteio+1}: ")
   for i, time in enumerate(times):
      print(f"Time {i+1}: {[j[0] for j in time]}")
   print()
