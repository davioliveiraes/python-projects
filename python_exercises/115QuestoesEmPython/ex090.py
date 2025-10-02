alunos = []

while True:
   aluno = dict()
   aluno['Nome'] = str(input("Digite o nome do aluno: "))
   aluno['Media'] = float(input("Digite a média do aluno: "))

   if 7 <= aluno['Media'] <= 10:
      aluno['Situacao'] = "Aprovado"
   elif 4 <= aluno['Media'] < 7:
      aluno['Situacao'] = "Recuperação"
   elif aluno['Media'] < 4:
      aluno['Situacao'] = "Reprovado"
   else:
      print("Verifique o seus dados!")
   
   alunos.append(aluno)

   resp = str(input("Deseja cadastrar um novo aluno[S/N]: "))
   if resp in "Nn":
      break

print("==" * 20)
print("   <<< DADOS DOS ALUNOS >>>  ")
for aluno in alunos:
   for i, dados_aluno in aluno.items():
      print(f"{i}: {dados_aluno}")
   print("==" * 20)
print("==" * 20)
