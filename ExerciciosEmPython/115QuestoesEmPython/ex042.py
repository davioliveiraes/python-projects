seg1 = float(input("Digite o segmento 1: "))
seg2 = float(input("Digite o segmento 2: "))
seg3 = float(input("Digite o segmento 3: "))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
   print("Forma um triângulo!")

   if seg1 == seg2 == seg3:
      print("É do tipo EQUILÁTERO!")
   elif seg1 != seg2 == seg3 or seg2 != seg1 == seg3 or seg3 != seg1 == seg2:
      print("É do tipo ISÓSCELES!")
   elif seg1 != seg2 != seg3:
      print("É do tipo ESCALENO!")
else:
   print("NÃO DA PRA FORMA UM TRIÂNGULO.")
