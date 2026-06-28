
# To MAke PDF Merger 1st install:
#| pip install PYPDF2|
## > https://pypdf2.readthedocs.io/en/3.x/user/merging-pdfs.html

from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
n = int(input("How Many PDF Do You Want To Merge?\n"))

for i in range (0, n):
    name = input(f'Enter the name of the pdf{i+1}:')
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
