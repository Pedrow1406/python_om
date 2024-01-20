"""   POLIMORFISMO
Polimorfismo em Python Orientado a Objetos
Polimorfismo é o princípio que permite que
classes derivadas de uma mesma superclasse
tenham métodos iguais (com mesma assinatura)
mas comportamentos diferentes.
Assinatura do métodos = Mesmo nome e quantidade de parâmetros
(retorno não faz parte da assinatura)
Opinião + princípios que contam:
Assinatura do método: nome, parâmetros e retorno iguais
Princípio da substituição de liskov
Objetos de uma superclasse devem ser substituíveis
por objetos de uma subclass sem quebrar a aplicação
"""

from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, mensagem):
        self._msg = mensagem

    @abstractmethod
    def send(self) -> bool: ...
    
class NotificationEmail(Notification):
    def send(self) -> bool:
        if self._msg: 
            print(f'E-mail: {self._msg}')
            return True
        return False
class NotificationSMS(Notification):
    def send(self) -> bool:
        if self._msg:
            print(f'SMS: {self._msg}')
            return True
        return False
def notificar(notification: Notification):
    send_notification = notification.send()

    if send_notification:
        print('Notificação foi Enviada')
        return
    print('Notificação não foi enviada')


email = NotificationEmail('Pedrow é lindo')
notificar(email)
sms = NotificationSMS('Pedrow é Sigma')
notificar(sms)
nada = NotificationSMS('')
notificar(nada)
sms.send()
email.send()