class Retangulo:
    def __init__(self, lado_a: float, lado_b: float):
        self.a = lado_a
        self.b = lado_b

    def muda_valor(self, novo_a: float, novo_b: float):
        self.a = novo_a
        self.b = novo_b

    def retorna_lado(self):
        print(f'O Retângulo possui dimensões {self.a} x {self.b}')

    def area(self) -> float:
        return self.a * self.b
