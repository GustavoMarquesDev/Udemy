import sys
from argparse import ArgumentParser


argumentos = sys.argv
qtd_argumentos = len(argumentos)

# if qtd_argumentos <= 1:
#     print('Nenhum argumento fornecido')
# else:
#     print(f'Você passou os argumentos {argumentos[1:]}')

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela',
    # type=str,  # Tipo do argumento
    metavar='STRING',
    # default='Olá mundo',  # valor padrão
    required=False,
    action='append',
    # nargs='+'  # permite mais de um argumento
)

parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs',
    action='store_true',

)
args = parser.parse_args()


if args.basic is None:
    print('Você não passou o valor de b')
    print(args.basic)

else:
    print(f'Você passou o valor de basic: {args.basic}')


print(args.verbose)
