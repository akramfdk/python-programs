# this app takes in two argumemts
# 1. name of folder containing the jpg files
# 2. name of new folder that will contain the pngs
# this new folder is created in the folder containing jpgs

# this
# python jpg_to_png_converter_1.py Pokedex New

import os
import sys
from PIL import Image

current_folder = sys.argv[1]
new_folder = sys.argv[2]

current_folder_path = os.path.join("./", current_folder)
new_folder_path = os.path.join(current_folder_path, new_folder)

# print(current_folder_path)
# print(new_folder_path)

if os.path.exists(current_folder):

    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    for filename in os.listdir(current_folder_path):
        filepath = os.path.join(current_folder, filename)


        if os.path.isfile(filepath):
            img = Image.open(filepath)

            new_filename = filename.split(".")[0] + ".png"
            new_filepath = os.path.join(new_folder_path, filename)

            # print(new_filename)
            # print(new_filepath)

            img.save(new_filepath, "png")

            img.close()
else:
    print(f"{current_folder} does not exist!!")
