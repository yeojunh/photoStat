import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\yeoju\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image 

# process image to text given path 
def imgToText(imgPath): 
    img = Image.open(imgPath)
    text = tess.image_to_string(img)
    return text

print(imgToText('data/img/test.jpg'))
print(imgToText('data/img/test2.jpg'))