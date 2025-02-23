turno_estudo = str(input("Digite em qual turno você estuda(M - Matutino; V-Vespertino; N-Noturno): ")).lower()

if turno_estudo == "m":
    print("Bom dia!")
elif turno_estudo == "v":
    print("Boa tarde!")
elif turno_estudo == "n":
    print("Boa noite!")
else:
    print("Valor Inválido!")
