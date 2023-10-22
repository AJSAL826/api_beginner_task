from fastapi import FastAPI
from pydantic import BaseModel

from typing import Optional

#declaring a model for request
class Product(BaseModel):
    name : str
    model : Optional[str]
    Price : int



app=FastAPI()



#declaring a Post variable
@app.post("/item")
def item(product:Product):
    return {"Data":f"the product detail is {product.name} and {product.Price}"}
    




@app.get("/books")

def hello(limit=10 , published:bool=False ,sort: Optional[str]= None):
    if published:
        return f'the {limit} books are arranged in {sort}'
    else:
        return f'no available books'
    


@app.get("/blog/published")
def published():
    return "published book is potter"


@app.get("/begun")
def begin():
    return {"name":"haris"}

@app.get("/{id}/det")

def begin(id: int):
    return{ "Data":{id," is an employee"}}


