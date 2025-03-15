import enum


class Direcoes(enum.Enum):
    ESQUERDA = 1  # enum.auto()
    DIREITA = 2  # enum.auto()
    ACIMA = enum.auto()


# enuns são constantes, entao sempre em letra maiúscula
# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])
print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
print(Direcoes(1).name, Direcoes.ESQUERDA.value)


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
