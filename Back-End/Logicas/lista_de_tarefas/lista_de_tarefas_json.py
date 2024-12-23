import os
from time import sleep
import ast
import json
from pathlib import Path

local_do_arquivo = Path(__file__).parent / 'tarefas.json'


def limpar_terminal():
    sleep(2)
    os.system('cls')


def exibe_lista_desempacotada(lista_de_tarefas):
    print(* lista_de_tarefas, sep='\n')
    print()


def verifica_entrada(entrada, lista_de_tarefas, tarefas_removidas):

    if entrada.lower() == 'listar':
        if len(lista_de_tarefas) == 0:
            print('Não há tarefas para listar!!!. \n')
            limpar_terminal()
        else:
            print('TAREFAS: ')
            exibe_lista_desempacotada(lista_de_tarefas)

    elif entrada.lower() == 'desfazer':
        if len(lista_de_tarefas) == 0:
            print('Não há tarefas para desfazer!!!. \n')
            limpar_terminal()
        else:
            os.system('cls')
            ultima_tarefa = lista_de_tarefas.pop()
            tarefas_removidas.append(ultima_tarefa)
            print(f'TAREFA: "{ultima_tarefa}" removida com sucesso!!!\n')
            print('TAREFAS: ')
            exibe_lista_desempacotada(lista_de_tarefas)

    elif entrada.lower() == 'refazer':
        if len(tarefas_removidas) == 0:
            print('Não há tarefas para refazer!!!. \n')
            limpar_terminal()
        else:
            os.system('cls')
            lista_de_tarefas.append(tarefas_removidas.pop())
            print(f'TAREFA: "{lista_de_tarefas[-1]}" refeita com sucesso!!!\n')
            print('TAREFAS: ')
            exibe_lista_desempacotada(lista_de_tarefas)

    elif not entrada.strip():
        print('Digite alguma tarefa.')
        limpar_terminal()

    elif entrada != 'sair' and entrada != 'SAIR':
        lista_de_tarefas.append(entrada)
        print('Tarefa adicionada com sucesso!!!')
        limpar_terminal()

    return lista_de_tarefas


comandos = ['listar', 'desfazer', 'refazer']


lista_de_tarefas = []
tarefas_removidas = []


try:
    with open(local_do_arquivo, 'r', encoding='UTF-8') as arquivo:

        if arquivo:
            carregar_lista = input(
                'Já existe um arquivo com tarefas. Deseja carregá-lo? [S/N]:')

            while carregar_lista.lower() != 's' and carregar_lista.lower() != 'n':
                carregar_lista = input('Digite uma opção válida [S/N]: ')

            if carregar_lista.lower() == 's':
                conteudo = json.load(arquivo)
                print('Tarefas carregadas com sucesso!!!\n')
                lista_de_tarefas.extend(conteudo)

        if carregar_lista.lower() == 'n':
            lista_de_tarefas = []


except FileNotFoundError:
    print('Nenhum arquivo encontrado, iniciando um novo arquivo...')
    limpar_terminal()
except Exception as e:
    print(f"Ocorreu um erro ao carregar o arquivo: {e}")

while True:

    print('Comandos: listar | desfazer | refazer | ou digite "sair" para salvar e sair.')
    print()
    entrada = input('Digite uma tarefa ou um comando: ')
    print()

    verifica_entrada(entrada, lista_de_tarefas, tarefas_removidas)

    if entrada.lower() == 'sair':
        break

salvar_ou_nao = input('Deseja salvar as tarefas? [S/N]: ')


while salvar_ou_nao.lower() != 's' and salvar_ou_nao.lower() != 'n':
    salvar_ou_nao = input('Digite uma opção válida [S/N]: ')

if salvar_ou_nao.lower() == 's':

    with open(local_do_arquivo, 'w', encoding='UTF-8') as arquivo:
        json.dump(lista_de_tarefas, arquivo, ensure_ascii=False, indent=4)
        print('Tarefas salvas com sucesso!')

elif salvar_ou_nao.lower() == 'n':
    pass
