from PyPDF2 import PdfWriter, PdfReader
from getpass import getpass


pdfwriter = PdfWriter()
pdf = PdfReader("Python 3 by Spahic Benjamin.pdf")

for page in range(len(pdf.pages)):
    pdfwriter.add_page(pdf.pages[page])


password = getpass(prompt="Enter the password: ")
pdfwriter.encrypt(password)

with open("protected.pdf", "wb") as file:
    pdfwriter.write(file)

