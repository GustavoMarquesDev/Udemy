from pathlib import Path
caminho_arquivo = Path(__file__).parent / 'aula116.txt'


# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()


with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Hello World!\n')
    arquivo.write('Hello World 2!\n')
    arquivo.writelines(
        ('Hello World 3!\n', 'Hello World 4!\n')
    )
    arquivo.seek(0, 0)  # reseta o cursor para o inicio do arquivo
    # ler a primeira linha e limpar todos os espaços no começo e no final
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())
