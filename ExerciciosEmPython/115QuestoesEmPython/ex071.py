print("==" * 30)
print(f"{"BEM VINDO AO BANCO KONOHA":^40}")
print("==" * 30)

dinheiro_sacar = int(input("Por favor digite quanto deseja sacar: R$"))
total = dinheiro_sacar
cedula = 100
total_cedula = 0
print("==" * 30)

while True:
   if total >= cedula:
      total -= cedula
      total_cedula += 1
   else:
      if total_cedula > 0:
         print(f"Vai sair {total_cedula} cédulas de R${cedula:,.2f}")
      if cedula == 100:
         cedula = 50
      elif cedula == 50:
         cedula = 20
      elif cedula == 20:
         cedula = 10
      elif cedula == 10:
         cedula = 5
      elif cedula == 5:
         cedula = 1
      total_cedula = 0
      if total == 0:
         break

print("==" * 30)
print("MUITO OBRIGADO, VOLTE SEMPRE AO BANCO DE KONOHA E TENHA UM ÓTIMO DIA!")