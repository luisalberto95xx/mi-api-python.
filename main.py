from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def leer_raiz():
    return {"status_code": 0, "mensaje": "Mi API en Python está viva"}