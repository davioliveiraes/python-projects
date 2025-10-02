from random import randint
from time import sleep
lista = list()
jogos = list()
print("==" * 30)
print(f"{"SORTEIO DE NÚMEROS DA MEGA SENA":^57}")
quant = int(input("Quantos jogos deseja sortear: "))
total_jogos = 1
while total_jogos <= quant:
   count = 0
   while True:
      num = randint(1, 60)
      if num not in lista:
         lista.append(num)
         count += 1
      if count >= 6:
         break
   lista.sort()
   jogos.append(lista[:])
   lista.clear()
   total_jogos += 1
print("==" * 3, f"< SORTEANDO {quant} JOGOS >", "==" * 3)
for i, j in enumerate(jogos):
   print(f"Jogos {i+1}: {j}")
   sleep(1)
print("==" * 3, f" < BOA SORTE > ", "==" * 3)