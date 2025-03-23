nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if 7.0 <= media <= 10.0:
   print(f"SUA MÉDIA É {media:.2f} E VOCÊ ESTÁ APROVADO.")
elif 5.0 <= media <= 6.9:
   print(f"SUA MÉDIA É {media:.2f} E VOCÊ ESTÁ DE RECUPERAÇÃO.")
elif media < 4.9:
   print(f"SUA MÉDIA É {media:.2f} E VOCÊ ESTÁ REPROVADO.")
