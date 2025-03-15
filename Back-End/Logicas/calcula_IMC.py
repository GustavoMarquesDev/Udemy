from os import system


def calcula_IMC(peso, altura):
    indice = peso / (altura ** 2)
    return round(indice, 2)


def classifica_IMC(imc):
    if imc < 18.5:
        return 'Magreza', 'Obesidade grau 0'
    elif 18.5 <= imc <= 24.9:
        return 'Normal', 'Obesidade grau 0'
    elif 24.9 < imc <= 29.9:
        return 'Sobrepeso', 'Obesidade grau 1'
    elif 29.9 < imc <= 34.9:
        return 'Obesidade', 'Obesidade grau 2'
    else:
        return 'Obesidade Grave', 'Obesidade grau 3'


def main():
    try:
        while True:
            # Entrada de dados
            peso = float(input('Insira o peso em Kilogramas: '))
            altura = float(input('Insira a altura em Metros: '))

            if peso <= 0 or altura <= 0:
                raise ValueError(
                    'Você não pode calcular com valores iguais ou menores que zero.')

            # Cálculo do IMC
            imc = calcula_IMC(peso, altura)
            classificacao, grau_obesidade = classifica_IMC(imc)

            # Exibindo o resultado
            print(f'Seu índice: {imc}')
            print(f'Sua classificação é "{classificacao}", {grau_obesidade}')

            # Pergunta se deseja continuar
            continuar = input('Deseja continuar? [S/N]: ').lower()
            if continuar == 'n':
                break

            system('cls')

    except ValueError as erro:
        print(f'Erro: {erro}')
    except ZeroDivisionError:
        print('Você está tentando calcular com altura igual a zero.')
    finally:
        system('cls')  # Limpa a tela quando o programa termina.
