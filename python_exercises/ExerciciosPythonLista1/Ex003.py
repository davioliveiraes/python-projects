nome = str(input("Digite seu nome: "))
salario = float(input("Digite seu salário: "))

print(f"Nome do funcionário: {nome}")
print(f"Salário: {salario:,.2f}")
print(f"O funcionário {nome} tem um salário de R${salario:,.2f} em Junho.")