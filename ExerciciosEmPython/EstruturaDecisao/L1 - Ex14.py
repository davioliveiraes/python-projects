def main():
   nota_parcial_1 = float(input("Digite a primeira nota 1: "))
   nota_parcial_2 = float(input("Digite a segunda nota 2: "))
   media_parcial = (nota_parcial_1 + nota_parcial_2) / 2
   print(f"A média parcial é: {media_parcial}")

   if 9.0 <= media_parcial <= 10.0:
      print("Conceito: A")
   elif 7.5 <= media_parcial < 9.0:
      print("Conceito: B")
   elif 6.0 <= media_parcial < 7.5:
      print("Conceito: C")
   elif 4.0 <= media_parcial < 6.0:
      print("Conceito: D")
   elif 0 <= media_parcial <= 4.0:
      print("Conceito: E")
   else:
      print("Valores Inválidos!")
 
if __name__ == "__main__":
   main()
