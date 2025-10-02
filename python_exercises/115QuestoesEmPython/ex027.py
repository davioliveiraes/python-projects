n = str(input("Digite seu nome completo: "))
nome_completo = n.split()
print(f"O seu primeiro nome é: {nome_completo[0]}")
print(f"O seu último nome é: {nome_completo[len(nome_completo)-1]}")
