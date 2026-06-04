# Create a web application in python that get 10 product price and display total bill with discount in percentage functionality

from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.post('/data')
def bill(price:list[int]):
    total=sum(price)
    final=total-total*17/100
    return {"total bill is ":f"{total} $",
            "discount":"17%",
            "final bill":final}


if __name__=="__main__":
    uvicorn.run("WproBill:app",host="127.0.0.1",port=8000,reload=True)