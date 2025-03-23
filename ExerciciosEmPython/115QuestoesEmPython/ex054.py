from datetime import date
de_maiores = 0
de_menores = 0
for count in range(1, 8):
   ano_nascimento = int(input(f"Digite o ano de nascimento da pessoa {count}ª: "))
   ano_atual = date.today().year
   idade = ano_atual - ano_nascimento
   if idade >= 18:
      de_maiores += 1
   elif idade < 18:
      de_menores += 1
   else:
      print("ERRO, TENTE NOVAMENTE!")
print(f"A quantidade de pessoas de maior de idade é: {de_maiores} pessoas.")
print(f"A quantidade de pessoas de menor de idade é: {de_menores} pessoas.")
