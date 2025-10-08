from abc import ABC, abstractmethod

class NotificationSander(ABC):

   @abstractmethod
   def send_notification(self, message: str) -> None: pass

class EmailNotificationSender(NotificationSander):
   
   def send_notification(self, message: str) -> None:
      print(f"SMS Message: {message}")

class Notificator:
   def __init__(self, notification_sender: NotificationSander) -> None:
      self.__notification_sender = notification_sender
   
   def send(self, message: str) -> None:
      self.__notification_sender.send_notification(message)

obj = Notificator(EmailNotificationSender())
obj.send('Hello World')