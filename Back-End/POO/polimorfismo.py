from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando -', self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando -', self.mensagem)
        return False


n = NotificacaoEmail('testando e-mail')
n.enviar()


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada com sucesso')
    else:
        print('Notificação não enviada')


notificacao_email = NotificacaoEmail('testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando sms')
notificar(notificacao_sms)
