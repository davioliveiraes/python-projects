aprov_jogador = dict()
aprov_jogador['Nome'] = str(input("Digite o nome do jogador: "))
aprov_jogador['Partidas'] = int(input("Digite quantas partidas jogou: "))
aprov_jogador['Quantidade total de gols'] = int(input("Digite a quantidade total de jogos: "))

aprov_jogador['Gols por partida'] = aprov_jogador['Quantidade total de gols'] / aprov_jogador['Partidas']

aprov_jogador['Aproveitamento(%)'] = (aprov_jogador['Quantidade total de gols']) / aprov_jogador['Partidas'] * 100
print("==" * 20)
print("   <<< APROVEITAMENTO DE JOGADOR >>>  ")
for k, v in aprov_jogador.items():
   print(f"{k}: {v:.2f}" if isinstance(v, float) else f"{k}: {v}")
print("==" * 20)