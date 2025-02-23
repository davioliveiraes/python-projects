contagem_extenso = ('Zero', 'Um', 'dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
   numero = int(input("Digite um número entre 0 a 20: "))
   if 0 <= numero <= 20:
      print(f"O número que você digitou foi {numero} e ele por extenso é {contagem_extenso[numero]}")
   else:
      print("Número não atuorizado, tente novamente...")
   
   deseja_continuar = ' '
   while deseja_continuar not in 'SN':
      deseja_continuar = str(input("Você deseja continuar[S/N]: ")).upper().strip()[0]
   if deseja_continuar == "N":
      break

print("PROGRAMA FINALIZADO, VOLTE SEMPRE!")
