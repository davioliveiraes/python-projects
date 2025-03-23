from datetime import datetime
dados = dict()
dados['Nome'] = str(input("Digite o seu nome: "))
dados['Sexo'] = str(input("Digite o seu sexo[M/F]: "))
ano_nasc = int(input("Digite o seu ano de nascimento: "))
dados['Idade'] = datetime.now().year - ano_nasc
dados['CTPS'] = int(input("Digite o número da Carteira de Trabalho (0 para não tem): "))

if dados['CTPS'] != 0 and dados['Sexo'] == "M" or dados['Sexo'] == 'm':
   dados['Ano_contracao'] = int(input("Digite o ano de contratação: "))
   dados['Salario'] = float(input("Digite o seu salário: R$"))
   dados['Aposentadoria'] = (dados['Idade'] + dados['Ano_contracao'] + 35) - datetime.now().year

elif dados['CTPS'] != 0 and dados['Sexo'] == 'F' or dados['Sexo'] == 'f':
   dados['Ano_contracao'] = int(input("Digite o ano de contração: "))
   dados['Salario'] = float(input("Digite o seu salário: R$"))
   dados['Aposentadoria'] = (dados['Idade'] + dados['Ano_contracao'] + 30) - datetime.now().year

print("==" * 30)
for k, v in dados.items():
   print(f"{k}: {v}")