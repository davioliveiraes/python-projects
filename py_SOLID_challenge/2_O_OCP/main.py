from abc import ABC, abstractmethod
from typing import List, Dict
from datetime import datetime

# Interface Base(Abstração)
class Exam(ABC):
   """Interface base para todos os tipos exames"""

   def __init__(self, pacient: str, veterinarian: str, request_data: datetime = None): # type: ignore
      self.pacient = pacient
      self.veterinarian = veterinarian
      self.request_data = request_data or datetime.now()
      self.approved = False

   @abstractmethod
   def check_conditions(self) -> bool:
      "Cada tipo de exame implementa suas próprias condições de aprovação"
      pass

   @abstractmethod
   def get_type(self) -> str:
      """Retorna o tipo do exame"""
      pass

   def approve(self):
      """Marca o exame como aprovado"""
      self.approved = True
   
   def __str__(self) -> str:
      return f"{self.get_type()} - Paciente: {self.pacient}"

# Implementações Concretas de Exames
class BloodTest(Exam):
   """Exame de sangue com usas regras específicas"""

   def __init__(self, pacient: str, veterinarian: str, fasting_hours: int):
      super().__init__(pacient, veterinarian)
      self.fasting_hours = fasting_hours
   
   def check_conditions(self) -> bool:
      """Condições específicos para exame de sangue"""
      # Regra o animal deve está em jejum de pelo menos 8 horas
      if self.fasting_hours >= 8:
         print(f" Jejum adequado: {self.fasting_hours}h")
         return True
      else:
         print(f" Jejum insuficiente: {self.fasting_hours}h (mínimo: 8 horas)")
         return False

   def get_type(self) -> str:
      return "Exame de Sangue"

class XRayExam(Exam):
   """Exame no raio-x com suas regras específicas"""

   def __init__(self, pacient: str, veterinarian: str, body_area: str, sedation: bool):
      super().__init__(pacient, veterinarian)
      self.body_area = body_area
      self.sedation = sedation
   
   def check_conditions(self) -> bool:
      """Condições específicas para exame de raio-x"""
      # Regra: área sensíveis requerem sedação
      sensation_areas = ["coluna", "cranio", "abdomen"]

      if self.body_area.lower() in sensation_areas and not self.sedation:
         print(f"  Área {self.body_area} requer sedação")
         return False
      
      print(f"  Raio-X da área '{self.body_area}' pode ser realizado")
      return True
   
   def get_type(self) -> str:
      return "Exame de Raio-X"

class UltrasoundExam(Exam):
   """Exame de Ultrassom com suas regras específicas"""

   def __init__(self, pacient: str, veterinarian: str, full_bladder: bool, shaved_hair: bool):
      super().__init__(pacient, veterinarian)
      self.full_bladder = full_bladder
      self.shaved_hair = shaved_hair
   
   def check_conditions(self) -> bool:
      """Condições específicas para ultrassom"""
      conditions_ok = True

      if not self.full_bladder:
         print(" Bexiga precisa estar cheia")
         conditions_ok = False
      else:
         print(" Bexiga cheia")
      
      if not self.shaved_hair:
         print(" Pelo precisa ser raspado na região")
         conditions_ok = False
      else:
         print(" Pelo raspado")

      return conditions_ok
   
   def get_type(self) -> str:
      return "Exame de Ultrassom"

class UrineTest(Exam):
   """Exame de Urina com suas específicas"""

   def __init__(self, pacient: str, veterinarian: str, recent_sample: bool, volume_ml: int):
      super().__init__(pacient, veterinarian)
      self.recent_sample = recent_sample
      self.volume_ml = volume_ml

   def check_conditions(self) -> bool:
      """Condições específicas para exame de urina"""
      # Regra: amostra dever ser recente (< 2h) e ter volume mínimo de 5ml
      if not self.recent_sample:
         print(" Amostra não é recente (deve ter menos de 2h)")
         return False

      if self.volume_ml < 5:
         print(f" Volume insuficiente: {self.volume_ml}ml (mínimo: 5ml)")
         return False

      print(f" Amostra adequada: {self.volume_ml}ml")
      return True

   def get_type(self) -> str:
      return "Exame de Urina" 

