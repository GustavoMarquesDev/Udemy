while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite um número: ')
    operador = input('Digite um operador (+ - / *)')

    numeros_validos = None
    operadores_permitidos = '+-/*'
    numero_1_float = 0
    numero_2_float = 0

    try:

        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operaodor')
        continue

    if (operador == '+'):
        resultado = numero_1_float + numero_2_float
        print(f'O resultado da soma é {resultado}')

    elif (operador == '-'):
        resultado = numero_1_float - numero_2_float
        print(f'O resultado da subtração é {resultado}')

    elif (operador == '/'):
        resultado = numero_1_float / numero_2_float
        print(f'O resultado da divisão é {resultado}')

    elif (operador == '*'):
        resultado = numero_1_float * numero_2_float
        print(f'O resultado da multiplicação é {resultado}')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
