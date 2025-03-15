import copy


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos_com_aumento = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in copy.deepcopy(produtos)
]


produto_ordenador_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['nome'], reverse=True
)

produto_ordenador_por_valor = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['preco'], reverse=True
)

print(*produtos, sep='\n')
print()
print(*produtos_com_aumento, sep='\n')
print()
print(*produto_ordenador_por_nome, sep='\n')
print()
print(*produto_ordenador_por_valor, sep='\n')
