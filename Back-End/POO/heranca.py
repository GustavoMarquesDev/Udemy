class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(f"""Meu nome é {self.nome} e meu sobrenome é {
              self.sobrenome}  minha classe é {self.__class__.__name__}""")


class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
    ...


c1 = Cliente("João", "Silva")
c1.falar_nome_classe()

a1 = Aluno("Maria", "Silva")
a1.falar_nome_classe()
