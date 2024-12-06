from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the API"}


@app.get("/ping")
def index():
    return {"response":"ping"}