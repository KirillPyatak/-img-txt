#C:\Program Files\Tesseract-OCR\tesseract.exe"
from PIL import Image
from pytesseract import pytesseract
image = Image.open('123.png')
image = image.resize((1000,1000))
image.save('Аннот.png')
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(image, lang=('rus+eng'))
#печать текста построчно
print(text[:-1])
