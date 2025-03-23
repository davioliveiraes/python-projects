print("  PROGRESSÃO ARITMÉTICA  ")
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
qtde_termo = int(input("Digite a quantidade de termos que vai ser apresentados: "))

termo = primeiro_termo
count = 1

while count <= qtde_termo:
   print(f"{termo} -> ", end="")
   termo += razao
   count += 1
print("FIM")
