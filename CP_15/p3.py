# Write A Web application in Python To Get A Number From User, The System Should Add Auto Increment To That Number. Half Of User Entered Number Should Be Incremented.

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/increment/{num}")
def increment(num: int):
    half = num / 2
    result = half + 1

    return {
        "number": num,
        "half": half,
        "incremented_half": result
    }

if __name__ == "__main__":
    uvicorn.run("p3:app", host="127.0.0.1", port=8000, reload=True)