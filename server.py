from fastapi import FastAPI

from models.my_model import MyModel
from models.body_model import BodyModel

app = FastAPI()

@app.get("/")
# @app.get("/", response_mode=ModelHere)
async def root():
    return {"message": "Hello World"}

@app.get("/other", response_model=MyModel)
# @app.get("/", response_mode=ModelHere)
async def other_endpoint():
    return MyModel(**{
      "id": "dsfzdfg",
      "name": "hello world"
    })

@app.post("/other")
# @app.get("/", response_mode=ModelHere)
async def other_endpoint(body: BodyModel):
    return body