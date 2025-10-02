from random import randint

# Alternativa

tupla_numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print(f"A tupla dos números gerados foi: {tupla_numeros}")
print(f"O menor número da tupla gerada é: {min(tupla_numeros)}")
print(f"O maior número da tupla gerada é: {max(tupla_numeros)}")

print("==" * 40)

# Alternativa 2

tupla_numeros_2 = tuple(randint(1, 100) for _ in range(5))
print(f"A tupla dos números gerados foi: {tupla_numeros_2}")
print(f"O menor número da tupla gerado é: {min(tupla_numeros_2)}")
print(f"O maior número da tupla gerado é: {max(tupla_numeros_2)}")
