from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / "exemplo.csv"
print(CAMINHO_CSV)

with open(CAMINHO_CSV, "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo, delimiter=";")

    for linha in leitor:
        print(linha[0])
