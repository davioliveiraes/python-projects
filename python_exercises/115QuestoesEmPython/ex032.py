# Para o ano ser bissexto precisa ser divisível por 4 e não ser por 100 ou ser divisível por 400

from datetime import date
ano = int(input("Digite um ano e descubra se ele é bissexto (caso voc~e digitar 0 ele vai pegar o ano atual): "))
if ano == 0:
   ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
   print(f"O ano {ano} ele é um ano bissexto.")
else:
   print(f"O ano {ano} ele não é um ano bissexto.")

