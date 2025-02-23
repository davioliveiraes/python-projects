print("            PROGRESSÃO ARITMÉTICA             ")
primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite o razão: "))
qtde_termo = int(input("Digite a quantidade de termis que vai ser apresentados: "))
termo = primeiro_termo + qtde_termo * razao

for count in range(primeiro_termo, termo, razao):
   print(f"{count}", end="->")
print("ACABOU")