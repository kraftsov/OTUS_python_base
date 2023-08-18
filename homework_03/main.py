import fastapi
import pydantic

app = fastapi.FastAPI()


class Status(pydantic.BaseModel):
    message: str = "ok"


@app.get("/")
def status():
    status = Status()
    return status

@app.get("/ping/")
def ping():
    return {"message": "pong"}

