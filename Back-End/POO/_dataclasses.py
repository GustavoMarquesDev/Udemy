from dataclasses import dataclass, asdict, astuple, field


@dataclass
class User:
    name: str = 'Missing'
    sobrenome: str = ' Not sent'
    enderecos: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.full_name = f"{self.name} {self.sobrenome}"

    # @property
    # def full_name(self):
    #     return f"{self.name} {self.sobrenome}"

    # @full_name.setter
    # def full_name(self, value):
    #     nome, *sobrenome = value.split(" ")
    #     self.name = nome
    #     self.sobrenome = (" ".join(sobrenome))


usuario = User("João", "davoli")
print(usuario)

lista = [User('maria', 'helena'), User('joao', 'davoli')]
odernada = sorted(lista, reverse=True, key=lambda x: x.name)
print(odernada)

print(asdict(usuario))
print(astuple(usuario))
