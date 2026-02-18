#this whole thing was about path parametets in fastapi

'''from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}'''

'''from fastapi import FastAPI
from enum import Enum

app=FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path:str):
    return {"file_path":file_path}'''

#now this whole code would be about the query parameters
#this specfic section of the code performs optional query parameters operations
'''from fastapi import FastAPI
from enum import Enum

app=FastAPI()

@app.get("/items/")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}'''

#now since we have already done the basic query parameters operations we would perform a basic type conversion around it.
'''from fastapi import FastAPI

app=FastAPI()

@app.get("/items/")
async def read_item(item_id:str, q:str|None= None,short:bool=False):#now this shows that we can declare bool types in the qurey parameter
    item ={"item_id ": item_id} 
    if q:
        item.update({"q":q})
    if not short:
        item.update(
           { "description":"this contains originally a very long description which may lead to an error"
        })
        return item'''

# with the above examples we are done with simply designing the api now we will learn sending request and response body
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    description:str|None=None
    price:float
    tax:float | None = None

app= FastAPI()
@app.post("/items/")
async def create_item(item:Item):
    item_dict=item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax":price_with_tax})
    return item_dict





