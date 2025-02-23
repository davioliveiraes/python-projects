num = int(input("Digite um número inteiro: "))
print('''

   ESCOLHA UMA BASE PARA CONVERSÃO:
   [1] - CONVERTE PARA BINÁRIO
   [2] - CONVERTE PARA OCTAL 
   [3] - CONVERTE PARA HEXADECIMAL

''')

opcao = int(input("Digite sua opção: "))
if opcao == 1:
   print(f"O {num} em binário é: {bin(num)[2:]}")
elif opcao == 2:
   print(f"O {num} em octal é: {oct(num)[2:]}")
elif opcao == 3:
   print(f"O {num} em hexadecimal é: {hex(num)[2:]}")
else:
   print("Opção inválida. Tente novamente!")