distanciaM = float(input("Digite uma distância em metros (m): "))
km =  distanciaM / 1000
hm = distanciaM / 100
dam = distanciaM / 10
m = distanciaM
dm = distanciaM * 10
cm = distanciaM * 100
mm = distanciaM * 1000

print(f"A medida em quilômetros é: {km} KM")
print(f"A medida em hectômetros é: {hm} HM")
print(f"A medida em decâmetros é: {dam} DAM")
print(f"A medida em metros: {m} M")
print(f"A medida em decímetros é: {dm} DM")
print(f"A medida em centímetros é: {cm} CM")
print(f"A medida em milímetros é: {mm} MM")