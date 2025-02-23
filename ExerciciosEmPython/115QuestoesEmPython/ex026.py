frase = str(input("Digite uma frase: ")).upper().strip()
print(f"A letra 'A' aparece {frase.count('A')}")
print(f"A primeira letra A apareceu na posição: {frase.find('A')+1}.")
print(f"A úlima letra A apareceu na posição: {frase.rfind('A')+1}")