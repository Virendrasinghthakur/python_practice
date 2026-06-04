# Write A Web application in Python To Take Age From The User To Check Whether User Able To Participate In Voting Or Not. If Age Is Less Than 18 Then It Don’t Allow To Participation. And Show, After How Much Year a Person Will Be Able To Participate

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/vote/{age}")
def voting(age: int):

    if age >= 18:
        return {
            "Age": age,
            "Status": "Eligible for voting"
        }

    years = 18 - age

    return {
        "Age": age,
        "Status": "Not eligible for voting",
        "Can Vote After": f"{years} year(s)"
    }

if __name__ == "__main__":
    uvicorn.run("p6:app", host="127.0.0.1", port=8000, reload=True)