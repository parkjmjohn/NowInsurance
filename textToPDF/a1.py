import os, shutil, pdftotext

inputDIR = "/Users/mia/Desktop/NowInsurance/textToPDF/inputPDFs"
outputDIR = "/Users/mia/Desktop/NowInsurance/textToPDF/outputPDFs"

# count = 0
for pdfFile in os.listdir(inputDIR):
    # count += 1
    # print(f'interation {count}')
    filename = str(pdfFile)[:-4] + ".txt"
    file = open(filename,"w")
    with open(inputDIR + "/" + pdfFile, "rb") as f:
        pdf = pdftotext.PDF(f)
    # print("Total number of pages: " + str(len(pdf)))
    for page in pdf:
        file.write(str(page))

    file.close
    shutil.move(filename, outputDIR)
