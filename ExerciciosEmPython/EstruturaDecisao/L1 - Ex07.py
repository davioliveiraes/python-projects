orcamento_1 = float(input("Digite o primeiro orçamento: R$"))
orcamento_2 = float(input("Digite o segundo orçamento: R$"))
orcamento_3 = float(input("Digite o terceiro orçamento: R$"))

maior_orcamento = orcamento_1
menor_orcamento = orcamento_1

if orcamento_2 > maior_orcamento:
    maior_orcamento = orcamento_2
if orcamento_2 < menor_orcamento:
    menor_orcamento = orcamento_2

if orcamento_3 > maior_orcamento:
    maior_orcamento = orcamento_3
if orcamento_3 < menor_orcamento:
    menor_orcamento = orcamento_3

print(f"O maior orçamento: R${maior_orcamento:,.2f}")
print(f"O menor orçamento: R${menor_orcamento:,.2f}")

print("==" * 30)

# Utilizando métodos feitos em Python
orcamentos = (orcamento_1, orcamento_2, orcamento_3)
print(f"O maior orçamento: R${max(orcamentos):,.2f}")
print(f"O menor orçamento: R${min(orcamentos):,.2f}")
