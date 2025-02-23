def dia_da_semana(numero_dia):
   dias_por_extenso = ['DOMING', 'SEGUNDA-FEIRA', 'TERÇA-FEIRA', 'QUARTA-FEIRA', 'QUINTA-FEIRA', 'SEXTA-FEIRA', 'SÁBADO']

   try:
      dia = dias_por_extenso[numero_dia - 1]
   except IndexError:
      dia = "Valor Inválido"
   return dia

def main():
   while True:
      try:
         numero_dia = int(input("Digite um número de 1 à 7: "))
         if 1 <= numero_dia <= 7:
            break
         else:
            print("Número inválido, digite um número de 1 à 7!")
      except ValueError:
         print("Entrada inválida, digite um número inteiro(1à7)!")

   dia = dia_da_semana(numero_dia)
   print(f"O dia da semana correspondente ao número: {numero_dia} é: {dia}")

if __name__ == '__main__':
   main()