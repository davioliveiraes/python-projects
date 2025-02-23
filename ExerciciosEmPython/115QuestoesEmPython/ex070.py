print("==" * 20)
print(f"{"LOJA DE KONOHA":^40}")
print("==" * 20)

total_gasto = count = 0.0
qtda_produto_mais_1000 = 0
nome_produto_mais_barato = ' '

while True:
   descricao_produto = str(input("Digite a descrição do produto : "))
   preco_produto = float(input("Digite o preço do produto: "))

   total_gasto += preco_produto
   count += 1

   if preco_produto > 1000:
      qtde_produto_mais_1000 += 1
   if count == 1 or preco_produto < preco_produto_mais_barato:
      preco_produto_mais_barato = preco_produto
      nome_produto_mais_barato = descricao_produto
   
   deseja_continuar = ' '
   while deseja_continuar not in "SN":
      deseja_continuar = str(input("Você deseja continuar[S/N]: ")).upper().strip()[0]
   if deseja_continuar == "N":
      break

print("==" * 30)
print(f"O total gasto na compra foi de: R${total_gasto:,.2f}")
print(f"A quantidade de produto que custam mais de R$1.000,00 são: {qtda_produto_mais_1000}")
print(f"O nome do produto mais barato é: {nome_produto_mais_barato}")
print("==" * 30)