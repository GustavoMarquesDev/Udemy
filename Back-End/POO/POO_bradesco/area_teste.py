import math
from area import Retangulo

while True:
    try:
        piso_a = float(input('Digite o valor de um lado do piso: '))
        piso_b = float(input('Digite o valor de outro lado do piso: '))

        if piso_a == 0 or piso_b == 0:
            raise ValueError

        piso = Retangulo(piso_a, piso_b)

        az_a = float(input('Digite o valor de um lado do azulejo: '))
        az_b = float(input('Digite o valor de outro lado do azulejo: '))

        azulejo = Retangulo(az_a, az_b)

        area_piso = piso.area()
        area_azulejo = azulejo.area()

        qntd_az = area_piso / area_azulejo

        if area_piso % area_azulejo == 0:
            print(
                f'A quantidade exata de azulejos para preencher o piso é {qntd_az}')
        else:
            print(f'''A quantidade mínima de azulejos para preencher o piso é {
                  math.ceil(qntd_az)}''')

    except ValueError:
        print('Valores inválidos')

    except Exception as e:
        print(f'Erro: {e}')
