# Personagem: classe mae
# Heroi: controlado pelo usuário
# Inimigo: adversário do usuário

from random import randint

class Personagem:
   def __init__(self, nome, vida, nivel):
      self.__nome = nome
      self.__vida = vida
      self.__nivel = nivel
   
   def get_nome(self):
      return self.__nome
   
   def get_vida(self):
      return self.__vida

   def get_nivel(self):
      return self.__nivel
   
   def exibir_detalhes(self):
      return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}\n"
   
   def receber_ataque(self, dano):
      self.__vida -= dano
      if self.__vida < 0:
         self.__vida = 0
      
   def ataque(self, alvo):
      dano = randint(self.get_nivel() * 2, self.get_nivel() * 4)
      alvo.receber_ataque(dano)
      print(f"{self.get_nome()} ataca {alvo.get_nome()} e causou {dano} de dano!")

class Heroi(Personagem):
   def __init__(self, nome, vida, nivel, habilidade):
      super().__init__(nome, vida, nivel)
      self.__habilidade = habilidade
   
   def get_habilidade(self):
      return self.__habilidade
   
   def exibir_detalhes(self):
      return f"{super().exibir_detalhes()}Habilidade: {self.get_habilidade()}\n"
   
   def ataque_especial(self, alvo):
      dano = randint(self.get_nivel() * 5, self.get_nivel() * 8)
      alvo.receber_ataque(dano)
      print(f"{self.get_nome()} usa habilidade especial em {alvo.get_nome()} e causou {dano} de dano!")

class Inimigo(Personagem):
   def __init__(self, nome, vida, nivel, tipo):
      super().__init__(nome, vida, nivel)
      self.__tipo = tipo
   
   def get_tipo(self):
      return self.__tipo

   def exibir_detalhes(self):
      return f"{super().exibir_detalhes()}Tipo: {self.get_tipo()}\n"
   
class Jogo:
   """Classe orquestradora do jogo"""

   def __init__(self) -> None:
      self.heroi = Heroi(nome="Batman", vida=100, nivel=5, habilidade="Ser rico")
      self.inimigo = Inimigo(nome="Coringa", vida=80, nivel=5, tipo="Palhaço")

   def iniciar_jogo(self):
      print("Iniciando o jogo...")
      while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
         print("\nDelhates dos personagens: ")
         print(self.heroi.exibir_detalhes())
         print(self.inimigo.exibir_detalhes())

         input("Pressione Enter para atacar o inimigo...")
         escolha = input("Escolha uma ação: 1 - Ataque normal, 2 - Habilidade Especial: ")

         if escolha == "1":
            self.heroi.ataque(self.inimigo)
         elif escolha == "2":
            self.heroi.ataque_especial(self.inimigo)
         else:
            print("ESCOLHA INVÁLIDA. Tente novamente.")

         if self.inimigo.get_vida() > 0:
            self.inimigo.ataque(self.heroi)

      if self.heroi.get_vida() <= 0:
         print("Você perdeu! O inimigo venceu.")
      else:
         print("Parabéns! Você venceu o inimigo.")
         

jogo = Jogo()
jogo.iniciar_jogo()
