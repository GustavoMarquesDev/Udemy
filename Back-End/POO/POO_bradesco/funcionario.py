class Funcionario:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email
        self.horas: dict = {}
        self.salario_horas: dict = {}

    def cadastro_hora(self, mes: str, horas: float) -> None:
        if (mes not in self.horas):
            self.horas[mes] = horas

    def cadastro_salario_hora(self, mes: str, horas: float) -> None:
        if (mes not in self.salario_horas):
            self.salario_horas[mes] = horas

    def calcular_salario(self, mes: str) -> float | str:
        if (mes not in self.horas) or (mes not in self.salario_horas):
            return f'Mês "{mes}" não cadastrado'
        else:
            return self.horas[mes] * self.salario_horas[mes]

    def __repr__(self) -> str:
        return f'Funcionario: {self.nome}\n\
    Email: {self.email},\n\
    horas/mês: {self.horas},\n\
    salário-hora: {self.salario_horas},'
