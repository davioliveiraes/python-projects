segm_1 = int(input("Digite o primeiro segmento(valor inteiro): "))
segm_2 = int(input("Digite o segundo segmento(valor inteiro): "))
segm_3 = int(input("Digite o terceiro segmento(valor inteiro): "))

if segm_1 < segm_2 + segm_3 and segm_2 < segm_1 + segm_3 and segm_3 < segm_1 + segm_2:
   print("FORMA UM TRIÂNGULO!")
else:
   print("NÃO FORMA UM TRIÂNGULO!")
