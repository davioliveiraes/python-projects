nome_func = str(input("Digite um nome de funcionário: "))
salario = float(input("Digite o salário do funcionário: "))
tempo_servico = int(input("Digite o tempo de serviço do funcionário: "))

try:
   if tempo_servico < 3:
      novo_salario = salario + (salario * 0.03)
      print(f"Funcionário: {nome_func} - Salário: R${novo_salario:.2f} - Aumento de 3%")
   elif 3 <= tempo_servico < 10:
      novo_salario = salario + (salario * 0.125)
      print(f"Funcionário: {nome_func} - Salário: R${novo_salario:.2f} - Aumento de 12.5%")
   elif tempo_servico >= 10:
      novo_salario = salario + (salario * 0.2)
      print(f"Funcionário: {nome_func} - Salário: R${novo_salario:.2f} - Aumento de 20%")
except ValueError as e:
   print(f"Erro: {e}")
