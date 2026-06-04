# Write a Python Program to Blur an image


import cv2

img=cv2.imread("C:/Users/Asus/Pictures/Camera Roll/WIN_20250227_00_00_53_Pro.jpg")

img1=cv2.blur(img,(5,5))
cv2.imshow("blut img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(img.shape)
