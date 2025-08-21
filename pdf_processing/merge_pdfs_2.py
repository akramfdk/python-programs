import pypdf
import sys
import os

inputs = sys.argv[1:]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
files_dir_path = os.path.join(BASE_DIR, "files")
merged_path = os.path.join(files_dir_path, "merged.pdf")

print(files_dir_path)

def pdf_merger(pdf_list):
    merger = pypdf.PdfWriter()
    for pdf in pdf_list:
        # print(os.path.join(files_dir_path, pdf))
        merger.append(os.path.join(files_dir_path, pdf))

    merger.write(merged_path)

pdf_merger(inputs)
