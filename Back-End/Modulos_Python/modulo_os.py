import os
from itertools import count

caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
print(caminho)
diretorio, arquivo = os.path.split(caminho)
print(diretorio, arquivo)
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(nome_arquivo, extensao_arquivo)
print(os.path.exists(
    '\\Users\\Microsoft\\OneDrive\\Documentos\\Programação\\Udemy\\Back-End\\Modulos Python'))
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(caminho))


caminho2 = os.path.join(
    r'C:\\Users\\Microsoft\\OneDrive\\Documentos\\Casa')
count = count()  # Para saber em qual for estamos

for pasta in os.listdir(caminho2):
    # Cria caminho completo de cada pasta
    caminho_completo_pasta = os.path.join(caminho2, pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print(imagem)

for root, dirs, files in os.walk(caminho2):
    the_count = next(count)
    print(the_count, 'Pasta atual:', root)

    for dir_ in dirs:
        print(the_count, 'Sub-pasta:', dir_)
        # os.unlink(caminho_completo_pasta) Apaga tudo na pasta

        # for file_ in files:
        #     full_path = os.path.join(root, file_)
        #     print(the_count, 'Arquivo:', full_path)
