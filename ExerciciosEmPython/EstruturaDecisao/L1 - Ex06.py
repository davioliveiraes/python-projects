orcEmpresa1 = float(input("Digite o orçamento da empresa 1: R$"))
orcEmpresa2 = float(input("Digite o orçamento da empresa 2: R$"))
orcEmpresa3 = float(input("Digite o orçamento da empresa 3: R$"))

if orcEmpresa1 > orcEmpresa2 and orcEmpresa1 > orcEmpresa3:
    print(f"Orçamento da empresa 1 é maior - R${orcEmpresa1}")
elif orcEmpresa2 > orcEmpresa1 and orcEmpresa2 > orcEmpresa3:
    print(f"Orçamento da empresa 2 é maior - R${orcEmpresa2}")
elif orcEmpresa3 > orcEmpresa1 and orcEmpresa3 > orcEmpresa2:
    print(f"Orçamento da empresa 3 é maior - R${orcEmpresa3}")
else:
    print("ERRO, PREENCHA AS INFORMAÇÕES CORRETAMENTE E TENTE NOVAMENTE...")
