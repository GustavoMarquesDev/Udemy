# class Ponto:
#     def __init__(self, x, y, z='String'):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __str__(self):
#         return f'(x={self.x}, y={self.y})'

#     def __repr__(self):
#         # class_name = self.__class__.__name__
#         class_name = type(self).__name__
#         return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'


# p1 = Ponto(1, 2)
# p2 = Ponto(3, 4)
# print(p1)
# print(repr(p2))


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        resultado_self = self.x > other.x
        resultado_other = other.x > self.y
        return resultado_self > resultado_other


if __name__ == '__main__':
    p1 = Ponto(1, 2)
    p2 = Ponto(3, 4)
    p3 = p1 + p2
    print(p3)
    print('P1 é maior do que p2', p1 > p2)
    print('P2 é maior do que p1', p2 > p1)
