def classificar_participacao():
   perguntas = [
      "Telefonou para a vítima?",
      "Esteve no local do crime?",
      "Mora perto da vítima?",
      "Devia para a vítima?",
      "Já trabalhou com a vítima?" 
   ]

   respostas_positivas = 0
   for pergunta in perguntas:
      resposta = input(pergunta + "(sim/não): ").strip().lower()
      if resposta == "sim":
         respostas_positivas += 1
   if respostas_positivas == 5:
      classificao = "ASSASSINO"
   elif 3 <= respostas_positivas <= 4:
      classificao = "CÚMPLICE"
   elif respostas_positivas == 2:
      classificao = "SUSPEITA"
   else:
      classificao = "INOCENTE"
   
   print(f"Classificação: {classificao}")

if __name__ == "__main__":
   classificar_participacao()