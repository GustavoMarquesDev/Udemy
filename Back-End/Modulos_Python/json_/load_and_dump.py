import json
import os

NOME_ARQUIVO = 'teste.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(os.path.dirname(__file__), NOME_ARQUIVO))


print(os.path.dirname(__file__))


nomes = {'nome': ['Pedro', 'João'],
         'idade': [10, 20],
         'have_carro': [True, False]
         }

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(nomes, arquivo, ensure_ascii=False, indent=4)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r', encoding='utf-8') as arquivo:  # converte dict novamente
    nomes_leitura = json.load(arquivo)

print(nomes_leitura)
