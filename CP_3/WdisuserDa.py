# Create a web application to display fastapi user data in a table.


from fastapi import FastAPI
import uvicorn

app=FastAPI()

dict={
    "name":"veer singh",
    "age":21,
    "number":6398749375,
    "city":"agra"
}

@app.get('/data')
def get_data():
    return {"data":dict}
    


if __name__=="__main__":
    uvicorn.run("WdisuserDa:app",host="127.0.0.1",port=8000,reload=True)
