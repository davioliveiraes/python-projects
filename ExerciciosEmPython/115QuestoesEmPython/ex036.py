valor_casa = float(input("Qual é o valor da casa: R$"))
salario_comprador = float(input("Qual é o salário do comprador: R$"))
anos_pagar = int(input("Em quantos anos vai pagar: "))

anos_em_meses = anos_pagar * 12
presta_mensal = valor_casa / anos_em_meses
valor_limite = salario_comprador * 0.30

print(f"MEDIANTE O VALOR DA CASA DE R${valor_casa:,.2f} E O FINANCIAMENTO DE {anos_em_meses} PRESTAÇÕES MENSAIS VAI FICAR DE R${presta_mensal:,.2f} E O EMPRÉSTIMO VAI SER: ")
if presta_mensal > valor_limite:
   print("NEGADO!")
else:
   print("LIBERADO!")