from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

CAMINHO_RAIZ = Path(__file__).parent
CAMINHOS_ORIGINAIS = CAMINHO_RAIZ / "pdfs_originais"
IMAGENS_EXTRAIDAS = CAMINHO_RAIZ / "imagens_extractadas"
PASTA_NOVA = CAMINHO_RAIZ / 'pdfs_novos'
RELATORIO_BACEN = CAMINHOS_ORIGINAIS / "R20241220.pdf"

PASTA_NOVA.mkdir(exist_ok=True)
IMAGENS_EXTRAIDAS.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))

# for page in reader.pages:
#     print(page)

page0 = reader.pages[0]
# print(page0.extract_text())


# para pegar a primeira imagem do pdf
# imagem0 = page0.images[0]
# with open(PASTA_NOVA / imagem0.name, "wb") as fp:
#     fp.write(imagem0.data)

# extrai todos os objetos de imagem do pdf
for image_file_object in page0.images:
    count = 0
    with open(IMAGENS_EXTRAIDAS / f"{image_file_object.name}", "wb") as fp:
        fp.write(image_file_object.data)
        count += 1


# para escrever um pdf
writer = PdfWriter()
with open(PASTA_NOVA / "novo_PDF.pdf", "wb") as fp:
    for page in reader.pages:
        writer.add_page(page)
    writer.write(fp)


# para escrever cada pagina em um pdf separado
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f"pagina_{i + 1}.pdf", "wb") as fp:
        writer.add_page(page)
        writer.write(fp)


files = [
    PASTA_NOVA / "pagina_1.pdf",
    PASTA_NOVA / "pagina_2.pdf",
]

merger = PdfMerger()
for file in files:
    merger.append(file)

merger.write(PASTA_NOVA / "paginas_mergeados.pdf")
merger.close()
