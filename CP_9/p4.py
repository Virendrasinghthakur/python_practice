# Write a Python Program to join two pictures.


from PIL import Image,ImageDraw

img1=Image.open("C:/Users/Asus/Pictures/Camera Roll/WIN_20241225_21_01_23_Pro.jpg")
img2=Image.open("C:/Users/Asus/Pictures/Camera Roll/WIN_20250409_23_40_06_Pro.jpg")


new_width = img1.width + img2.width
new_height = max(img1.height, img2.height)

new_img = Image.new("RGB", (new_width, new_height))

new_img.paste(img1, (0, 0))
new_img.paste(img2, (img1.width, 0))

new_img.show()
# new_img.save("joined.jpg")