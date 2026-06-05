# Write Web application in Python To Find Force Of A Man On A Object Which Have  Mass And Acceleration. Get Mass And Acceleration From User. Display unit with Force as Newton.

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/force/{mass}/{acceleration}")
def force(mass: float, acceleration: float):
    f = mass * acceleration

    return {
        "Mass": f"{mass} kg",
        "Acceleration": f"{acceleration} m/s²",
        "Force": f"{f} Newton"
    }

if __name__ == "__main__":
    uvicorn.run("p7:app", host="127.0.0.1", port=8000, reload=True)