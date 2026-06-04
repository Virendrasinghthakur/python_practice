# Write a Python Program to Rotate an image


import cv2

img=cv2.imread("C:/Users/Asus/Pictures/Camera Roll/WIN_20250227_00_00_53_Pro.jpg")

img1=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("blut img",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()