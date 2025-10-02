peso = float(input("Digite o peso da pessoa(KG): "))
altura = float(input("Digite a altura da pessoa(M): "))

imc = peso / (altura ** 2)

if imc < 18.5:
   print(f"IMC: {imc:.2f} - ABAIXO DO PESO")
elif 18.5 <= imc < 25:
   print(f"IMC: {imc:.2f} - PESO IDEAL")
elif 25 <= imc < 30:
   print(f"IMC: {imc:.2f} - SOBREPESO")
elif 30 <= imc < 40:
   print(f"IMC: {imc:2f} - OBESIDADE")
elif imc >= 40:
   print(f"IMC: {imc:.2f} - OBESIDADE MORBIDA")
else:
   print("VALOR INVÁLIDO")

