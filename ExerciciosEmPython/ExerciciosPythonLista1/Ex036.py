# iniciante
hora_atividade_mes = int(input("Digite a quantidade de horas de atividade que teve por mês: "))

pontos = 0
if hora_atividade_mes < 10:
   pontos = hora_atividade_mes * 2
elif 10 <= hora_atividade_mes < 20:
   pontos = hora_atividade_mes * 5
elif hora_atividade_mes >= 20:
   pontos = hora_atividade_mes * 10
else:
   print(f"Entrada Inválida.")

dinheiro_ganho = pontos * 0.05
print(f"Quantidade de pontos: {pontos} pontos - Dinheiro ganho: R${dinheiro_ganho:,.2f}")

# Avançado
def calcular_pontos(horas: int) -> int:
   if horas < 0:
      raise ValueError("Horas não podem ser negativas.")
   elif horas < 10:
      return horas * 2
   elif horas < 20:
      return horas * 5
   else:
      return horas * 10

def calcular_dinheiro(pontos: int) -> float:
   return pontos * 0.05

def exibir_resultado(horas: int, pontos: int, dinheiro: float) -> None:
   print("\nResumo da Atividade Física: ")
   print(f"Horas de atividade no mês: {horas}h")
   print(f"Total de pontos acumulados: {pontos} pontos")
   print(f"Dinheiro ganho: R${dinheiro:,.2f}")

def main():
   try:
      horas = int(input("Digite a quantidade de horas de atividade que teve por mês: "))
      pontos = calcular_pontos(horas)
      dinheiro = calcular_dinheiro(pontos)
      exibir_resultado(horas, pontos, dinheiro)
   except ValueError as e:
      print(f"Erro: {e}")

if __name__ == "__main__":
   main()
