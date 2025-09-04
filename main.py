from fastapi import FastAPI

app = FastAPI(title="Task Tracker")

@app.get("/")
def read_root():
    return {"message": "Welcome to Trackle"}

