altura = float(input("Digite a sua altura(M): "))
sexo = str(input("Digite o seu sexo[M/F]: ")).upper()[0]
if sexo == 'M':
    pesoIdeal = 72.7 * altura - 58
elif sexo == 'F':
    pesoIdeal = 62.1 * altura - 44.7
else:
    print("ERRO! Verifique se está tudo correto.")

print(f"O peso ideal da pessoa é {pesoIdeal:.2f}")
