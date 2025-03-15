perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '2', '3', '4'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 2?',
        'Opções': ['10', '22', '11', '3'],
        'Resposta': '10',
    },
    {
        'Pergunta': 'Quanto é 20 / 5?',
        'Opções': ['1', '4', '3', '2'],
        'Resposta': '4',
    },
]

acertos = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print('\nOpções:')
    for indice, opcao in enumerate(pergunta['Opções']):
        print(f'{indice}) {opcao}')

    while True:
        resposta_usuario = input('\nEscolha uma opção: ')

        if resposta_usuario not in pergunta['Opções']:
            print('Digite uma opção válida!\n')
        else:
            if pergunta['Resposta'] == resposta_usuario:
                print(f'Resposta correta!\n')
                acertos += 1
            else:
                print('Resposta incorreta!\n')
            break

print(f'Você acertou {acertos} de {len(perguntas)} perguntas!')
