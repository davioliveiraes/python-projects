expressao = str(input("Digite uma expressão númerica: "))
pilha = []

for simb in expressao:
   if simb == '(':
      pilha.append('(')
   elif simb == ')':
      if len(pilha) > 0:
         pilha.pop()
      else:
         pilha.append(')')

if len(pilha) == 0:
   print("A expressão está válida!")
else:
   print("A expressão está inválida!")