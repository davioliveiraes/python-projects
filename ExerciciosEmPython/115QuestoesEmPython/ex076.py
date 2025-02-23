tabela_precos = ('Teclado', 300.99, 'Mouse', 150.89, 'Monitor', 1150.00, 'Headset', 350.99, 'Roteador', 120.49, 'Apple Watch', 599.99, 'Suporte Articulado', 250.00, 'Cabo HDMI', 69.90, 'Filtro de linha', 89.90)

print("==" * 20)
print(f"{"TABELA DE PREÇOS - LOJA KONOHA":^40}")
print("==" * 20)

for pos in range(0, len(tabela_precos)):
   if pos % 2 == 0:
      print(f"{tabela_precos[pos]:.<30}", end='')
   else:
      print(f"R${tabela_precos[pos]:>7.2f}")
print("==" * 40)