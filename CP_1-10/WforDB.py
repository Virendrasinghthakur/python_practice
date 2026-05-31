# Create a web application in python to create a database table for student to store student information.
from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.get("/") 
def home():
    return {"message":"welcome to the home page"}

@app.post('/save')
def data(roll_no:int,name:str,year:int,branch:str):
    db={
        "roll_no":roll_no,
        "Name":name,
        "year":year,
        "branch":branch
        }
    return {"message":"data saved successfully"}
    
    print(db)



if __name__ == "__main__":
    uvicorn.run("WforDB:app",host="127.0.0.1",port=8000,reload=True)