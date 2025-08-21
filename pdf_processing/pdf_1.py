import pypdf
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pdf_file_path = os.path.join(BASE_DIR, "files/dummy.pdf")
rotated_file_path = os.path.join(BASE_DIR, "files/dummy_rotated.pdf")

print(pdf_file_path)


# with open(pdf_file_path, "rb") as pdf_file:
#     reader = pypdf.PdfReader(pdf_file)

#     print(len(reader.pages))
#     page = reader.pages[0]
#     print(page.extract_text())

# use the reader object to open the Pdf file in read mode
reader = pypdf.PdfReader(pdf_file_path)
print(len(reader.pages))

# to read all pages
for page in reader.pages:
    print(page.extract_text())

writer = pypdf.PdfWriter()
for page in reader.pages:
    writer.add_page(page.rotate(-90))

with open(rotated_file_path, "wb") as rotated_file:
    writer.write(rotated_file)