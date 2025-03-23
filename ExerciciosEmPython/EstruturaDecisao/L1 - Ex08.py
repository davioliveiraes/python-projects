preco_produto1 = float(input("Digite o preço do primeiro produto: R$"))
preco_produto2 = float(input("Digite o preço do segundo produto: R$"))
preco_produto3 = float(input("Digite o preço do terceiro produto: R$"))

menor_preco = preco_produto1

if preco_produto2 < menor_preco:
    menor_preco = preco_produto2
if preco_produto3 < menor_preco:
    menor_preco = preco_produto3

print(f"O produto que deve comprar é o que custa: R${menor_preco:,.2f}")

precos_produtos = (preco_produto1, preco_produto2, preco_produto3)
print(f"O produto que deve comprar é o que custa: R${min(precos_produtos):,.2f}")
