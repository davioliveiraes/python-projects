salario_atual = float(input("Digite o seu salário atual: R$"))
aumento = int(input("Digite em percentual quanto você teve de aumento(não precisa colocar o percentual): "))
salario_aumento = salario_atual + (salario_atual * (aumento/100))
print(f"O seu salário com aumento de {aumento}%, vai ficar de: R${salario_aumento:,.2f}")