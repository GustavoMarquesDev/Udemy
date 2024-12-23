from pathlib import Path
# caminho_arquivo = '\\Users\\Microsoft\\OneDrive\\Documentos\\Programação\\Udemy\\Back-End\\POO\\context_manager\\teste.txt'
caminho_arquivo = Path(__file__).parent / 'teste.txt'


class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('Abrindo arquivo')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf-8')
        return self._arquivo

    def __exit__(self, class_exception, exeception_, traceback_):
        print('Fechando arquivo')
        self._arquivo.close()
        if class_exception or exeception_ or traceback_:
            print(class_exception)
            print(exeception_)
            print(traceback_)
            exeception_.add_note('Minha Nota')
        # return True


# instancia = MyOpen('teste.txt', 'w')

with MyOpen(caminho_arquivo, 'w') as arquivo:
    arquivo.write('linha 1 \n', 123)  # Causando o erro
    arquivo.write('linha 2 \n')
    arquivo.write('linha 3 \n')

    print('WITH', arquivo)
