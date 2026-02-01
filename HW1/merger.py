from PyPDF2 import PdfMerger
import os

# Folder where your PDFs are stored
pdf_folder = "pdfs"

# List your PDF files in order (relative to the pdf_folder)
pdfs = ["p1.pdf", "p2.pdf", "p3.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    # Join folder path and file name
    pdf_path = os.path.join(pdf_folder, pdf)
    merger.append(pdf_path)

# Output merged PDF
output_path = os.path.join(pdf_folder, "merged.pdf")
merger.write(output_path)
merger.close()

print(f"PDFs merged successfully into {output_path}")
