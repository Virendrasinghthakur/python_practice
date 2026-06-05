# Write Web application in A Python To Add Number From List That Are Greater Than 5 And Less Than 10

from fastapi import FastAPI
from typing import List
import uvicorn

app = FastAPI()

@app.get("/sum_numbers")
def sum_numbers(nums: List[int]):
    total = sum(num for num in nums if 5 < num < 10)

    return {
        "numbers": nums,
        "sum": total
    }

if __name__ == "__main__":
    uvicorn.run("p9:app", host="127.0.0.1", port=8000, reload=True)