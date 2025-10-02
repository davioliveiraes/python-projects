preco_produto = float(input("Digite o preço do produto: R$"))
desconto = int(input("Digite em percentual o seu desconto(não precisa colocar a %): "))
preco_descontado = preco_produto - (preco_produto * (desconto/100))
print(f"O preço do produto com desconto vai ficar por: R${preco_descontado:,.2f}")