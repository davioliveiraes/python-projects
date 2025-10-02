from datetime import datetime
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
idade = datetime.now().year - ano_nascimento
print(f"Idade: {idade}")

if idade >= 16 and idade <= 70:
   print("De acordo com sua idade, é obrigatório votar.")
else:
   print("De acordo com sua idade, não é obrigatório votar.")
