# Create  a web application in python to display website different web page like home, contact us, about us etc


from fastapi import FastAPI,HTTPException
import uvicorn
import pandas as pd

app=FastAPI()


@app.get('/home')
def home():
    return {"Message":"welcome to home page"}
@app.get('/About')
def about():
    return {"Message":"I'm a python developer"}
@app.get('/contact')
def contact():
    return {"Message":"6398749375"}


if __name__=="__main__":
    uvicorn.run("WdiffPg:app",host="127.0.0.1",port=8000,reload=True)