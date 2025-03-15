from pathlib import Path

from PIL import Image

ROOT_FOLDER = Path(__file__).parent
IMAGE_PATH = ROOT_FOLDER / 'troxa.jpg'
NEW_IMAGE_PATH = ROOT_FOLDER / 'new_troxa.jpg'


pil_image = Image.open(IMAGE_PATH)
width, height = pil_image.size

# para salvar as informações sobre a imagem que constam nela
exif = pil_image.info['exif']

# regra de 3 para se auto dimensionar
# width ---- new_width: valor novo que você quer
# height ---     x: valor que você vai deixar se auto dimensionar

new_width = 640
new_height = round(height * (new_width / width))

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    fp=NEW_IMAGE_PATH,
    quality=70,
    exif=exif,
)
