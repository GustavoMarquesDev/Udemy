def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


clientes = adiciona_clientes('João Pedro')
adiciona_clientes('Maria Silva', clientes)
adiciona_clientes('Pedro Silva')
print(clientes)

clientes2 = adiciona_clientes('João Paulo')
adiciona_clientes('Julia Silva', clientes2)

print(clientes2)
