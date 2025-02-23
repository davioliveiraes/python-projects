def area(largura, comprimento):
   area_terreno = largura * comprimento
   return area_terreno

largura_terreno = float(input("Digite a largura do terreno(M): "))
comprimento_terreno = float(input("Digite o comprimento do terreno(M): "))
print("    >>> CONTROLE DE TERRENOS <<<   ")
print(f"O terreno {largura_terreno}m X {comprimento_terreno}m tem uma área de {area(largura_terreno, comprimento_terreno):.2f}m²")
print("   <<< PROGRAMA ENCERRADO >>>  ")
