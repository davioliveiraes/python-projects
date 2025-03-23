def verificar_ano_bissexto(ano):
   if ano % 4 == 0:
      if ano % 100 == 0:
         if ano % 400 == 0:
            return True
         else:
            return False
      else:
         return True
   else:
      return False

ano = int(input("Digite o ano: "))
if verificar_ano_bissexto(ano):
   print(f"O ano {ano} é bissexto!")
else:
   print(f"O ano {ano} não é bissexto!")