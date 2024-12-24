from fastapi import FastAPI

app = FastAPI()


# Ruta raíz
@app.get("/")
def read_root():
    return {"message": "¡Hola, FastAPI!"}


# Ruta con parámetros
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# Ruta para crear un recurso
@app.post("/items/")
def create_item(item: dict):
    return {"message": "Item creado", "item": item}
