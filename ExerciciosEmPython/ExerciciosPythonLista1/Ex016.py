qtde_cigarros_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
qtde_anos_fumando = int(input("Digite a quantidade de anos fumando: "))

minutos_perdidos_por_cigarro = 10

total_cigarros = qtde_cigarros_dia * 365 * qtde_anos_fumando

total_minutos_perdidos = total_cigarros * minutos_perdidos_por_cigarro

tempo_restanta_vida_dias = total_minutos_perdidos / 1440

print(f"O tempo de vida restante é de aproximadamente de: {tempo_restanta_vida_dias:.1f} dias")
