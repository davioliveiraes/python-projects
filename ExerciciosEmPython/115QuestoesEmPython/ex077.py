times_futebol = ('Corinthians', 'Fortaleza', 'Flamengo', 'Palmeitas', 'Vasco', 'Fluminense', 'Santos', 'Botafogo', 'Real Madrid', 'Manchester City', 'Ceará', 'São Paulo')

for palavras in times_futebol:
   print(f"\nNa palavra do time de futebol {palavras.upper()} temos: ", end='')
   for letras in palavras:
      if letras.lower() in 'aeiou':
         print(letras, end='')