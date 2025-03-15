from collections import namedtuple
from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'


Carta2 = namedtuple('Carta', ['valor', 'naipe'],
                    defaults=['a', 'espadas'])
as_de_espadas = Carta2(valor="a", naipe='espadas')
print(as_de_espadas)
print(as_de_espadas.valor)
print(as_de_espadas.naipe)
print(as_de_espadas[0])
