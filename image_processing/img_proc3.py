# use thumbnail method to reduce image size as it preserves aspect ratio
# resize can make images look squished

from PIL import Image

img = Image.open("./astro.jpg")

print(img.size)

img.thumbnail((400, 400))
print(img.size)

img.save("./processed/thumbnail.png", "png")

img.close()