from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'Nota': 'A'},
    {'nome': 'Otávio', 'Nota': 'B'},
    {'nome': 'Pedro', 'Nota': 'A'},
    {'nome': 'Lucas', 'Nota': 'C'},
    {'nome': 'Paulo', 'Nota': 'D'},
    {'nome': 'Alex', 'Nota': 'A'},
    {'nome': 'Juca', 'Nota': 'B'},
    {'nome': 'John', 'Nota': 'A'},
    {'nome': 'Delhi', 'Nota': 'C'},
]


def ordena(aluno):
    return aluno['Nota']


alunos_grupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_grupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)

