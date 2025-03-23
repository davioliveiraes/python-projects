num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

opcao = 0
print("=========== MENU DE OPÇÕES ===========")
while opcao != 5:
   print('''
   
   [1] SOMAR
   [2] MULTIPLICAR
   [3] MAIOR
   [4] NOVOS NÚMEROS
   [5] SAIR DO PROGRAMA
   
   ''')
   opcao = int(input("Digite a sua opção: "))

   if opcao == 1:
      soma = num1 + num2
      print(f"A soma entre {num1} e {num2} é igual: {soma}")
   elif opcao == 2:
      multi = num1 * num2
      print(f"A multiplicação entre {num1} e {num2} é igual a: {multi}")
   elif opcao == 3:
      if num1 > num2:
         print(f"O maior número entre {num1} e {num2} é: {num1}")
      else:
         print(f"O maior número entre {num1} e {num2} é: {num2}")
   elif opcao == 4:
      print("Por favor, digite os novos números: ")
      num1 = int(input("Digite o primeiro número: "))
      num2 = int(input("Digite o segundo número: "))
   elif opcao == 5:
      print("Finalizando...")
   else:
      print("Opção inválida! Tente novamente...")
print("Fim do programa, volte sempre!")