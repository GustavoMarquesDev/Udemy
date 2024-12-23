import json
from pathlib import Path

caminho_arquivo = Path(__file__).parent / 'aula116.json'

pessoa = {
    'nome': 'João Pedro',
    'sobrenome': 'Silva',
    'endereco': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.80,
    'dev': True,
    'nada': None,
    'numero_preferidos': (1, 3, 4, 5)
}


with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))
