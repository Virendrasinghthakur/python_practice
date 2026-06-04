# Write a Python Program to blur an image on web

from fastapi import FastAPI
from fastapi.responses import FileResponse
import cv2
import uvicorn

app = FastAPI()

@app.get("/blur")
def blur_image():

    img=cv2.imread("C:/Users/Asus/Pictures/Camera Roll/WIN_20250227_00_00_53_Pro.jpg")

    blur = cv2.GaussianBlur(img, (15, 15), 0)

    cv2.imwrite("blurred.jpg", blur)

    return FileResponse(
        "blurred.jpg",
        media_type="image/jpeg",
        filename="blurred.jpg"
    )

if __name__ == "__main__":
    uvicorn.run(
        "blrImgWeb:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )