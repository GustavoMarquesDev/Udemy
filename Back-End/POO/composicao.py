class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('Destruindo o cliente')


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero


cliente1 = Cliente('Gustavo')
cliente1.inserir_endereco('Rua 1', 123)
cliente1.inserir_endereco('Rua 2', 456)
cliente1.listar_enderecos()
