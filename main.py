""" A simple products API that uses a list of dictionaries to store data on products. """

from fastapi import FastAPI,HTTPException, status
from typing import Annotated
from pydantic import BaseModel, PositiveInt, PositiveFloat, Field
from datetime import datetime

app = FastAPI()

# Product Model
class Product(BaseModel):
    name: Annotated[str, Field(max_length=100)]
    description: Annotated[str | None, Field(max_length=255)]
    quantity: Annotated[PositiveInt, Field(le=100000)]
    price: Annotated[PositiveFloat, Field(le=1000000)]


# Product example
product_example = Product(
    name="Foo", 
    description="Foo bar", 
    quantity=100, 
    price=100.0
)


# Product dictionary
products = {1: product_example}


# Get all products
@app.get("/products", status_code=status.HTTP_200_OK)
async def get_all_products():
    if not products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No products found."
        )

    return products


# Get a specific product
@app.get("/products/{id}", status_code=status.HTTP_200_OK)
async def get_product(id: int):
    if id not in products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Product {id} not found."
        )

    return products[id]


# Add a product
@app.post("/products", status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    curr_index = list(products.keys())[-1] + 1
    products.update({curr_index: product})
    print(products)

    return {"status": status.HTTP_201_CREATED, "message": f"Product {curr_index} created."}


# Update a specific product
@app.put("/products/{id}", status_code=status.HTTP_200_OK)
async def update_product(product: Product, id: int):
    if id not in products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Product {id} not found."
        )

    products.update({id: product})
    return {"status": status.HTTP_200_OK, "message": f"Product {id} updated."}


# Delete a specific product
@app.delete("/products/{id}", status_code=status.HTTP_200_OK)
async def delete_product(id: int):
    if id not in products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Product {id} not found."
        )

    products.pop(id)
    return {"status": status.HTTP_200_OK, "message": f"Product {id} deleted."}


# Delete all products
@app.delete("/products", status_code=status.HTTP_200_OK)
async def delete_all_products():
    if not products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No products to delete."
        )

    products.clear()
    return {"status": status.HTTP_200_OK, "message": f"All products deleted."}
