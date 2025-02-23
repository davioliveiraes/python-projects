preco_produto = float(input("Digite o preço do produto: R$"))
preco_promo_5_desconto = preco_produto - (preco_produto *  0.05)
print(f"\nO produto que custava R${preco_produto:.2f}, na promoção com desconto de 5% vai custar R${preco_promo_5_desconto:.2f}")
