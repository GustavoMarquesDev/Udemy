class MeuError(Exception):
    ...


class OutroError(Exception):
    ...


def levantar():
    exception_ = MeuError("A mensagem de erro")
    exception_.add_note('Olha a nota 1')
    exception_.add_note('Você errou isso')
    raise exception_


try:

    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError("Vou lançar de novo")
    raise exception_ from error
