# Write A Python Program To Store 5 Subjects Marks Of Student And Also Store Their Total, Average And Percentage on Web

from fastapi import FastAPI,HTTPException
import uvicorn
app=FastAPI()
st={
    "virendra":{
        "marks":[68,98,74,36,85],
        "total":425,
        "avg":65,
        "percent":67
    }
}

@app.post('/data')
def save(name:str,d:list[int]):
    total=sum(d)
    st[name]={
        "marks":d,
        "total":total,
        "avg":total/5,
        "percent":f"{total/5:.2f}%"
    }
    return {"response":"data saved successfully"}
@app.get('/load')
def load(name:str):
    if not name in st.keys():
        return {"message ":"student not found"}
    data=st[name]
    return {"data":data}



if __name__=="__main__":
    uvicorn.run("WstoreStd:app",host="127.0.0.1",port=8000,reload=True)

