import time
import os


class Cronometro:
    def __init__(self, segundos: int = 0, minutos: int = 0, horas: int = 0):
        self.segundos = segundos
        self.minutos = minutos
        self.horas = horas

    def incremento(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
            if self.minutos >= 60:
                self.minutos = 0
                self.horas += 1

    def start(self):
        while True:
            os.system('cls')
            print(self)
            self.incremento()
            time.sleep(1)

    def __repr__(self) -> str:
        return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'


cronometro1 = Cronometro()
cronometro1.start()
