# https://pypi.org/project/translate/

from translate import Translator

langs = ["ja", "ko", "pt", "zh", "pa"]

# select a language
lang = langs[-1]

translator = Translator(to_lang=lang)

try:
    with open("./test.txt", mode="r", encoding="utf-8") as file1:
        with open(f"./test_{lang}.txt", mode="w", encoding="utf-8") as file2:
            for line in file1.readlines():
                file2.write(translator.translate(line.strip()))
                file2.write("\n")
except FileNotFoundError as err:
    print("File missing!! Check your path!!")


