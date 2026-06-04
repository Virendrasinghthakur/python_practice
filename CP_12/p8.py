# Write a Web application in Python to calculate difference and symmetric difference of two. A = {3,2,4,5,6,7,8} B = {4,12,5,1,6,8}

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/setops")
def set_operations():

    A = {3, 2, 4, 5, 6, 7, 8}
    B = {4, 12, 5, 1, 6, 8}

    difference = A.difference(B)
    symmetric_difference = A.symmetric_difference(B)

    return {
        "A": list(A),
        "B": list(B),
        "Difference (A-B)": list(difference),
        "Symmetric Difference": list(symmetric_difference)
    }

if __name__ == "__main__":
    uvicorn.run("p8:app", host="127.0.0.1", port=8000, reload=True)