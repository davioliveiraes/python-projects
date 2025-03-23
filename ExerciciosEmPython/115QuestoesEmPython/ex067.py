i = 0
deseja_continuar = "S"

while deseja_continuar in "Ss":
   num = int(input("Quer ver a tabuada de qual número: "))

   if num < 0:
      print("==" * 15)
      print("Número negativo não é permitido.")
      print("==" * 15)
      break
   print("                TABUADA                ")
   for i in range(0, 11):
      print(f"{num} X {i} = {num * i} | ", end="")
   print("\n", "==" * 86)

   deseja_continuar = str(input("Deseja continuar[S/N]: ")).upper().strip()[0]

print("PROGRAMA FINALIZADO.")