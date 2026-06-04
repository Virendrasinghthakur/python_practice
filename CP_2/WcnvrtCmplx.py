# Write A Python Program To Get A Integer Number From User To Convert Into Complex on Web
from fastapi import FastAPI,HTTPException
import uvicorn

app=FastAPI()


@app.post('/cal')
def calulate(n:int):
    n=complex(n)
    return {"response":f" your number is {n}"}


if __name__=="__main__":
    uvicorn.run("WcnvrtCmplx:app",host="127.0.0.1",port=8000,reload=True)

