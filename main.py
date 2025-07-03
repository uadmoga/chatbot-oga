from fastapi import FastAPI
import csv

app = FastAPI()

# Cargamos el CSV en memoria al iniciar la app (muy rápido)
database = []
with open('personal.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        database.append(row)

@app.get("/buscar")
def buscar_legajo(legajo: str):
    for row in database:
        if row["Legajo"] == legajo:
            return {"nombre": row["Nombre"]}
    return {"nombre": "No encontrado"}
