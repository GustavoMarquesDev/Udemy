def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi " {resultado} "')
        print('Ok, você foi decorado')
        return resultado
    return interna


@criar_funcao
def inverter_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Parâmetro deve ser string')


string_invertida = inverter_string('123')

print(string_invertida)
