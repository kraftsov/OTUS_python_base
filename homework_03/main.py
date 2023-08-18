from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Status(BaseModel):
    message: str = "ok"


@app.get("/ping/")
def ping():
    return {"message": "pong"}


@app.get("/status/")
def get_status():
    return Status()
