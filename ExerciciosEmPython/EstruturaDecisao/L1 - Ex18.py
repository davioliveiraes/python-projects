try:
   valor_saque = int(input("Digite quantia que quer sacar(mínimo - R$10; máximo - R$600): R$"))
   if not (10 <= valor_saque <= 600):
      raise ValueError("Valor de saque fora do intervalo permitido.")
except ValueError as e:
   print(f"Error: {e}")
   exit()

notas_100 = notas_50 = notas_10 = notas_5 = notas_1 = 0

if valor_saque >= 100:
   notas_100 = valor_saque // 100
   valor_saque %= 100

if valor_saque >= 50:
   notas_50 = valor_saque // 50
   valor_saque %= 50

if valor_saque >= 10:
   notas_10 = valor_saque // 10
   valor_saque %= 10

if valor_saque >= 5:
   notas_5 = valor_saque // 5
   valor_saque %= 5

if valor_saque >= 1:
   notas_1 = valor_saque // 1
   valor_saque %= 1

print(" == NOTAS FORNECIDAS == ")
if notas_100 > 0:
   print(f"Notas de R$100: {notas_100}")
if notas_50 > 0:
   print(f"Notas de R$50: {notas_50}")
if notas_10 > 0:
   print(f"Notas de R$10: {notas_10}")
if notas_5 > 0:
   print(f"Notas de R$5: {notas_5}")
if notas_1 > 0:
   print(f"Notas de R$1: {notas_1}")


