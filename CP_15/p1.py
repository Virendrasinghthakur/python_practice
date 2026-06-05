# Write a Web Application in Python To Get 2 Number From The User, Find Their Square, And Add Both Result, Finally Find Cube Of Result And Display To User.


from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/calculate/{n1}/{n2}")
def calculate(n1: int, n2: int):
    square1 = n1 ** 2
    square2 = n2 ** 2

    addition = square1 + square2
    cube_result = addition ** 3

    return {
        "Number1": n1,
        "Number2": n2,
        "Square1": square1,
        "Square2": square2,
        "Addition": addition,
        "Final Cube": cube_result
    }

if __name__ == "__main__":
    uvicorn.run("p1:app", host="127.0.0.1", port=8000, reload=True)