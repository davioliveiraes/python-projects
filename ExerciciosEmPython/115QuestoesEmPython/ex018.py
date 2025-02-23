import math
angulo = float(input("Digite um ângulo: "))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f"O seno do ângulo de {angulo}º é de: {sen:.2f}")
print(f"O cosseno do ângulo de {angulo}º é de: {cos:.2f}")
print(f"A tangente do ângulo de {angulo}º é de: {tan:.2f}")

print("=================================================================")

from math import radians, sin, cos, tan
angulo = float(input("Digite o ângulo: "))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))

print(f"O seno do ângulo de {angulo}º é de: {sen:.2f}")
print(f"O cosseno do ângulo de {angulo}º é de: {cos:.2f}")
print(f"A tangente do ângulo de {angulo}º é de: {tan:.2f}")