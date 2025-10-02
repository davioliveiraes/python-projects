def validar_mensagem(mensagem):
   while True:
      try:
         valor = int(input(mensagem))
         if valor < 0:
            print("Por favor digite um valor inteiro positivo.")
         else:
            return valor
      except ValueError:
         print("Entrada invália. Por favor, insira um número inteiro positivo.")

def calcular_dias_perdidos(cigarros_por_dia, anos_fumando):
   minutos_perdidos_por_cigarro = 10
   minutos_por_dia = 1440

   total_cigarros = cigarros_por_dia * 365 * anos_fumando
   total_minutos_perdidos = total_cigarros * 10
   dias_perdidos = total_minutos_perdidos / minutos_por_dia

   return dias_perdidos

def main():
   print("Calculando a Redução de Tempo de Vida de um Fumante")
   print("---------------------------------------------------")

   cigarros_por_dia = int(input("Digite a quantidade de cigarros por dia: "))
   anos_fumando = validar_mensagem("Digite a quantos anos você fuma: ")
   dias_perdidos = calcular_dias_perdidos(cigarros_por_dia, anos_fumando)

   print("\nResultado: ")
   print(f"Você tem aproximadamente {dias_perdidos:.2f} dias de vida.")
   
   if dias_perdidos > 365:
      anos_perdidos = dias_perdidos / 365
      print(f"Isso equivale aproximadamente {anos_perdidos:.2f} anos de vida restante.")
   else:
      print("Pense em parar de fumar para evitar mais perdas.")

if __name__ == "__main__":
   main()