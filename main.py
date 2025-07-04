from fastapi import FastAPI
import csv

app = FastAPI()

# Cargar CSV
database = []
with open('personal.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    print(f"Columnas detectadas: {reader.fieldnames}")  # Para verificar las columnas
    for row in reader:
        database.append(row)

@app.get("/buscar")
def buscar_legajo(legajo: str):
    for row in database:
        if row["LEGAJO"].strip() == legajo.strip():
            return {"nombre": row["NOMBRE"]}
    return {"nombre": "No encontrado"}


