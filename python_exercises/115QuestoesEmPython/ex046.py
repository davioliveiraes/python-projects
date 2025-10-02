from emoji import emojize
from time import sleep
print("CONTAGEM REGRESSIVA PARA ESTOURO: ")
for count in range(10, -1, -1):
   print(count)
   sleep(1)
print(emojize("🎇 🎆" * 30))
