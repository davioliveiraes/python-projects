def investigar_crime():
   nome_investigado = str(input("Digite o seu nome: "))
   p1 = str(input("Telefonou para vitima[S/N]? ")).upper()
   p2 = str(input("Esteve com a vitima[S/N]? ")).upper()
   p3 = str(input("Mora perto da vítima[S/N]? ")).upper()
   p4 = str(input("Devia para a vítima[S/N]? ")).upper()
   p5 = str(input("Já trabalhou com a vítima[S/N]? ")).upper()

   cont_positivo = 0
   perguntas = [p1, p2, p3, p4, p5]
   for pergunta in perguntas:
      if pergunta == 'S':
         cont_positivo += 1

   if cont_positivo == 2:
      print(f"{nome_investigado} - SUSPEITA")
   elif cont_positivo == 3 and cont_positivo == 4:
      print(f"{nome_investigado} - CÚMPLICE")
   elif cont_positivo == 5:
      print(f"{nome_investigado} - ASSASSINO")
   else:
      print(f"{nome_investigado} - INOCENTE")

investigar_crime()

