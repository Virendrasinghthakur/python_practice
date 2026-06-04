# Write a Web Application to add logout functionality in Django Project


from fastapi import FastAPI
import uvicorn
app=FastAPI()

users={
    "user":"veer2006",
    "password":"1234"
}

log=False
@app.get('/login')
def login(user:str,password:str):
    global log
    if user==users["user"] and users["password"]==password:
        log=True
        return{"succes":"login successfull"}
    return{"error":"invalid user"}

@app.get('/logout')
def logout():
    global log
    if log:
        log=False
        return{"message":"logout successfully"}
    else:
        return{"message":"No user logged in"}
   

if __name__=="__main__":
    uvicorn.run("Wlogout:app",host="127.0.0.1",port=8000,reload=True)