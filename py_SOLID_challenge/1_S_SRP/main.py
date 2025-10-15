from abc import ABC, abstractmethod
from typing import List, Dict, Any
from datetime import datetime
import json

# Models
class Task:
   """Modelo de dados para uma tarefa"""
   def __init__(self, id: int, title: str, description: str, status: str):
      self.id = id
      self.title = title
      self.description = description
      self.status = status
      self.created_at = datetime.now()
      self.updated_at = datetime.now()
   
   def to_dict(self) -> Dict[str, Any]:
      return {
         'id': self.id,
         'title': self.title,
         'description': self.description,
         'status': self.status,
         'created_at': self.created_at.isoformat(),
         'updated_at': self.updated_at.isoformat()
      }

# Responsabilidade: Conexão com API
class APIConnector:
   """Responsável apenas por gerenciar a conexão com a API"""
   def __init__(self, base_url: str, api_key: str):
      self.base_url = base_url
      self.api_key = api_key
      self.session = None
   
   def connect(self):
      """Estabale conexão com a API"""
      print(f"Conectando à API: {self.base_url}")
      self.session = {"connected": True, "api_key": self.api_key}
      return True
   
   def disconnect(self):
      """Encerra conexão com a API"""
      print("Desconectando da API")
      self.session = None
   
   def is_connected(self) -> bool:
      return self.session is not None

# Responsabilidade: Operações de Tarefas
class TaskRepository:
   """Responsável apenas por operações CRUD de tarefas"""
   def __init__(self, api_connector: APIConnector):
      self.api_connector = api_connector
      self.tasks: Dict[int, Task] = {}
      self.next_id = 1
   
   def create_task(self, title: str, description: str, status: str = 'pending') -> Task:
      """Cria uma nova tarefa"""
      if not self.api_connector.is_connected():
         raise ConnectionError("API não está conectada")

      task = Task(self.next_id, title, description, status)
      self.tasks[task.id] = task
      self.next_id = 1
      print(f"Tarefa '{title}' criada com ID: {task.id}")
      return task
   
   def update_task(self, task_id: int, **kwargs) -> Task:
      """Atualiza uma tarefa existente"""
      if task_id not in self.tasks:
         raise ValueError(f"Tarefa com ID {task_id} não encontrada")
      
      task = self.tasks[task_id]
      for key, value in kwargs.items():
         if hasattr(task, key):
            setattr(task, key, value)
      task.updated_at = datetime.now()
      print(f"Tarefa ID {task_id} atualizada")
      return task

   def remove_task(self, task_id: int) -> bool:
      """Remova uma tarefa"""
      if task_id not in self.tasks:
         raise ValueError(f"Tarefa com ID {task_id} não encontrada")
      
      del self.tasks[task_id]
      print(f"Tarefa ID {task_id} removida")
      return True
   
   def get_all_tasks(self) -> List[Task]:
      """Retorna todas as tarefas"""
      return list(self.tasks.values())

# Responsabilidade: Notificações
class NotificationService:
   """Responsável apenas por enviar notificações"""
   def __init__(self, notification_type: str = "email"):
      self.notification_type = notification_type
   
   def send_notification(self, recipient: str, message: str, subject: str = ""):
      """Envia uma notificação"""
      print(f"\nEnviando notificação via {self.notification_type}")
      print(f"  Para: {recipient}")
      print(f"  Assunto: {subject}")
      print(f"  Messagem: {message}")

# Responsabilidade: Geração de Relatórios
class ReportGenerator:
   """Responsável apenas por gerar relatórios"""
   def __init__(self, task_repository: TaskRepository):
      self.task_repository = task_repository
   
   def generate_report(self, format: str = "json") -> str:
      """Gera relatório das tarefas"""
      tasks = self.task_repository.get_all_tasks()

      if format == "json":
         return self._generate_json_report(tasks)
      elif format == "text":
         return self._generate_text_report(tasks)
      else:
         raise ValueError(f"Formato '{format}' não suportado")
   
   def _generate_json_report(self, tasks: List[Task]) -> str:
      """Gera relatório em formato JSON"""
      report = {
         'total_tasks': len(tasks),
         'generated_at': datetime.now().isoformat(),
         'tasks': [task.to_dict() for task in tasks]
      }
      return json.dumps(report, indent=2)

   def _generate_text_report(self, tasks: List[Task]) -> str:
      """Gera relatório em formato texto"""
      lines = [
         "=" * 50,
         "RELATÓRIO DE TAREFAS",
         "=" * 50,
         f"Total de tarefas: {len(tasks)}",
         f"Gerado em {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}",
         "=" * 50,
         ""
      ]
      
      for task in tasks:
         lines.extend([
            f"ID: {task.id}",
            f"Título: {task.title}",
            f"Status: {task.status}",
            f"Descrição: {task.description}",
            "-" * 50
         ])
      return "\n".join(lines)

# Responsabilidade: Envio de Relatórios
class ReportSender:
   """Responsável apenas por enviar relatórios"""
   def __init__(self, notification_service: NotificationService):
      self.notification_service = notification_service
   
   def send_report(self, report: str, recipient: str):
      """Envia o relatório para um destinatário"""
      self.notification_service.send_notification(
         recipient=recipient,
         subject="Relatório de Tarefas",
         message=f"Segue o relatório gerado: \n\n{report[:200]}..."
      )

# Exemplo de uso
def main():
   print("=" * 60)
   print("DEMONSTRAÇÃO DO PRINCÍPIO DE RESPONSABILIDADE ÚNICA (SRP)")
   print("=" * 60)

   # 1. Configurar conexão
   api = APIConnector("https://api.tasks.com", "my-secret-key")
   api.connect()

   # 2. Gerenciar tarefas
   task_repo = TaskRepository(api)

   task1 = task_repo.create_task(
      title="Implementar autenticação",
      description="Adicionar JWT ao sistema",
      status="em progresso"
   )
   task2 = task_repo.create_task(
      title="Escrever testes",
      description="Cobertura de 80%",
      status="pendente"
   )

   # 3. Atualizar tarefa
   task_repo.update_task(task1.id, status="concluída")

   # 4. Enviar notificação
   notifier = NotificationService(notification_type="email")
   notifier.send_notification(
      recipient="dev@empresa.com",
      subject="Tarefa Concluída",
      message=f"A tarefa '{task1.title}' foi concluída!"
   )

   # 5. Gerar relatório
   report_gen = ReportGenerator(task_repo)
   report_text = report_gen.generate_report(format="text")
   print("\n" + report_text)

   # 6. Enviar relatório
   report_sender = ReportSender(notifier)
   report_sender.send_report(report_text, "gerente@empresa.com")

   # 7. Desconectar
   api.disconnect()

if __name__ == "__main__":
   main()
