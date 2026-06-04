# Write a Web Application Python Program to get 5 number from user, store in a list, convert to pandas series to change their default index numbers to alpha.

from fastapi import FastAPI,HTTPException
import uvicorn
import pandas as pd

app=FastAPI()


@app.post('/cal')

def calulate(n:list[int]):
    if len(n)!=5:
        return {"error":"PLease enter only 5 number"}
    s=pd.Series(n,index=['a','b','c','d','e'])
    return s.to_dict()


if __name__=="__main__":
    uvicorn.run("WchngIdx:app",host="127.0.0.1",port=8000,reload=True)