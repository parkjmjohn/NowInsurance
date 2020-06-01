import PDFConversion.PDFtoText as p

inputDIR = "./inputPDFs/"
outputDIR = "./outputPDFs/"
imagePDF = []
textPDF = []

convertedPDF = p.identifyPDF(inputDIR)
textPDF = convertedPDF[0]
imagePDF = convertedPDF[1]

p.textPDFConversion(textPDF, outputDIR)
p.imagePDFConversion(imagePDF, outputDIR)
