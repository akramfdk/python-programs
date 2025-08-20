# execute the file with arguments as follows:
# python jpg_to_png_converter.py Pokedex/ new/

import sys
import os
from PIL import Image


# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# print(image_folder, output_folder)

# print(os.path.exists(image_folder))
# print(os.path.exists(output_folder))

# check if new/ exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


for filename in os.listdir(image_folder):
    filepath = f"{image_folder}{filename}"
    if os.path.isfile(filepath):
        img = Image.open(filepath)
        # filename = filename.split(".")[0]+".png"
        clean_name = os.path.splitext(filename)[0]
        # print(f"{output_folder}{clean_name}.png")
        img.save(f"{output_folder}{clean_name}.png", "png")