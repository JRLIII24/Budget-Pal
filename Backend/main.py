from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def read_root():
    """
    Returns a simple welcome message for the root endpoint.
    """
    return {"message": "Welcome to your Budget Application Backend!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Returns an item ID. Demonstrates path parameters and type hints.
    """
    return {"item_id": item_id, "description": f"This is item number {item_id}"}
