# Proyecto: Análisis histórico del embalse de La Baells

Este proyecto consiste en la exploración, limpieza, análisis y visualización de datos del embalse de La Baells. Utiliza técnicas de procesamiento de series temporales y suavizado para detectar periodos de sequía a lo largo de más de 20 años.

## 📁 Estructura del proyecto

pec4_baells/
│
├── data/ # Contiene el archivo CSV original (baells.csv)
├── eda/ # Funciones auxiliares para análisis de datos
│ └── utils.py
├── visuals/ # Funciones de visualización
│ └── plot.py
├── img/ # Carpeta donde se guardan las imágenes generadas
├── main.py # Script principal de ejecución
├── README.md # Este archivo
├── LICENSE # Licencia de uso
└── requirements.txt # Dependencias del proyecto


## ⚙️ Instalación y ejecución

1. Clona el repositorio o descarga el código.
2. Asegúrate de tener Python 3.10 o superior instalado.
3. Instala las dependencias con:

```bash
pip install -r requirements.txt
Ejecuta el proyecto con:

python main.py
🧪 Cómo ejecutar los tests
Este proyecto no incluye tests automatizados, pero puedes probar el correcto funcionamiento ejecutando el script principal (main.py). En caso de usar pytest, puedes organizar los tests en una carpeta tests/.

📚 Documentación
Actualmente no se genera documentación automática, pero puedes comentarla o extenderla con herramientas como pdoc, Sphinx, etc.