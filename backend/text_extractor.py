import glob

import pytesseract
from PIL import Image
# class TextExtractor:
#     def extract_text(img):
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Jeremy\AppData\Local\Tesseract-OCR\tesseract.exe"


for filename in glob.glob("backend/test_photos/*"):
    print(filename)
    image = Image.open(filename)
    text = pytesseract.image_to_string(image)
    print(text)
# text = pytesseract.image_to_string(Image.open(r'C:\Users\Jeremy\Documents\Code\acnh-item-ocr\backend\test_photos\20200625_175157.jpg'))
# print(text)



### Find the most similar item sentence to what the OCR outputs, and we can assume this is the item