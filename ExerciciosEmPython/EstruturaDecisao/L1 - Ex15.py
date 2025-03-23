def main():
   ano = int(input("Digite o número do ano: "))
   if ano % 400 == 0 or ano % 4 == 0 and not ano % 100 == 0:
      print("O ano é: BISSEXTO")
   else:
      print("O ano: NÃO É BISSEXTO")

if __name__ == "__main__":
   main()