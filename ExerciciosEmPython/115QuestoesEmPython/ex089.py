from time import sleep
ficha_aluno = list()

while True:
   nome = str(input("Digite o nome do aluno: "))
   nota1 = float(input("Digite a primeira nota: "))
   nota2 = float(input("Digite a segunda nota: "))
   media = (nota1 + nota2) / 2

   ficha_aluno.append([nome, [nota1, nota2], media])

   resp = str(input("Deseja cadastrar mais um aluno[S/N]: "))
   if resp in "Nn":
      break

print("==" * 20)
print(f"{"ID.":<6}{"NOME:":<7}{"MÉDIA:":>8}")
for i, aluno in enumerate(ficha_aluno):
   print(f"{i:<6}{aluno[0]:<7}{aluno[2]:>8}")
print("==" * 20)
while True:
   opc = int(input("Digite o ID do aluno(a) que deseje ver a nota: "))
   if opc == 999:
      print("FINALIZANDO")
      sleep(1)
      break
   print(f"As notas do aluno {ficha_aluno[opc][0]} são: {ficha_aluno[opc][1]}")
print(" <<< VOLTE SEMPRE >>> ")
