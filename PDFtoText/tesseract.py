try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r"../bin/tesseract"
print(pytesseract.image_to_string(Image.open('testPNGs/test2.png')))

# image = Image.open("/Users/mia/Desktop/NowInsurance/textToPDF/sample.png")
#
# image_to_text = pytesseract.image_to_string(image, lang="eng")
#
# print(image_to_text)
