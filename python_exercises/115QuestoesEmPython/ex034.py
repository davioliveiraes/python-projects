salario_func = float(input("Digite o seu salário: R$"))
if salario_func > 1250:
   novo_salario = salario_func + (salario_func * 0.10)
elif salario_func <= 1250:
   novo_salario = salario_func + (salario_func * 0.15)

print(f"De acordo com o salário digitado. O seu novo salário vai ser de R${novo_salario:,.2f}")