peso_peixes = float(input("Digite o peso dos peixes: "))
if peso_peixes > 50:
   peso_excesso = peso_peixes - 50
   multa_pagar = peso_excesso * 4

print(f"PESO TOTAL DE PEIXES: {peso_peixes:.3f}KG")
print(f"PESO EXCESSO: {peso_excesso:.3f}KG")
print(f"MULTA PELO EXCESSO DE PESO LIMITE: R${multa_pagar:,.2f}")
