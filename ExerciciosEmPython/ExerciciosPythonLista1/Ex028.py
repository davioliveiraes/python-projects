largura_terreno = float(input("Largura do terreno (m): "))
comprimento_terreno = float(input("Comprimento do terreno (m): "))

area = largura_terreno * comprimento_terreno

try:
   if area < 100:
      print(f"Área do terreno: {area:.2f} m² - TERRENO POPULAR")
   if area >= 100 and area < 500:
      print(f"Área do terreno: {area:.2f} m² - TERRENO MASTER")
   if area >= 500:
      print(f"Área do terreno: {area:.2f} m² - TERRENO VIP")
except ValueError as e:
   print(f"Erro: {e}")
