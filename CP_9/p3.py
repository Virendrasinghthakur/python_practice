# Write a Python Program to write text on picture

from PIL import Image,ImageDraw

img1=Image.open("C:/Users/Asus/Pictures/Camera Roll/WIN_20241225_21_01_23_Pro.jpg")
img2=Image.open("C:/Users/Asus/Pictures/Camera Roll/WIN_20250409_23_40_06_Pro.jpg")

draw=ImageDraw.Draw(img1)
draw.text((50,50),"hello veer singh",fill="red")
img1.show()
