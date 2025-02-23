ganho_por_hora = float(input("Digite quanto ganha por hora: R$"))
horas_trabalhadas_mes = int(input("Digite a quantidade de horas trabalhadas no mês: "))

salarioBruto = ganho_por_hora * horas_trabalhadas_mes
IR = salarioBruto * 0.11
INSS = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - (IR + INSS + sindicato)

print(f"Salário Bruto: R${salarioBruto}; Descontos - IR: R${IR}, INSS: R${INSS}, Sindicato: R${sindicato}")
print(f"O salário líquido a receber vai ser de: R${salarioLiquido}")
