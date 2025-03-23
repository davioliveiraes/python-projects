print("==" * 25)
print("          SEQUÊNCIA DE FIBONACCI          ")
print("==" * 25)

termos = int(input("Digite a quantidade de termos que deseja: "))
t1 = 0
t2 = 1

print("=="  * 15)
print(f"{t1} -> {t2}", end="")
count = 3

while count <= termos:
   t3 = t1 + t2
   print(f" -> {t3}", end="")
   t1 = t2
   t2 = t3
   count += 1
print(" -> FIM")
print("==" * 15)
