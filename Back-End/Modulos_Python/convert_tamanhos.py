import math
import os
from itertools import count


def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    if tamanho_em_bytes <= 0:
        return '0 B'

    abreviacao_tamanhos = 'B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    potencia = base ** (indice_abreviacao_tamanhos)

    tamanho_final = round(tamanho_em_bytes / potencia, 2)
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]

    return f'{tamanho_final} {abreviacao_tamanho}'


caminho = os.path.join(
    r'C:\\Users\\Microsoft\\OneDrive\\Documentos\\FIFA 23')
count = count()  # Para saber em qual for estamos

for pasta in os.listdir(caminho):
    # Cria caminho completo de cada pasta
    caminho_completo_pasta = os.path.join(caminho, pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print(imagem)

for root, dirs, files in os.walk(caminho):
    the_count = next(count)
    print(the_count, 'Pasta atual:', root)

    for dir_ in dirs:
        print(the_count, 'Sub-pasta:', dir_)

        for file_ in files:
            full_path = os.path.join(root, file_)
            tamanho = os.path.getsize(full_path)
            print(the_count, 'Arquivo:', file_, formata_tamanho(tamanho))
