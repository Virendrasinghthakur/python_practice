# Create a web application in python to make percentage calculator and design with CSS coding

from fastapi import FastAPI
import uvicorn
app=FastAPI()

@app.get("/home")
def hello():
    return {"response":"hello world"}

if __name__=="__main__":
    uvicorn.run("p6:app",host="127.0.0.1",port=8000,reload=True)