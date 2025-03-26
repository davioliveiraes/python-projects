def tipo_triangulo(seg1, seg2, seg3):
   if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
      if seg1 == seg2 == seg3:
         return 'Equilátero'
      elif seg1 == seg2 or seg1 == seg3 or seg2 == seg3:
         return 'Isósceles'
      elif seg1 != seg2 != seg3:
         return 'Escaleno'
   else:
      return 'Não é um triângulo'

seg1 = float(input("Digite o valor do primeiro segmento: "))
seg2 = float(input("Digite o valor do segundo segmento: "))
seg3 = float(input("Digite o valor do terceiro segmento: "))

print(f"O triângulo é do tipo: {tipo_triangulo(seg1, seg2, seg3)}")
