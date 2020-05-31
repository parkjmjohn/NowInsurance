import PDFtoText as p

inputDIR = "./inputPDFs/"
outputDIR = "./outputPDFs/"
imagePDFs = []
textPDFs = []

x = p.identifyPDF(inputDIR)
textPDFs = x[0]
imagePDFs = x[1]

p.textPDFConversion(textPDFs, outputDIR)
