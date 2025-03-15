from pathlib import Path
from shutil import rmtree

# print(Path.home())# raiz do sistema operacional
caminho_projeto = Path()

# caminho do arquivo atual
caminho_arquivo = Path(__file__)


# volta um caminho e cria outro caminho
ideias = caminho_arquivo.parent / 'teste.txt'

# Cria o caminho onde sera criado o arquivo, somente cria o caminho
caminho_arquivo = Path.home() / 'OneDrive' / 'Documentos' / 'Programação' / \
    'Udemy' / 'Back-End' / 'Modulos Python' / 'pathlib_' / 'arquivo.txt'

# # Cria o arquivo
# caminho_arquivo.touch()
# caminho_arquivo.write_text('teste')

# deleta o arquivo
# caminho_arquivo.unlink()

# # ler o conteudo do arquivo
# print(arquivo.read_text())

# apaga o conteudo do arquivo, o deixa em branco
# caminho_arquivo.write_text('')

# with caminho_arquivo.open('a+') as file:
#     file.write('teste\n')
#     file.write('teste2\n')

# print(caminho_arquivo.read_text())

caminho_pasta = Path.home() / 'OneDrive' / 'Documentos' / 'Programação' / \
    'Udemy' / 'Back-End' / 'Modulos Python' / 'pathlib_' / 'pasta_teste'

caminho_pasta.mkdir(exist_ok=True)
# subpasta = caminho_pasta / 'subpasta'
# subpasta.mkdir(exist_ok=True)

# mais_arquivo = subpasta / 'arquivo.txt'
# mais_arquivo.touch()
# mais_arquivo.write_text('teste')

# apaga a pasta, mas somente se estiver vazia
# caminho_pasta.rmdir()

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'arquivo{i}.txt'

    if file.exists():
        file.unlink()

    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write(f'Hello World {i}\n')
        text_file.write(f'file {i}')

# apaga a pasta e todos os arquivos dentro dela recursivamente
# rmtree(caminho_pasta)
