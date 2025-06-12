📄 README.md

# PEC4 - Programación para la Ciencia de Datos  
**Abdullah Fasih – UOC 2025**

Este proyecto corresponde a la PEC4 de la asignatura *Programación para la Ciencia de Datos*, del Grado en Ciencia de Datos Aplicada en la UOC.  
Consiste en el diseño modular, documentado y testeado de un flujo de trabajo para el análisis de datos relacionados con sequías.

---

## 📥 Clonar el repositorio

Puedes clonar o descargar el proyecto desde GitHub:

🔗 [https://github.com/SocAbdul/pec4_baells](https://github.com/SocAbdul/pec4_baells)

```bash
git clone https://github.com/SocAbdul/pec4_baells.git
cd pec4_baells
📁 Estructura del proyecto

.
├── data/                     # Datos fuente (ej: baells.csv)
├── doc/                      # Documentación HTML generada con pdoc
│   ├── index.html
│   ├── exercises.html
│   ├── src.html
│   └── logo2.png
├── eda/                      # Funciones para análisis exploratorio
│   ├── cleaning.py
│   ├── loader.py
│   └── utils.py
├── img/                      # Imágenes generadas (visualizaciones)
│   ├── labaells_abdullah_fasih.png
│   └── labaells_smoothed_abdullah_fasih.png
├── screenshots/              # Evidencias de testing y cobertura
│   ├── coverage_report.png
│   └── test_ejecuccion.png
├── src/                      # Código principal
│   └── exercises/            # Ejercicios por fases
│       ├── ex1_exploracion.py
│       ├── ex2_limpieza.py
│       ├── ex3_procesamiento.py
│       ├── ex4_suavizado.py
│       ├── ex5_sequias.py
│       └── __init__.py
├── tests/                    # Pruebas unitarias
│   ├── test_loader.py
│   └── __init__.py
├── visuals/                  # Visualizaciones (ej. plot.py)
│   └── plot.py
├── LICENSE
├── main.py                   # Script principal ejecutable
├── README.md                 # Este archivo
└── requirements.txt          # Dependencias del proyecto
▶️ Ejecución
Desde la raíz del proyecto:

```bash
python main.py
Este script carga, limpia, suaviza y visualiza los datos del embalse de Baells.

🧪 Tests
Los tests están definidos en tests/test_loader.py y se ejecutan con:

```bash
python -m unittest discover
La cobertura de código se ha verificado con coverage y se encuentra en la carpeta screenshots/.

🧾 Documentación
La documentación se ha generado con pdoc a partir de los docstrings.
Se encuentra en la carpeta doc/ y puede abrirse directamente en el navegador mediante doc/index.html.

✅ Requisitos
Instalar dependencias:

```bash
pip install -r requirements.txt
👨‍💻 Autor
Abdullah Fasih
Universitat Oberta de Catalunya (UOC) – 2025