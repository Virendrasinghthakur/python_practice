# Write a Web application in Python to find union and intersection of two set. A = {3,2,4,5,6,7,8} B = {4,12,5,1,6,8}

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/sets")
def set_operations():
    A = {3, 2, 4, 5, 6, 7, 8}
    B = {4, 12, 5, 1, 6, 8}

    union_set = list(A.union(B))
    intersection_set = list(A.intersection(B))

    return {
        "A": list(A),
        "B": list(B),
        "Union": union_set,
        "Intersection": intersection_set
    }

if __name__ == "__main__":
    uvicorn.run("p7:app", host="127.0.0.1", port=8000, reload=True)