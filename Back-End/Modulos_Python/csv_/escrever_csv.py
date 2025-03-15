import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / "exemplo_escrito.csv"

lista_clientes = [
    {'Nome': 'Gustavo', 'Endereço': 'Av1, 22'},
    {'Nome': 'Pedro', 'Endereço': 'Av2, 33'},
    {'Nome': 'Maria', 'Endereço': 'Av3, 44'},
]

# with open(CAMINHO_CSV, 'w', encoding='utf-8') as arquivo:
#     nome_colunas = lista_clientes[0].keys()
#     escritor = csv.writer(arquivo, delimiter=';')

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente.values())


# Com DictWriter
with open(CAMINHO_CSV, 'w', encoding='utf-8') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(arquivo, delimiter=';', fieldnames=nome_colunas)

    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)
