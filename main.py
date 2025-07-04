from fastapi import FastAPI
import csv

app = FastAPI()

# Carga CSV
database = []
with open('personal.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)  # SIN delimiter, ya que usa comas
    print(f"Columnas detectadas: {reader.fieldnames}")  # Verificación
    for row in reader:
        database.append(row)

@app.get("/buscar")
def buscar_legajo(legajo: str):
    for row in database:
        if row["LEGAJO"].strip() == legajo.strip():
            return {"nombre": row["NOMBRE"]}
    return {"nombre": "No encontrado"}

