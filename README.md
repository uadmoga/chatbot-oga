# Chatbot Administrativa OGA - Tucumán

Este proyecto contiene un chatbot web que permite a los agentes de la OGA Penal Tucumán registrar solicitudes de licencias de forma automática, rápida y sencilla.

---

## ✅ Funcionalidades
- Chatbot embebido en Google Sites o cualquier página.
- Consulta automática del nombre del agente a partir del número de legajo.
- El chatbot lee directamente un archivo CSV público almacenado en este mismo repositorio (no usa backend).
- 100% Gratis, sin Render ni servidores adicionales.
- Rápido y simple de mantener.

---

## ✅ Cómo funciona
1. El agente ingresa su número de legajo en el chatbot.
2. El chatbot descarga el archivo `personal.csv` directamente desde GitHub.
3. Busca el legajo en el CSV.
4. Muestra el nombre del agente si lo encuentra.
5. Continúa con el flujo de solicitud de licencia.

---

## ✅ Estructura del Proyecto
- `index.html` → Chatbot listo para subir a GitHub Pages o incrustar en Google Sites.
- `personal.csv` → Base de datos con los legajos y nombres de los agentes, separada por comas:
```csv
LEGAJO,APELLIDO,NOMBRE
7170,SALLES,JORGE ALFREDO
7545,ROSSETTI BERIRO,FEDERICO
...
✅ Cómo actualizar la base de personal
Abrir Google Sheets o Excel.

Actualizar la base de personal.

Exportar como CSV (separado por comas, sin comillas).

Subir el nuevo archivo personal.csv a este repositorio.

¡Listo! El chatbot tomará automáticamente la nueva base en la próxima consulta.

✅ URL pública del CSV (utilizada por el chatbot)
plaintext
Copiar
Editar
https://raw.githubusercontent.com/uadmoga/chatbot-oga/refs/heads/main/personal.csv
✅ Ventajas de esta solución
Sin servidores externos ni APIs.

Todo gestionado desde GitHub.

Mantenimiento muy simple.

Accesible solo para quienes tengan acceso al Google Sites (según configuración interna).

✅ Notas adicionales
Este chatbot es ideal para entornos internos y controlados.

No se recomienda para entornos con datos sensibles o con miles de registros (por rendimiento).

Toda la lógica se ejecuta directamente en el navegador del usuario.

✅ Créditos
Desarrollado para la Oficina de Gestión Administrativa Penal - Tucumán.

yaml
Copiar
Editar

---

## ✅ Qué hacer ahora:
1. Copiá el contenido de este README.
2. Creá el archivo `README.md` en tu repo de GitHub.
3. Pegalo y hacé **commit**.

---

Si querés, también puedo prepararte un texto para anunciarle al personal que el chatbot ya está activo. ¿Querés que lo arme?
