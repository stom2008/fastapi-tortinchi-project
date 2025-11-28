
from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List
from datetime import date, datetime
app = FastAPI()

mevalar = []

def id_generator():
    son = 1
    while True:
        yield son
        son += 1

idgenerator = id_generator()

class Mevalar(BaseModel):
    id: int 
    name: str 
    created_at: date = None


@app.get("/", status_code=status.HTTP_403_FORBIDDEN)
def home(id: str):
    return {"message": f"ok"}

@app.get("/mevalar", response_model =List[Mevalar])
def home():

    return mevalar

@app.post("/mevalar/create")
def home(meva: Mevalar):
    print((meva))
    mevalar.append({
        "id": next(idgenerator),
        "name": meva.name,
        "created_at": meva.created_at
    })
    resp = {
    "message": "success",
    "created_data": meva
    }
    return resp

