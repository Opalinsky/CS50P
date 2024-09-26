from PIL import Image, ImageFilter

img = Image.open("image.jpg")
img = img.rotate(180)
img = img.filter(ImageFilter.BLUR)
img.save("out.jpg")
