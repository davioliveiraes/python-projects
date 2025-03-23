from datetime import datetime

try:

   ano_nascimento = int(input("Digite o ano nascimento: "))
   ano_atual = datetime.today().year

   idade_alistamento = 18
   idade_rapaz = ano_atual - ano_nascimento

   if idade_rapaz == 18:
      print("Acabou de fazer o alistamento.")
   elif idade_rapaz < 18:
      falta_alistamento = idade_alistamento - idade_rapaz
      print(f"Falta {falta_alistamento} anos para o alistamento.")
   elif idade_rapaz > 18:
      tempo_alistamento = idade_rapaz - idade_alistamento
      print(f"Tempo de alistamento de {tempo_alistamento} anos.")

except ValueError:
   print("ERRO. Por favor digite corretamento o ano pedido.")