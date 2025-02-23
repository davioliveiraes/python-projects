numero = int(input("Digite um número inteiro: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f"A unidade do número é: {u}")
print(f"A dezena do número é: {d}")
print(f"A centana do número: {c}")
print(f"O milhar do número: {m}")

print("========================================================")

# Trabalhando com a forma string - Texto
numero = str(input("Digite um número inteiro: "))
print(f"A unidade do número: {numero[3]}")
print(f"A dezena do número: {numero[2]}")
print(f"A centena do número: {numero[1]}")
print(f"O milhar do número: {numero[0]}")

