class Caneta:
    def __init__(self, cor):
        self.cor = cor  # Armazena a cor em _cor

    @property
    def cor(self):
        print('Estou no getter')
        return self._cor  # Retorna o valor de _cor

    @cor.setter
    def cor(self, valor):
        if valor == 'rosa':
            raise ValueError('Cor inválida')
        print('Estou no setter')
        self._cor = valor


caneta = Caneta('verde')
caneta.cor = 'pink'
print(caneta.cor)
