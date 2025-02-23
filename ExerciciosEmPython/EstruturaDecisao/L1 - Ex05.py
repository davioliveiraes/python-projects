nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 7:
    print(f"MÉDIA: {media} - APROVADO!")
elif media < 7:
    print(f"MÉDIA: {media} - REPROVADO!")
elif media == 10:
    print(f"MÉDIA: {media} - APROVADO COM DISTINÇÃO!")
else:
    print("ERRO, PREENCHA AS INFORMAÇÕES CORRETAMENTE E TENTE NOVAMENTE...")
