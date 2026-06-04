# Write a Web Application to add login functionality in Django Application.

from fastapi import FastAPI
import uvicorn
app=FastAPI()

users={
    "user":"veer2006",
    "password":"1234"
}

@app.get('/login')
def login(user:str,password:str):
    if user==users["user"] and users["password"]==password:
        return{"succes":"login successfull"}
    return{"error":"invalid user"}


if __name__=="__main__":
    uvicorn.run("Wlogin:app",host="127.0.0.1",port=8000,reload=True)