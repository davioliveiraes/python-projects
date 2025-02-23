import requests

def obter_taxa_cambio_dolar():
   url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

   response = requests.get(url)

   if response.status_code == 200:
      data = response.json()
      taxa_dolar = float(data["USDBRL"]['bid'])
      return taxa_dolar
   else:
      print("Erro ao obter taxa de câmbio de dólar.")

def converter_real_para_dolar(real, taxa_dolar):
   if taxa_dolar is not None:
      dolar = real / taxa_dolar
      return dolar
   else:
      return None

if __name__ == "__main__":
   real = float(input("Digite quanto você tem na carteira: R$"))
   taxa_dolar = obter_taxa_cambio_dolar()

   if taxa_dolar is not None:
      dolar = converter_real_para_dolar(real, taxa_dolar)
      print(f"\nCotação atual do dólar: R${taxa_dolar:.2f}")
      print(f"Você tem R${real:.2f}, que equivale a US${dolar:.2f}")
   else:
      print("Não foi possível realizar a conversão.")
