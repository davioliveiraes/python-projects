peso = float(input("Qual é o seu peso[KG]: "))
altura = float(input("Qual é a sua altura[M]: "))

imc = peso / (altura ** 2)

print(f"O seu índice de massa corporal é: {imc:.2f} - RESULTADO É: ")
if imc <= 18.5:
   print("ABAIXO DO PESO!")
elif 18.5 < imc <= 30:
   print("PESO IDEAL!")
elif 30 < imc <= 40:
   print("SOBREPESO!")
elif imc > 40:
   print("OBSIDADE MÓRBIDA!")
else:
   print("NÃO SE ENCAIXA EM NENHUM CATEGORIA DE IMC!")

