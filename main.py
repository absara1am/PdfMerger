#pip install pypdf
from pypdf import PdfMerger, PdfWriter

pdfs = ['file1.pdf', 'file2.pdf']

merger = PdfWriter()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()