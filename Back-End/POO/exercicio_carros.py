# class Carro:
#     def __init__(self):
#         self.carros = []

#     def criar_carro(self, nome, motor, fabricante):
#         # Adiciona um dicionário com nome, motor e fabricante à lista de carros
#         self.carros.append(
#             {"nome": nome, "motor": motor, "fabricante": fabricante})

#     def listar_carros(self):
#         # Lista cada carro com o nome, motor e fabricante
#         for carro in self.carros:
#             print(f"""Carro: {carro['nome']}, Motor: {
#                   carro['motor'].motor}, Fabricante: {carro['fabricante'].fabricante}""")


# class Motor:
#     def __init__(self, motor):
#         self.motor = motor


# class Fabricante:
#     def __init__(self, fabricante):
#         self.fabricante = fabricante


# # Testando o código
# fabricante1 = Fabricante('Honda')
# fabricante2 = Fabricante('Ford')
# motor1 = Motor('2.5/250cv')
# motor2 = Motor('V6/400cv')

# carros = Carro()
# carros.criar_carro('Civic', motor1, fabricante1)
# carros.criar_carro('Mustang', motor2, fabricante2)
# carros.listar_carros()


# ## Codigo do professor

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.motor.nome, fusca.fabricante.nome)

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
motor_1_0 = Motor('1.0')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome, fiat_uno.motor.nome, fiat_uno.fabricante.nome)
