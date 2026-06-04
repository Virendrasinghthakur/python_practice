# Write A Python Program To Get Phone Number From User. And System Should Put a ‘-’ After Country And Area Code Automatically on Web

from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.post('/number')
def get_code(num:str):
    new=num[:2]+"-"+num[2:]
    return {"number":new}


if __name__=="__main__":
    uvicorn.run("WcntryCode:app",host="127.0.0.1",port=8000,reload=True)
