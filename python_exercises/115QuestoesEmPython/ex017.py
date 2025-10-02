co = float(input("Digite o comprimento de cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f"Para ser um triângulo retângulo a hipotenusa tem quer ser igual a: {hi:.2f}")

print("=============================================================================")

import math
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
hi = math.hypot(co, ca)
print(f"Para ser um triângulo retângulo a hipotenusa tem que ser igual a: {hi:.2f}")

print("=============================================================================")

from math import hypot
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
hi = hypot(co, ca)
print(f"Para ser um triângulo retângulo a hipotenusa tem quer ser igual a: {hi:.2f}")
