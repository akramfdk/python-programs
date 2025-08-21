import pypdf
import os
import sys

script_pdf = sys.argv[1]
watermark_pdf = sys.argv[2]


def watermark(script_pdf, watermark_pdf):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(BASE_DIR, f"files/{script_pdf}")
    watermark_path = os.path.join(BASE_DIR, f"files/{watermark_pdf}")
    output_path = os.path.join(BASE_DIR, "files/watermarked.pdf")

    # print(script_path)
    # print(watermark_path)

    writer = pypdf.PdfWriter()

    watermark_reader = pypdf.PdfReader(watermark_path)
    watermark = watermark_reader.pages[0]

    script_reader = pypdf.PdfReader(script_path)
    for page in script_reader.pages:
        page.merge_page(watermark)
        writer.add_page(page)

    writer.write(output_path)

watermark(script_pdf, watermark_pdf)
