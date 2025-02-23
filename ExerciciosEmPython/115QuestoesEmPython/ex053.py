texto = str(input("Digite um texto: ")).strip().upper()
palavras = texto.split()
junto = "".join(palavras)
inverso = ""

for letras in range(len(junto)-1, -1, -1):
   inverso += junto[letras]
print("O invetso do texto")