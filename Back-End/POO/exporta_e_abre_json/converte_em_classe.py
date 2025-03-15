import json
from exporta import Pessoa, local


with open(local, 'r', encoding='utf-8') as arquivo:
    gustavo = json.load(arquivo)


gustavo = Pessoa(**gustavo)

print(gustavo.nome)
print(gustavo.idade)
print(gustavo.sexo)
