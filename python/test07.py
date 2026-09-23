from pydantic import BaseModel
from fastapi import FastAPI
app=FastAPI()
class User(BaseModel):
    username:str
    age:int
@app.post("/register")
def register(user:User):
    return {"message":"注册成功","user":user.username}