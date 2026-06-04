# Write a Python Program to display image using openv
import cv2

img=cv2.imread("C:/Users/Asus/Pictures/Camera Roll/WIN_20250227_00_00_53_Pro.jpg")


cv2.imshow("My Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()