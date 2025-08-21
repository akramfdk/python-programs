import pypdf
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pdf1_path = os.path.join(BASE_DIR, "files/twopage.pdf")
pdf2_path = os.path.join(BASE_DIR, "files/dummy.pdf")
merged_pdf_path = os.path.join(BASE_DIR, "files/merged_pdf.pdf")

# print(pdf1_path)
# print(pdf2_path)

def merge_pdfs(pdfs, output_file_path):
    writer = pypdf.PdfWriter()

    for pdf in pdfs:
        writer.append(pdf)

    with open(output_file_path, "wb") as output_file:
        writer.write(output_file)


merge_pdfs([pdf1_path, pdf2_path], merged_pdf_path)
