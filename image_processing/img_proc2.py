from PIL import Image

img = Image.open("./Pokedex/pikachu.jpg")

# rotate image
img_90 = img.rotate(90)
img_180 = img.rotate(180)

img_90.save("./processed/rotate_90.png", "png")
img_180.save("./processed/rotate_180.png", "png")


# get image size
image_size = img.size
print(image_size)

# resize image
# notice it takes a tuple
reduced_size = img.resize((200, 200))
reduced_size.save("./processed/smaller.png", "png")


# get image box
image_box = img.getbbox()
print(image_box)

# crop the image, pass the box (left, upper, right, lower)
crop_box = (100, 100, 400, 400)
cropped = img.crop(crop_box)
cropped.save("./processed/cropped.png", "png")

img.close()