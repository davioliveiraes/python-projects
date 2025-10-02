nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota_1 + nota_2) / 2
try:
   if media < 5:
      print(f"Média: {media:.2f} - REPROVADO")
   elif media >= 5 and media < 7:
      print(f"Média: {media:.2f} - RECUPERAÇÃO")
   elif media >= 7:
      print(f"Média: {media:.2f} - APROVADO")
except ValueError as e:
   print(f"Erro: {e}")
   