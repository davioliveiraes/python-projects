jogador = dict()
partidas = list()

jogador['Nome'] = str(input("Digite o nome do jogador: "))
total_partidas = int(input(f"Digite a quantidade de partidas que o {jogador['Nome']} jogou: "))

for count in range(0, total_partidas):
   partidas.append(int(input(f"     Quantos gols fez na partida {count+1}: ")))
jogador['Partidas'] = partidas[:]
jogador['gols'] = sum(partidas)

print("==" * 20)
print(jogador)
print("==" * 20)

for k, v in jogador.items():
   print(f"{k}: {v}")
print("==" * 20)

print(f"O jogador {jogador['Nome']} jogou {len(jogador['Partidas'])} partidas. ")
for i, g in enumerate(jogador['Partidas']):
   print(f"     => Na partida {i+1}, fez {g} gols")
aprov_jogador = (jogador['gols'] / total_partidas) * 100

print(f"O total de gols foi de: {jogador['gols']} gols.")
print(f"Aproveitament de gols: {aprov_jogador:.2f}%")
print("==" * 20)