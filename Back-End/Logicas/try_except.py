try:
    a = 18
    b = 2
    c = a / b

    nome = 'Luiz Otávio'

    print(nome[1000])

except ZeroDivisionError:
    print('Divide por zero')

except ValueError:
    print('Valor errado')

except NameError:
    print('Nome errado')

except AttributeError:
    print('Atributo errado')

except (IndexError, KeyError, TypeError) as error:
    print(f'Erro: {error}')
    print(f'{error.__class__.__name__}')

except Exception as e:
    print('Houve um erro desconhecido, desculpe')


try:
    print('Abrir arquivo')
    8/p  # Forçando o erro

except ZeroDivisionError as error:
    print(f'Erro: {error}')
    print(f'{error.__class__.__name__}')

except NameError:
    print('Tu ta fazendo merda')

else:
    print('Executou')  # Se não houver erro, executar este bloco
finally:
    print('Fechar arquivo')


def nao_aceita_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True


def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (int, float)):
        raise TypeError(
            f'"{n} deve ser int ou float."'
            f'"{tipo_n.__name__}" enviado.'
        )


def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceita_zero(d)
    return n/d


print(divide(10, '0'))
