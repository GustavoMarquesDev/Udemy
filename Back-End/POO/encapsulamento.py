class Foo:
    def __init__(self):
        self.public = 'Isso é publico'
        self._protected = 'Isso é protegido'

    def metodo_publico(self):
        return 'metodo_publico'


f = Foo()
print(f.public)
print(f._protected)
