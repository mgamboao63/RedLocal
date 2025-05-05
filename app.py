from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECCIONES = {
    "logica": "Lógica y Fundamentos de Matemáticas",
    "estadistica": "Probabilidad y Estadística",
    "investigacion": "Fundamentos de Investigación",
    "COE": "Comunicación Oral y Escrita"
}

@app.route("/")
def index():
    archivos_por_seccion = {}
    for carpeta, nombre in SECCIONES.items():
        ruta = os.path.join(BASE_DIR, carpeta)
        if os.path.isdir(ruta):
            archivos = [f for f in os.listdir(ruta) if f.endswith(".pdf")]
            archivos_por_seccion[carpeta] = archivos
    return render_template("index.html", secciones=SECCIONES, archivos=archivos_por_seccion)

@app.route("/<seccion>/<archivo>")
def descargar(seccion, archivo):
    return send_from_directory(os.path.join(BASE_DIR, seccion), archivo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

