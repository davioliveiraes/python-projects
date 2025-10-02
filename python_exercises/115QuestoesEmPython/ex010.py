import requests

url = "https://api.exchangerate-api.com/v4/latest/BRL"
response = requests.get(url)
data = response.json()

dolar_cotacao = 1 / data["rates"]["USD"]
euro_cotacao = 1 / data["rates"]["EUR"]
libra_cotacao = 1 / data["rates"]["GBP"]

dinheiroReal = float(input("Digite o quanto você tem na carteira: R$ "))

dolar = dinheiroReal / dolar_cotacao
euro = dinheiroReal / euro_cotacao
libra = dinheiroReal / libra_cotacao

print(f"Com R${dinheiroReal:,.2f}, você pode comprar: ")
print(f" - {dolar:,.2f} dolares")
print(f" - {euro:,.2f} euros")
print(f" - {libra:,.2f} libras")
