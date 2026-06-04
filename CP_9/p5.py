# Write a Python program to check whether password is strong or weak on WEB.
import re
from fastapi import FastAPI
import uvicorn
app=FastAPI()

@app.get("/pas")
def passws(p:str):
        
    if re.match(r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])",p):
        return {"message":"password is strong"}
    else:
        return {"message":"password is weak"}

if __name__ =="__main__":
    uvicorn.run("p5:app",host="127.0.0.1",port=8000,reload=True,)