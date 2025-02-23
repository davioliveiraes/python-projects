tabela_brasileirao_2024 = (
    "Botafogo FR RJ",
    "Palmeiras SP",
    "Flamengo",
    "Fortaleza CE",
    "Internacional RS",
    "São Paulo FC SP",
    "Corinthians SP",
    "Cruzeiro",
    "Vasco Gama",
    "EC Vitória BA",
    "Atletico Mineiro MG",
    "Fluminense RJ",
    "Gremio",
    "EC Juventude RS",
    "Red Bull Bragantino SP",
    "CA Paranaense PR",
    "Criciúma",
    "AC Goianiense GO",
    "Cuiabá Esporte Clube MT",
)

print("==" * 40)
print(f"Os 5 primeiros colocados são: {tabela_brasileirao_2024[0:5]}")
print("==" * 40)
print(f"Os últimos 4 colocados são: {tabela_brasileirao_2024[-4:]}")
print("==" * 40)
print(f"A tabela em ordem alfabética vai ficar: {sorted(tabela_brasileirao_2024)}")
print("==" * 40)
print(f"A posição que o time do Corinthians está é a: {tabela_brasileirao_2024.index('Corinthians SP')+1}ª posição")
print("==" * 40)
print(f"E a posição que o time do Fortaleza está é a: {tabela_brasileirao_2024.index('Fortaleza CE')+1}ª Posição")
print("==" * 40)

