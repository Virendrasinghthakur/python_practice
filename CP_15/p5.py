# Write a Web application in Python To Find Acceleration Of An Object Having Velocity (v) in (t) Time. Display unit with Acceleration as m/s2

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/acceleration/{v}/{t}")
def acceleration(v: float, t: float):
    a = v / t

    return {
        "velocity": f"{v} m/s",
        "time": f"{t} s",
        "acceleration": f"{a} m/s²"
    }

if __name__ == "__main__":
    uvicorn.run("p12:app", host="127.0.0.1", port=8000, reload=True)