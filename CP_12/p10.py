#Write A Web application in Python To Take Age and Marks From User To Check Whether User Able To Get admission Or Not. Criteria: Age should be greater than 20 or less than or equal to 25 Marks should be greater than 60 or less than or equal to 100.

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/admission/{age}/{marks}")
def admission(age: int, marks: float):

    if 20 < age <= 25 and 60 < marks <= 100:
        return {
            "Age": age,
            "Marks": marks,
            "Status": "Admission Granted"
        }

    return {
        "Age": age,
        "Marks": marks,
        "Status": "Admission Denied"
    }

if __name__ == "__main__":
    uvicorn.run("p6:app", host="127.0.0.1", port=8000, reload=True)