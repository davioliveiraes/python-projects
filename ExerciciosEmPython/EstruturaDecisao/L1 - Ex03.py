estadoCivil = str(input("Digite o seu estado civil(C - Casado; S - Solteiro; D - Divorciado; V - Viúvo; O - Outros): "))
if estadoCivil in "Cc":
    print("REGISTRADO - CASADO")
elif estadoCivil in "Ss":
    print("REGISTRADO - SOLTEIRO")
elif estadoCivil in "Dd":
    print("REGISTRADO - DIVORCIADO")
elif estadoCivil in "Vv":
    print("REGISTRADO - VIÚVO")
elif estadoCivil in "Oo":
    print("REGISTRADO - OUTROS")
else:
    print("ERRO, PREENCHA AS INFORMAÇÕES CORRETAMENTE E TENTE NOVAMENTE...")
