ganho_por_hora = float(input("Digite o quanto você ganha por hora: R$"))
hora_por_dia = int(input("Digite quantas horas trabalha por no dia: "))
dias_trabalhados = int(input("Digite quantos dias você trabalhou esse mês: "))
salario_mes = (hora_por_dia * dias_trabalhados) * ganho_por_hora
print(f"O seu salário no final do mês é: R${salario_mes:.2f}")
