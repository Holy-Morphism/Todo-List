from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to Basic Fastapi app"}


@app.get("/help")
def help():
    return {"message": "Please call 1122"}
