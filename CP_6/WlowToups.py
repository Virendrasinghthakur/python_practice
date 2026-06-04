# Create a Web Application to Get a sentence from user to convert into uppercase. And also display length of sentence, total spaces to user.

from fastapi import FastAPI
import uvicorn
app=FastAPI()

@app.get('/sent')
def sent(s:str):
    s=s.upper()
    sp=0
    for i in range(len(s)):
        if s[i]==" " :
            sp+=1
    return{"Senetece in ups":s,"length":len(s),"total spaces":sp}


if __name__=="__main__":
    uvicorn.run("WlowToups:app",host="127.0.0.1",port=8000,reload=True)