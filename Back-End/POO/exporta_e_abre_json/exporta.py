import json

local = 'C:\\Users\\Microsoft\\OneDrive\\Documentos\\Programação\\Udemy\\Back-End\\POO\\exporta_e_abre_json\\exporta_json.json'


class Pessoa:
    def __init__(self, nome, idade, sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


gustavo = Pessoa("Gustavo", 20, "Masculino")
exporta_json = gustavo.__dict__


with open(local, "w", encoding='UTF-8') as file:
    json.dump(exporta_json, file, indent=4)
