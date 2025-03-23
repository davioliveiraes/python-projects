carteira_real = float(input("Digite quanto você tem na carteira: R$"))

carteira_real_em_dolar = carteira_real / 3.45
print(f"\nVocê tem R${carteira_real:.2f}, que equivale a US${carteira_real_em_dolar:.2f}")
