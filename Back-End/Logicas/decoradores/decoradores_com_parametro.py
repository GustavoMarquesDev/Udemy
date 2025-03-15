def parametros_decorador(nome):
    def decorador(func):
        print('Decorador', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador


@parametros_decorador(nome='terceiro')
@parametros_decorador(nome='segundo')
@parametros_decorador(nome='primerio')
def soma(a, b):
    return a + b


dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
