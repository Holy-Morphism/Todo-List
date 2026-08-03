from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "The OG To-Do List"}


@app.get("/help")
def help():
    return {"message": "Please call 1122"}
