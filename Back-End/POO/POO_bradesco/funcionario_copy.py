from dataclasses import dataclass, field


@dataclass
class Funcionario:

    nome: str = field(default='')
    email: str = field(default='')
    horas: dict = field(default_factory=dict)
    salario_horas: dict = field(default_factory=dict)

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
