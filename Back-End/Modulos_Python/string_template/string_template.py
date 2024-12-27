import json
import locale
import string
from pathlib import Path
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
CAMINHO_MENSAGEM = Path(__file__).parent / 'mensagem.txt'


def converte_para_brl(numero: float | int) -> str:
    brl = locale.currency(numero, symbol=True, grouping=True)
    return brl


data = datetime(2024, 12, 20)
dados = dict(
    nome='Gustavo',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O.M',
    telefone='(11) 99999-9999',

)

# print(json.dumps(dados, indent=4, ensure_ascii=False))


with open(CAMINHO_MENSAGEM, 'r', encoding='utf-8') as arquivo:
    arquivo = arquivo.read()

    template = string.Template(arquivo)
    print(template.substitute(dados))
