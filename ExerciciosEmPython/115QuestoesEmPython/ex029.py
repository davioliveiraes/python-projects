vel_carro = float(input("Digite a velocidade do carro(Km/h): "))
multa = (vel_carro - 80.0) * 7
if vel_carro > 80.0:
   print(f"Você ultrapassou a velocidade permitada. Foi multado com R${multa:.2f}")
else:
   print("Você está dentro da velocidade permitida.")
print("Tenha um bom dia e dirija com cuidado.")