import io, os, shutil, pdftotext, pytesseract
from PIL import Image
from wand.image import Image as wi

inputDIR = "./inputPDFs"
outputDIR = "./outputPDFs"

def textPDFConversion():
    count = 0
    for pdfFile in os.listdir(inputDIR):
        count += 1
        print(f'interation {count}, working with PDF {pdfFile}')
        filename = str(pdfFile)[:-4] + ".txt"
        file = open(filename,"w")
        with open(inputDIR + "/" + pdfFile, "rb") as f:
            pdf = pdftotext.PDF(f)
        # print("Total number of pages: " + str(len(pdf)))
        try:
            for page in pdf:
                file.write(str(page))
                print(f'pageType {type(page)}, pdf {pdf}, pdfType {type(pdf)}')
            print(f'interation {count}, no error')
        except UnicodeEncodeError:
            print(f'interation {count}, enter UnicodeEncodeError')
        except:
            print("\n\n\n Undefined Error \n\n\n")
        file.close
        shutil.move(filename, outputDIR)

def imagePDFConversion(f):
    pdfFile = wi(filename = f, resolution = 300)
    image = pdfFile.convert('jpeg')
    imageBlobs = []
    for img in image.sequence:
        imgPage = wi(image = img)
        imageBlobs.append(imgPage.make_blob('jpeg'))
    filename = f[:-4] + "V2.txt"
    file = open(filename,"w")
    for imgBlob in imageBlobs:
        image = Image.open(io.BytesIO(imgBlob))
        text = pytesseract.image_to_string(image, lang = 'eng')
        file.write(text)
    file.close
    shutil.move(filename, outputDIR)

textPDFConversion()
imagePDFConversion("./inputPDFs/test4.pdf")
imagePDFConversion("./inputPDFs/test7.pdf")
