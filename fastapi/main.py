from typing import Union

import uvicorn
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World fastapi"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


Instrumentator().instrument(app).expose(app)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8011)
