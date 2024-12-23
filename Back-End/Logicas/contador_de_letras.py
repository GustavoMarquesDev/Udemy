frase = 'O Python á uma linguagem de programação multiparadgma. Python foi criado por Guido van Rossum'

i = 0
qtd_apareceu_mais_vezes = 0
letras_apareceram_mais_vezes = []

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_atual > qtd_apareceu_mais_vezes:
        qtd_apareceu_mais_vezes = qtd_atual
        letras_apareceram_mais_vezes = [letra_atual]
    elif qtd_atual == qtd_apareceu_mais_vezes and letra_atual not in letras_apareceram_mais_vezes:
        letras_apareceram_mais_vezes.append(letra_atual)

    i += 1

if len(letras_apareceram_mais_vezes) == 1:
    print(
        'A letra que apareceu mais vezes foi '
        f'"{letras_apareceram_mais_vezes[0]}"'
        f' ela apareceu {qtd_apareceu_mais_vezes} vezes'
    )
else:
    print(
        'As letras que apareceram mais vezes foram '
        f'{", ".join(letras_apareceram_mais_vezes)}'
        f', cada uma apareceu {qtd_apareceu_mais_vezes} vezes'
    )
