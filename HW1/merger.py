from PyPDF2 import PdfMerger

# List your PDF files in order
pdfs = ["p1.pdf", "p3.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

# Output merged PDF
merger.write("merged.pdf")
merger.close()

print("PDFs merged successfully into merged.pdf")