class Echocardiogram(Exam):
   """Exame de ecocardiograma com suas regras específicas"""

   def __init__(self, pacient: str, veterinarian: str, calm_animal: bool, age_years: int):
      super().__init__(pacient, veterinarian)
      self.calm_animal = calm_animal
      self.age_years = age_years
   
   def check_conditions(self) -> bool:
      """Condições específicas para ecocardiagrama"""
      if not self.calm_animal:
         print(" Animal precisa estar calmo (considera sedação leve)")
         return False
      
      if self.age_years < 1:
         print(" Animal muito jovem, exame requer especialista")

      print(" Condições adequadas para ecocardiograma")
      return True

   def get_type(self) -> str:
      return "Ecocardiograma"
   
# Pode está implementando aqui um novo tipo de exame.

# Classe Aprovadora (Fechada Para Modificação)
class ApproveExam:
   """
   Classe responsávle por aprovar exames.
   FECHADA para modificação: não precisa ser alterada ao adicionar novo exames
   ABERTA para extensão: aceita qualquer tipo de exame que implemente
   """

   def __init__(self):
      self.approved_exams: List[Exam] = []
      self.failed_exams: List[Exam] = []
   
   def approve_exam_request(self, exam: Exam) -> bool:
      """
      Aprova um exame baseado em suas condições específicas.
      Não importa o tipo de exame, o método funciona para todos!
      """
      print(f"\n Analisando: {exam}")
      print(f"  Veterinário: {exam.veterinarian}")
      print(f"  Data: {exam.request_data.strftime('%d/%m/%y %H:%M')}")

      if exam.check_conditions():
         exam.approve()
         self.approved_exams.append(exam)
         print(f" {exam.get_type()} APROVADO!\n")
         return True
      else:
         self.failed_exams.append(exam)
         print(f"  {exam.get_type()} REPROVADOS!\n")
         return False
   
   def generate_report(self) -> Dict[str, int]:
      """Gera relatório de aprovações"""
      return {
         'Aprovados': len(self.approved_exams),
         'Reprovados': len(self.failed_exams),
         'Total': len(self.approved_exams) + len(self.failed_exams)
      }

# Exemplo de uso
def main():
   print("=" * 70)
   print("SISTEMA DE APROVAÇÃO DE EXAMES - CLÍNICA VETERINÁRIA")
   print("Demonstração do Princípio Aberto/Fechado (OCP)")
   print("=" * 70)

   approver = ApproveExam()

   # Criando diferentes tipos de exames
   exams = [
      BloodTest(
         pacient="Rex (Labrador)",
         veterinarian="Dr Oliveira",
         fasting_hours=10
      ),
   
      BloodTest(
         pacient="Mimi (Gata Persa)",
         veterinarian="Dr Lima",
         fasting_hours=5 # Insuficiente
      ),

      XRayExam(
         pacient="Bob (Bulldog)",
         veterinarian="Dr. Cavalcante",
         body_area="coluna",
         sedation=False # Faltou sedação!
      ),

      UltrasoundExam(
         pacient="Thor (Pasto Alemão)",
         veterinarian="Dra Alice",
         full_bladder=True,
         shaved_hair=True
      ),

      UrineTest(
         pacient="Mel (Beagle)",
         veterinarian="Dr. Costa",
         recent_sample=True,
         volume_ml=8
      ),

      Echocardiogram(
         pacient="Simba (Golden Retriever)",
         veterinarian="Dra Mara", 
         calm_animal=True,
         age_years=7
      )
   ]

   for exam in exams:
      approver.approve_exam_request(exam)
   
   print("=" * 70)
   print("RELATÓRIO FINAL")
   print("=" * 70)
   report = approver.generate_report()
   print(f"Exames aprovados: {report['Aprovados']}")
   print(f"Exames reprovados: {report['Reprovados']}")
   print(f"Total de exames: {report['Total']}")
   print("=" * 70)

   print("VANTAGEM DO OCP:")
   print(" Para adicionar um novo tipo de exame (ex: Tomografia),")
   print(" Basta cria um nova classe que herda 'Exam'.")
   print(" A classe 'ApproveExam' NÃO precisa ser modificado!")

if __name__ == "__main__":
   main()
