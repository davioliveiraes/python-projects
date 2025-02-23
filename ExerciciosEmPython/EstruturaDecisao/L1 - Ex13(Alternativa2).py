numero_dia = int(input("Digite o número do dia da semana(1à7): "))

dias_por_extenso = [
    "DOMINGO",
    "SEGUNDA-FEIRA",
    "TERÇA-FEIRA",
    "QUARTA-FEIRA",
    "QUINTA-FEIRA",
    "SEXTA-FEIRA",
    "SÁBADO"
]

if 1 <= numero_dia <= 7:
   dia_por_extenso = dias_por_extenso[numero_dia - 1]
   print(f"O dia por extenso correspondente a: {numero_dia} é: {dia_por_extenso}")
else:
   print("Valor inválido, digite um número inteiro 1 à 7!")
