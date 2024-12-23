class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])

    def inserir_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

    def __repr__(self):
        return f'Carrinho com {len(self._produtos)} produtos'


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
print(carrinho)
p1, p2 = Produto('Carro', 1000), Produto('Moto', 2000)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())

print(carrinho)
