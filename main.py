from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

# Configurar CORS para permitir solo tu dominio de GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://uadmoga.github.io"],  # Solo tu GitHub Pages
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar el CSV
database = []
with open('personal.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    print(f"Columnas detectadas: {reader.fieldnames}")  # Debug en logs
    for row in reader:
        database.append(row)

@app.get("/buscar")
def buscar_legajo(legajo: str):
    for row in database:
        if row["LEGAJO"].strip() == legajo.strip():
            return {"nombre": row["NOMBRE"]}
    return {"nombre": "No encontrado"}




