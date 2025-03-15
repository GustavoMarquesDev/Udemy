class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)


Pessoa.metodo_de_classe()
p2 = Pessoa.criar_com_50_anos('Gustavo')
print(p2.nome, p2.idade)
