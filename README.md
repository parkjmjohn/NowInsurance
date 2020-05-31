# NowInsurance

## Keywords
automated data entry; machine learning; optical character recognition; text mining; natural language processing;

## Project Flow
1. convert mixed media PDFs to text-only PDFs
2. transform text-only PDFS to XML
3. extract information from XML

## Modules

#### PDF to Text files Process
**PDFtoText.py** handles this process. First, the code check if the PDFs are text-based or image-based. If the PDF is text-based, the python library _pdftotext_ handles this well. If the PDF is imaged, the python library _wand_ converts the PDF to JPEGs and _pytesseract_ uses an optic character recognition model to convert the JPEGs to text.

To run this process, run the following command:
'''
cd ./PDFtoText ; python3 os.py
'''

#### NLP research
#### NLP Model
#### Performance Analysis

## Python3 Libraries
- os
- shutil
- pdftotext
- pytesseract
- wand

## Similar Projects
- MagicBot by SlickPie
- GROBID

### PDF -> Text Projects
- Freek.dev
