print("==" * 20)
print("     PROGRESSÃO ARITMÉTICA    ")
print("==" * 20)

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
qtde_termos = int(input("Digite a quantidade de termos que quer mostrar: "))

termo = primeiro_termo
count = 1
total_termos = 0
mais_termos = qtde_termos

while mais_termos != 0:
   total_termos += mais_termos
   while count <= total_termos:
      print(f"{termo} -> ", end="")
      termo += razao
      count += 1
   print("PAUSA")
   mais_termos = int(input("Quantos termos você quer a mais[Digite 0 para encerrar a progressão]: "))

print("==" * 20)
print(f"Progressão Aritmética finalizada, com {qtde_termos} termos!")
print("==" * 20)
