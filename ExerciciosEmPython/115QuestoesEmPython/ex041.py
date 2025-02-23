from datetime import date
ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = date.today().year

idade = ano_atual - ano_nascimento

print(f"O atleta tem {idade} anos!")
if idade <= 9:
   print("Categoria MIRIM!")
elif 9 < idade <= 14:
   print("Categoria INFANTIL!")
elif 14 < idade <= 19:
   print("Categoria JÚNIOR")
elif 19 < idade <= 25:
   print("Categoria SÊNIOR")
elif idade > 25:
   print("Categoria MASTER")
else:
   print("NÃOI SE ENCAIXA EM NENHUMA CATEGORIA!")