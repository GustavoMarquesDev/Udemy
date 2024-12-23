import os
from time import sleep

lista_usuario = []


while True:

    print('Por favor, selecione uma opção ou pressiona qualquer outra tecla para sair:\n')
    opcao_usuario = input(
        '[I]nserir ' '[A]pagar ' '[L]istar :')

    resposta_usuario_maiusculo = opcao_usuario.upper()

    if resposta_usuario_maiusculo == 'I':
        os.system('cls')
        print('Você selecionou: Inserir\n')
        item_para_adicionar = input('Digite o item a ser inserido:\n ')
        lista_usuario.append(item_para_adicionar)
        print('Item inserido com sucesso!!!')

    elif resposta_usuario_maiusculo == 'A':
        os.system('cls')
        print('Você selecionou: Apagar\n')
        try:
            item_para_apagar = input(
                'Digite o item ou o indíce a ser apagado:\n ')

            if (item_para_apagar.isdigit() and int(item_para_apagar) < len(lista_usuario)):
                item_para_apagar = int(item_para_apagar)
                lista_usuario.pop(item_para_apagar)
                print('Item apagado com sucesso!!!\n')
                continue

            if (item_para_apagar in lista_usuario):
                lista_usuario.remove(item_para_apagar)
                print('Item apagado com sucesso!!!\n')
            else:
                print('Item não encontrado')
                continue

        except ValueError:
            print('Digite um item ou um índice válido')
            print(f'Houve um erro {ValueError}')
            continue

        except IndexError:
            print('Digite um índice válido')
            print(f'Houve um erro {IndexError}')
            continue

    elif resposta_usuario_maiusculo == 'L':
        os.system('cls')
        print('Você selecionou: Listar\n')

        if (len(lista_usuario) == 0):
            print('Não há itens na lista')

        else:
            for iten in lista_usuario:
                print(f'-{iten}\n')

    else:
        print('Saindo...')
        sleep(2)
        os.system('cls')
        break
