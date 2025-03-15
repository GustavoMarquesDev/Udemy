from time import sleep
from threading import Thread, Lock


# class MeuThread(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo
#         super().__init__()

#     def run(self):
#         sleep(self.tempo)
#         print(f'Thread {self.texto} terminou')


# t1 = MeuThread('1', 5)  # termina em ultimo
# t1.start()

# t2 = MeuThread('2', 3)  # termina em segundo
# t2.start()

# t3 = MeuThread('3', 2)  # termina em primeiro
# t3.start()


# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(f'Thread {texto} terminou')


# t4 = Thread(target=vai_demorar, args=('4', 1))  # vai terminar primeiro
# t4.start()

# # Se ficar assim ele esta na mesma thread no for, entao o for não executa até acabar aqui
# # while t1.is_alive():
# #     print('Esperando a thread terminar...')
# #     sleep(2)


# for i in range(10):
#     print(i)
#     sleep(1)

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()  # Para não quebrar o programa, trava para ser comprado um por vez

    def comprar(self, quantidade):
        # É a chave para esse bloco de codigo, apenas um pega por vez os outros ficam em espera
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes')
            self.lock.release()  # libera o metodo para ser executado por outro thread
            return
        sleep(1)

        self.estoque -= quantidade
        print(
            f'Você comprou {quantidade} ingresso(s). Ainda temos {self.estoque} \n')
        self.lock.release()  # libera o metodo para ser executado por outro thread


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 10):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
