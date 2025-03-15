from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

total = 0
for produto in produtos:
    total += round(produto['preco'], 2)

total = round(total, 2)


def funcao_do_reduce(acumlador, produto):
    print('acumlador', acumlador)
    print('produto', produto)
    return acumlador + produto['preco']


total = round(reduce(funcao_do_reduce, produtos, 0), 2)
print(total)

print(total)

total = reduce(lambda acc, valor: acc + valor['preco'], produtos, 0)
total = round(total, 2)

print(total)

print(round(sum([p['preco'] for p in produtos]), 2))
