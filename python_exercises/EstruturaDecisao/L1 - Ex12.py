def main():
   valor_hora = float(input("Digite o valor da hora trabalhada: R$"))
   qtde_horas_mes = int(input("Digite a quantidade de horas trabalhadas no mês: "))

   salario_bruto = valor_hora * qtde_horas_mes

   if salario_bruto <= 900:
      desc_ir = 0
      desc_inss = 0
   elif 900 < salario_bruto <= 1500:
      desc_ir = 5
      desc_inss = 10
   elif 1500 < salario_bruto <= 2500:
      desc_ir = 10
      desc_inss = 15
   else:
      desc_ir = 20
      desc_inss = 25
   
   valor_desconto_ir = salario_bruto * (desc_ir / 100)
   valor_desconto_inss = salario_bruto * (desc_inss / 100)
   total_desconto = valor_desconto_ir + valor_desconto_inss
   salario_liquido = salario_bruto - total_desconto

   print("==" * 10)
   print(f"Salário Bruto: R${salario_bruto:,.2f}")
   print(f"(-) IR({desc_ir}%): R${valor_desconto_ir:,.2f}")
   print(f"(-) INSS({desc_inss}%): R${valor_desconto_inss:,.2f}")
   print(f"Total de descontos: R${total_desconto:,.2f}")
   print(f"Salário Líquido: R${salario_liquido:,.2f}")

if __name__ == "__main__":
   main()