import json
from pprint import pprint
from typing import TypedDict  # Para usar tipos


class Pessoa(TypedDict):
    nome: str
    idade: int
    have_carro: bool


string_json = """

{
    "nome": ["Pedro", "João"],
    "idade": [10, 20],
    "have_carro": [true, false]
    
}
"""

pessoas: Pessoa = json.loads(string_json)  # Converte em dict
pessoa_convertida = json.dumps(
    pessoas, ensure_ascii=False, indent=4)  # Converte em json
print(type(pessoa_convertida))
print(pessoa_convertida)
