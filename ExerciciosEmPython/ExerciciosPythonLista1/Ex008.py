distancia_metros = float(input("Digite uma distância em metros(m): "))

km = distancia_metros / 1000
hm = distancia_metros / 100
dam = distancia_metros / 10
dm = distancia_metros * 10
cm = distancia_metros * 100
mm = distancia_metros * 1000

print(f"A distância de {distancia_metros:.1f}: corresponde a: ")

print(f"KM: {km:.5f}")
print(f"HM: {hm:.4f}")
print(f"DAM: {dam:.3f}")
print(f"DM: {dm:.1f}")
print(f"CM: {cm:.1f}")
print(f"MM: {mm:.1f}")
