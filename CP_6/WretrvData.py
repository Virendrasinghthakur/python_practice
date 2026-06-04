# Write a Web Application to retrieve data from database table and display to user.



from fastapi import FastAPI
import uvicorn
app=FastAPI()

users={
    "message":"hii how are you"
}

@app.get('/show')
def show():
   
    return{"success":users["message"]}

if __name__=="__main__":
    uvicorn.run("WretrvData:app",host="127.0.0.1",port=8000,reload=True)