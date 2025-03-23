from copy import deepcopy
jogador = dict()
partidas = list()
time = list()

while True:
   jogador['Nome'] = str(input("Digite o nome do jogador: "))
   tot_partidas = int(input(f"Digite a quantidade de partidas que o jogador {jogador['Nome']} jogou: "))
   partidas.clear()
   for count in range(0, tot_partidas):
      partidas.append(int(input(f"  Quantos gols fez na partida {count+1}: ")))
   jogador['Partidas'] = partidas[:]
   jogador['gols'] = sum(partidas)
   time.append(deepcopy(jogador))
   while True:
      resp = str(input("Deseja cadastrar um novo jogador[S/N]: ")).upper()[0]
      if resp in 'SN':
         break
   if resp == 'N':
      break
print("==" * 20)
print("COD ", end='')
for i in jogador.keys():
   print(f"{i:<10}", end='')
print()
print("==" * 20)
for k, v in enumerate(time):
   print(f"{k:>3}", end='')
   for d in v.values():
      print(f"{str(d):<10}", end='')
   print()
print("==" * 20)

while True:
   buscar = int(input("Mostrar dados de qual jogador(999 para sair): "))
   if buscar == 999:
      break
   if buscar >= len(time):
      print(f"ERRO!, Não existe jogador com o código {buscar}.")
   else:
      print(f" >>> LEVANTAMENTO DO JOGADOR {time[buscar]['Nome']} <<< ")
      for i, g in enumerate(time[buscar]['Partidas']):
         print(f"   No jogo {i+1} fez {g} gols.")
      aproveitamento = time[buscar]['gols'] / len(time[buscar]['Partidas'])
      print(f"       Média de gols: {aproveitamento:.1f} gols por jogo;")
      print(f"       Aproveitamento de: {aproveitamento * 100:.1f}%")
   print("==" * 20)
print("  <<< OBRIGADO POR USAR O PROGRAMA, VOLTE SEMPRE! >>> ")
