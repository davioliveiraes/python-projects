from datetime import datetime

ano_atual = datetime.now().year
mes_atual = datetime.now().month

ano_nascimento = int(input("Digite o ano de nascimento: "))
mes_nascimento = int(input("Digite o mês de nascimento(1-12): "))

idade = ano_atual - ano_nascimento

if mes_nascimento > mes_atual:
   idade -= 1
if idade < 16:
   print(f"Você tem {idade} anos e NÃO pode votar.")
elif 16 <= idade < 18 or idade >= 70:
   print(f"Você tem {idade} anos e o voto é opcional.")
else:
   print(f"Você tem {idade} anos e o voto é obrigatório.")
