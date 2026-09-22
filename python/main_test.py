from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hello world","status":"success"}
@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id==1:
        return {"user_id":1,"name":"张三"}
    elif user_id==2:
        return {"user_id":2,"name":"李四"}
    else:
        return {"user_id":user_id,"name":"未命名"}