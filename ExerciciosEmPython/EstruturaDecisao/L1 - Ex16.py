nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
if 7 <= media < 10:
   print(f"APROVADO! SUA MÉDIA É: {media:.2f}")
elif media < 7:
   print(f"REPROVADO! SUA MÉDIA É: {media:.2f}")
elif media == 10:
   print(f"APROVADO COM DISTINÇÃO! SUA MÉDIA É: {media:.2f}")
else:
   print("VALORES INCORRETOS, TENTE NOVAMENTE.")
