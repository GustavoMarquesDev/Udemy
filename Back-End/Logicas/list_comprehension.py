from sys import getsizeof
import pprint


def p(v):
    pprint.pprint(v, width=40, sort_dicts=False)


pessoa = {
    'nome': 'Luiz Otávio',
    'idade': 25,
    'sexo': 'masculino',
    'cidade': 'São Paulo'
}

a1, a11, a2, *a3 = pessoa.items()


def mostrar(*args, **kwargs):

    for chave, valor in kwargs.items():
        print(chave, ':', valor)

    for valor in args:
        print(valor)


# mostrar('pedro', 'paulo', nome='Joao', sobrenome='Marques')


produtos = [
    {'nome': 'Notebook', 'preco': 1000},
    {'nome': 'Geladeira', 'preco': 2000},
    {'nome': 'Computador', 'preco': 3000},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 2000 else {**produto}
    for produto in produtos
]


# print(*novos_produtos, sep='\n')

# p(novos_produtos)

produto = {
    'nome': 'Notebook',
    'preco': 1000,
    'cor': 'verde',
    'tamanho': 'grande',
}


dc = {
    chave: valor.upper()
    if isinstance(valor, str)
    else valor
    for chave, valor in produto.items()
}

# print(dc)

lista = [
    'a', 1, 1.1, True, None, [0, 1, 2], (1, 2), {'a': 1}, {0, 1}
]

for item in lista:
    if isinstance(item, list):
        item.append(10)
        print(item, isinstance(item, list))

    if isinstance(item, (int, float)):
        print(item, item * 2)


iterable = ['eu', 'sou', 'um', 'iter']
iterator = iter(iterable)
# print(next(iterator))


lista = [n for n in range(100000)]
generator = (n for n in range(1000))
# print(getsizeof(generator))
# print(getsizeof(lista))
# print(next(generator))


def generator2(n=0):
    yield n
    print('Continuando')
    yield 2


gen = generator2(3)
# print(next(gen))
# print(next(gen))


def generator3(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return


gen2 = generator3()
# for n in gen2:
#     print(n)
