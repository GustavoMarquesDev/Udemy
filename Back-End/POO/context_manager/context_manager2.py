from contextlib import contextmanager

caminho_arquivo = '\\Users\\Microsoft\\OneDrive\\Documentos\\Programação\\Udemy\\Back-End\\POO\\context_manager\\teste2.txt'


@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf-8')
        yield arquivo
    except Exception as e:
        print('Ocorreu um erro', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()


with my_open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('linha 1 \n')
    arquivo.write('linha 2 \n')
    arquivo.write('linha 3 \n')

    print('WITH', arquivo)
