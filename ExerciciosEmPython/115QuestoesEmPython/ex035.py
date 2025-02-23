seg1 = float(input("Digite o segmento 1: "))
seg2 = float(input("Digite o segmento 2: "))
seg3 = float(input("Digite o segmento 3: "))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
   print("Dá pra forma um triângulo.")
else:
   print("Não dá pra forma um triângulo.")