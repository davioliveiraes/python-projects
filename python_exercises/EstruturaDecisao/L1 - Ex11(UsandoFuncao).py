def main():
   salario_colaborador = float(input("Digite o seu salário atual: R$"))
   if salario_colaborador <= 280:
      percentual_aumento = 20
   elif 280 <= salario_colaborador < 700:
      percentual_aumento = 15
   elif 700 <= salario_colaborador < 1500:
      percentual_aumento = 10
   else:
      percentual_aumento = 5
   
   valor_aumento = salario_colaborador * (percentual_aumento / 100)
   novo_salario = salario_colaborador + valor_aumento

   print("==" * 20)
   print(f"Salário antes do reajuste: R${salario_colaborador:,.2f}")
   print(f"O percentual de aumento aplicado: {percentual_aumento}%")
   print(f"O valor do aumento: R${valor_aumento:,.2f}")
   print(f"Novo salário, após o aumento: R${novo_salario:,.2f}")

if __name__ == "__main__":
   main()