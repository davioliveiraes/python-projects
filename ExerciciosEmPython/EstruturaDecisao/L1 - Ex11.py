salario_colaborador = float(input("Digite o seu salário: R$ "))

if salario_colaborador <= 280:
   print(f"Salário antes do reajuste: R${salario_colaborador:,.2f}")
   percentual = 20
   valor_aumento = salario_colaborador * 0.20
   novo_salario = salario_colaborador + valor_aumento
elif 280 < salario_colaborador < 700:
   print(f"Salário antes do reajuste: R${salario_colaborador:,.2f}")
   percentual = 15
   valor_aumento = salario_colaborador * 0.15
   novo_salario = salario_colaborador + valor_aumento
elif 700 <= salario_colaborador <= 1500:
   print(f"Salário antes do reajuste: R${salario_colaborador:,.2f}")
   percentual = 10
   valor_aumento = salario_colaborador * 0.10
   novo_salario = salario_colaborador + valor_aumento
elif salario_colaborador >= 1500:
   print(f"Salário antes do reajuste: R${salario_colaborador:,.2f}")
   percentual = 5
   valor_aumento = salario_colaborador * 0.05
   novo_salario = salario_colaborador + valor_aumento

print("==" * 20)
print(f"O percentual de aumento aplicado: {percentual}%")
print(f"O valor do aumento: R${valor_aumento}")
print(f"O novo salário, após aumento: R${novo_salario}")
