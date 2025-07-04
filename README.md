# Chatbot Administrativa OGA - Tucumán

Este proyecto contiene un chatbot web que permite a los agentes de la OGA Penal Tucumán registrar solicitudes de licencias de forma automática, rápida y segura.

## ✅ Funcionalidades
- Chatbot embebido en Google Sites.
- Consulta automática del nombre del agente a partir del número de legajo.
- Respuesta ultra rápida mediante API en Python (FastAPI) alojada en Render.com.
- Base de datos local en formato CSV, fácil de actualizar.

---

## ✅ Estructura del proyecto

### 📂 Chatbot (frontend)
- `index.html`  
  Chatbot en HTML, CSS y JavaScript, embebible en Google Sites mediante iframe.

### 📂 Backend (API en Python)
- `main.py`  
  API con FastAPI, consulta el CSV y devuelve el nombre según el legajo.
- `personal.csv`  
  Base de datos de ejemplo con legajos, apellidos y nombres.
- `requirements.txt`  
  Lista de dependencias para Render:



---

## ✅ Cómo funciona el flujo

1. El agente ingresa su legajo en el chatbot.
2. El chatbot hace una petición a la API (`/buscar?legajo=XXXX`).
3. La API busca en `personal.csv` el nombre correspondiente.
4. El chatbot saluda automáticamente al agente con su nombre y continúa el flujo.

---

## ✅ Cómo actualizar la base de datos (personal.csv)
1. Abrir tu Google Sheets con la base de personal.
2. Descargarla como CSV:
3. Reemplazar el archivo `personal.csv` en tu repo de GitHub.
4. Render actualizará automáticamente la app con la nueva base.

---

## ✅ Cómo desplegar el backend en Render.com
1. Crear una cuenta en [https://render.com](https://render.com).
2. Crear un **Web Service** conectando tu repositorio de GitHub.
3. Configurar:
- **Build Command:**  
  ```
  pip install -r requirements.txt
  ```
- **Start Command:**  
  ```
  uvicorn main:app --host 0.0.0.0 --port 10000
  ```
4. Render asignará una URL pública a tu API.

---

## ✅ Cómo integrar el chatbot en Google Sites
1. Subir el archivo `index.html` a GitHub Pages (o cualquier hosting que permita HTML).
2. Obtener la URL pública del chatbot.
3. Incrustarlo en Google Sites mediante **Insertar → Incrustar → URL**.

---

## ✅ Notas adicionales
- Este sistema es muy rápido y no requiere bases de datos externas ni costos.
- Si necesitás más seguridad, podés agregar autenticación en la API.
- La base CSV se mantiene en memoria, por lo que es muy eficiente para bases medianas.

---

## ✅ Créditos
Desarrollado por el equipo administrativo de OGA Penal Tucumán con la colaboración de herramientas open-source.
