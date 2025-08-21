# https://pypi.org/project/translate/

from translate import Translator
import os

langs = ["ja", "ko", "pt", "zh", "pa"]

# select a language
lang = langs[-1]

translator = Translator(to_lang=lang)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(BASE_DIR, "test.txt")
output_file = os.path.join(BASE_DIR, f"test_{lang}.txt")

try:
    with open(input_file, mode="r", encoding="utf-8") as file1:
        with open(output_file, mode="w", encoding="utf-8") as file2:
            for line in file1.readlines():
                file2.write(translator.translate(line.strip()))
                file2.write("\n")
except FileNotFoundError as err:
    print("File missing!! Check your path!!")


