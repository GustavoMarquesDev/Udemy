def adiciona_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = meu_repr
    return cls


def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        if 'Terra' in resultado:
            return 'Você está em casa'
        return resultado
    return interno


@adiciona_repr
class Time():
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta():
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
        return f'O nome do planeta é {self.nome}'


# Planeta = adiciona_repr(Planeta) Não é muito utilizado desta forma mas funciona


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')


print(brasil)
print(terra)
print(terra.falar_nome())
print(marte.falar_nome())