class Funcionario:
   def __init__(self, nome, salario_atual, genero, anos_empresa):
      self.nome = nome
      self.salario_atual = salario_atual
      self.genero = genero.lower()
      self.anos_empresa = anos_empresa
   
   def calcular_novo_salario(self):
      percentual = self._obter_percentual_aumento()
      novo_salario = self.salario_atual * (1 + percentual / 100)
      return novo_salario
   
   def _obter_percentual_aumento(self):
      if self.genero == "f" or self.genero == 'feminino':
         if self.anos_empresa < 15:
            return 5
         elif 15 <= self.anos_empresa <= 20:
            return 12
         else:
            return 23
      elif self.genero == "m" or self.genero == 'masculino':
         if self.anos_empresa < 20:
            return 3
         elif 20 <= self.anos_empresa <= 30:
            return 13
         else:
            return 25
      else:
         raise ValueError("Genêro inválido. Use 'M' ou 'F'.")

def obter_float(mensagem):
   while True:
      try:
         return float(input(mensagem))
      except ValueError:
         print("Valor inválido. Digite um número.")

def obter_int(mensagem):
   while True:
      try:
         return int(input(mensagem))
      except ValueError:
         print("Valor inválido. Digite um número inteiro.")

def main ():
   print("=== Reajuste Salarial ===")
   nome = str(input("Nome do funcionário: "))
   salario = obter_float("Salário atual: R$")
   genero = input("Gênero [M/F]: ")
   anos = obter_int("Anos de empresa: ")

   funcionario = Funcionario(nome, salario, genero, anos)
   try:
      novo_salario = funcionario.calcular_novo_salario()
      print(f"\n{funcionario.nome} terá um novo salário de R${novo_salario:,.2f} ")
   except ValueError as e:
      print(f"ERRO: {e}")

if __name__ == "__main__":
   main()