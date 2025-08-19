from PIL import Image, ImageFilter

img = Image.open("./Pokedex/pikachu.jpg")

print(img)
print(img.filename)
print(img.format)
print(img.size)
print(img.mode)

# can use different filters like BLUR, CONTOUR, SHARPEN etc
filtered_img = img.filter(ImageFilter.CONTOUR)
# filtered_img.show()
filtered_img.save("./processed/contour.png", "png")


# can convert image to a different color mode
grey_img = img.convert("L")
grey_img.save("./processed/grey.png", "png")

img.close()