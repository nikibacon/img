from PIL import Image

image_file = Image.open("") # open image
image_file = image_file.convert('1') # covert image to black and white
image_file.save('')