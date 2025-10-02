nome_completo = str(input("Digite seu nome completo: "))
uppercase_text = nome_completo.upper()
lowercase_text = nome_completo.lower()
no_spaces = nome_completo.replace(" ", "")
len_nome_completo = len(no_spaces)
first_name = nome_completo.split()[0]
len_first_name = len(first_name)

print(f"Seu nome em letras maiúsculas: {uppercase_text}")
print(f"Seu nome em letras minúsculas: {lowercase_text}")
print(f"Quantidade de letras ao todo do seu nome completo sem contar os espaços é: {len_nome_completo} letras")
print(f"Quantidade de letras do primeiro nome: {len_first_name} letras")

print("==================================================================================")

nome_completo = str(input("Digite o seu nome completo: ")).strip()
print("ANALISANDO SEU NOME...")
print(f"Seu nome em letras maiúsculas é: {nome_completo.upper()}")
print(f"Seu nome completo ao todo tem {nome_completo.lower()} letras")
print(f"Seu nome completo ao todo tem {nome_completo.count(" ")}")
# print(f"Seu primeiro nome tem {nome_completo.find(" ")}")
split_nome_completo = nome_completo.split()
print(f"Seu primeiro nome é {split_nome_completo[0]} e tem {len(split_nome_completo[0])}")