# class minhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(minhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno


# nome = minhaString("Carlos")
# print(nome.upper())


class A(object):
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('EI, burlei o sistema')

    def metodo(self):
        print('C')


c = C('Atributo', 'Qualquer outra coisa')
print(c.atributo)
print(c.outra_coisa)


print(C.__mro__)
