# Pergunta: Escreva um programa que aceite uma sequência de números separados por vírgulas do console e gere uma lista e uma tupla que contenha todos os números. Suponha que a seguinte entrada seja fornecida ao programa: 34,67,55,33,12,98 Então, a saída deve ser: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

# Dicas: No caso de dados de entrada serem fornecidos à pergunta, deve-se presumir que seja uma entrada do console. O método tuple() pode converter lista em tupla

# Alternativa 1
values = input("Digite uma sequência de números separados por vírgulas: ")
lista_values = values.split(",")
tupla_values = tuple(lista_values)

print(f"Lista: {lista_values}")
print(f"Tupla: {tupla_values}")

print()

# Alternativa 2
def obter_sequencia():
   while True:
      try:
         entrada = input("Digite uma sequência de números seperados por vírgula: ").strip()

         if not entrada:
            raise ValueError("A entrada não pode ser vazia.")
         lista = [item.strip() for item in entrada.split(",")]
         
         if not all(item.isdigit() for item in lista):
            raise ValueError("A sequência só pode ser separados por vígulas.")
         tupla = tuple(lista)

         return lista, tupla
      
      except ValueError as e:
         print(f"Erro: {e}. Tente novamente.")

lista, tupla = obter_sequencia()
print(f"Lista: {lista}")
print(f"Tupla: {tupla}")
   
