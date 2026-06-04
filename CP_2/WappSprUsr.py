# Create  a web application in python to create a super user and view the admin area
from fastapi import FastAPI,HTTPException
import uvicorn
app=FastAPI()

users=[]
@app.get('/')
def home():
    return {"response":"Welcome to home page"}

@app.post("/SPU")
def create_superUser(username:str,password:str):
    user={
        "username":username,
        "password":password,
        "issuper":True
    }

    users.append(user)

    return {"response":"super user created"}

@app.get("/admin")
def get_admin(usern:str):

    for user in users:
        if user["username"]==usern and user["issuper"]:
            return {"response":"welcome to admin section"}
    
    raise HTTPException(status_code=403,detail="Access denied")


if __name__=="__main__":
    uvicorn.run("WappSprUsr:app",host="127.0.0.1",port=8000,reload=True)