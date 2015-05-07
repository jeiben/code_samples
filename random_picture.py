from random import randint
from PIL import Image

num = randint(1,3)

path = "pictures/"

if num == 1:
	path += "cartoon1.jpg"
elif num == 2:
	path += "cartoon2.jpg"
else:
	path += "cartoon3.jpg"

img = Image.open(path)
img.show()