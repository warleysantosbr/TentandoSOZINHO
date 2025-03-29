import os
import shutil
import pytesseract
from PIL import Image
import cv2

# Caminho para o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR'

# Pasta com as imagens
pasta_imagens = r'C:\Users\quali\Downloads\warley automa\teste\descarregadas'
pasta_destino = r'C:\Users\quali\Downloads\warley automa\teste\29-03'

# Lista de imagens ordenadas
imagens = sorted([f for f in os.listdir(pasta_imagens) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])

ultima_pasta = None
lote_atual = []

for img_nome in imagens:
    caminho_img = os.path.join(pasta_imagens, img_nome)
    imagem = cv2.imread(caminho_img)

    # Converter para escala de cinza
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicar OCR
    texto = pytesseract.image_to_string(cinza)
    texto = texto.strip().replace(" ", "").upper()

    if "P-" in texto:
        # Se encontrou pulseira
        numero_pulseira = texto.split("P-")[-1][:5]
        nome_pasta = f'P-{numero_pulseira}'

        if lote_atual:
            destino = os.path.join(pasta_destino, ultima_pasta)
            os.makedirs(destino, exist_ok=True)
            for img in lote_atual:
                shutil.copy2(os.path.join(pasta_imagens, img), os.path.join(destino, img))
            lote_atual = []

        ultima_pasta = nome_pasta
    else:
        lote_atual.append(img_nome)

print("✅ Organização concluída.")
