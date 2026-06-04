# Write a Web Application to register a user on Django.


from fastapi import FastAPI
import uvicorn
app=FastAPI()

users={
    "user":"veer2006",
    "password":"1234"
}

@app.post('/register')
def register(user:str,password:str):
    if user!=users["user"]:
        users[user]=password
        return{"succes":"user created"}
    return{"error":"invalid user alredy exists"}


if __name__=="__main__":
    uvicorn.run("WregisterUsr:app",host="127.0.0.1",port=8000,reload=True)