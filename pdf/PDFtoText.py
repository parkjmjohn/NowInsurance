import io, os, shutil, pdftotext, pytesseract
from PIL import Image
from wand.image import Image as wi


'''
function: identifyPDF
parameters: path
output:
requirements:
'''
def identifyPDF(path):
    textPDFs = []
    imagePDFs = []
    for pdf in os.listdir(path):
        fontRet = os.popen('pdffonts ' + path + str(pdf)).read()
        if fontRet.count('\n') > 2:
            textPDFs.append(path + str(pdf))
        else:
            imagePDFs.append(path + str(pdf))
    return textPDFs, imagePDFs


'''
function: checkScanned
parameters:
output: return if the PDF was scanned
requirements:
'''
def checkScanned():
    return 0


'''
function: textPDFConversion
parameters: textPDF, path
output:
requirements:
'''
def textPDFConversion(textPDF, path):
    # count = 0
    for pdf in textPDF:
        # count += 1
        # print(f'interation {count}, working with PDF {pdf}')
        charIndex = str(pdf).rfind("/") + 1
        filename = str(pdf)[charIndex:-4] + ".txt"
        file = open(filename,"w")
        with open(pdf, "rb") as f:
            pdf = pdftotext.PDF(f)
        # print("Total number of pages: " + str(len(pdf)))
        try:
            for page in pdf:
                file.write(str(page))
                # print(f'pageType {type(page)}, pdf {pdf}, pdfType {type(pdf)}')
            print(f'interation {count}, no error')
        except UnicodeEncodeError:
            print(f'interation {count}, enter UnicodeEncodeError')
        except:
            print("\n\n\n Undefined Error \n\n\n")
        file.close
        shutil.move(filename, path)


'''
function: imagePDFConversion
parameters: pdf
output:
requirements:
'''
def imagePDFConversion(path, pdf):
    pdfImage = wi(filename = pdf, resolution = 300)
    image = pdfImage.convert('jpeg')
    imageBlobs = []
    for img in image.sequence:
        imgPage = wi(image = img)
        imageBlobs.append(imgPage.make_blob('jpeg'))
    charIndex = str(pdf).rfind("/") + 1
    filename = pdf[charIndex:-4] + "V2.txt"
    file = open(filename,"w")
    for imgBlob in imageBlobs:
        image = Image.open(io.BytesIO(imgBlob))
        text = pytesseract.image_to_string(image, lang = 'eng')
        file.write(text)
    file.close
    shutil.move(filename, path)