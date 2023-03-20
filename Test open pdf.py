#C:\Program Files\Tesseract-OCR\tesseract.exe"
from PIL import Image
from pytesseract import pytesseract
image = Image.open('Аннотация 2023-03-20 155434.png')
image = image.resize((400,200))
image.save('Аннот.png')
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(image, lang='rus')
#печать текста построчно
print(text[:-1])
