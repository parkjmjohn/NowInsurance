import io
from PIL import Image
import pytesseract
from wand.image import Image as wi

pdfFile = wi(filename = "inputPDFs/test7.pdf", resolution = 300)
image = pdfFile.convert('jpeg')

imageBlobs = []

for img in image.sequence:
    imgPage = wi(image = img)
    imageBlobs.append(imgPage.make_blob('jpeg'))


filename = str(pdfFile)[:-4] + ".txt"
file = open(filename,"w")

for imgBlob in imageBlobs:
    image = Image.open(io.BytesIO(imgBlob))
    text = pytesseract.image_to_string(image, lang = 'eng')
    file.write(text)

file.close
