# PEC4 - Programación para la Ciencia de Datos
**Abdullah Fasih – UOC 2025**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)

Este repositorio contiene el proyecto para la Práctica de Evaluación Continua (PEC4) de la asignatura *Programación para la Ciencia de Datos*. El objetivo es diseñar, documentar y testear un flujo de trabajo modular para analizar datos sobre la sequía, utilizando como caso de estudio el embalse de La Baells.

---

## 🚀 Primeros Pasos

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

### 1. Clonar el repositorio

Primero, clona el repositorio desde GitHub y navega al directorio del proyecto.

```bash
git clone [https://github.com/SocAbdul/pec4_baells.git](https://github.com/SocAbdul/pec4_baells.git)
cd pec4_baells
2. Crear un entorno virtual (Recomendado)
Es una buena práctica aislar las dependencias del proyecto en un entorno virtual.

Bash

# Crear el entorno
python -m venv venv

# Activarlo (en macOS/Linux)
source venv/bin/activate

# Activarlo (en Windows)
.\venv\Scripts\activate
3. Instalar dependencias
Instala todas las librerías necesarias listadas en requirements.txt.

Bash

pip install -r requirements.txt
▶️ Ejecución
Una vez configurado el entorno, puedes ejecutar el script principal. Este se encargará de cargar, limpiar, procesar, suavizar y visualizar los datos del embalse.

Bash

python main.py
Las gráficas generadas se guardarán automáticamente en el directorio /img.

🧪 Pruebas
El proyecto incluye pruebas unitarias para garantizar la fiabilidad del código.

Para ejecutar las pruebas, usa el siguiente comando desde la raíz del proyecto:

Bash

python -m unittest discover tests/
Para generar un informe de cobertura de código:

Bash

coverage run -m unittest discover tests/
coverage report -m
Puedes encontrar capturas de pantalla de los resultados de las pruebas y la cobertura en la carpeta /screenshots.

📁 Estructura del Proyecto
El repositorio está organizado de la siguiente manera:

Bash

.
├── data/              # Contiene los datasets de entrada (ej: baells.csv)
├── doc/               # Documentación HTML generada con pdoc
├── eda/               # Módulos para el análisis exploratorio de datos
├── img/               # Imágenes y visualizaciones generadas
├── screenshots/       # Evidencias de testing y cobertura
├── src/               # Módulos principales de la aplicación
│   └── exercises/     # Scripts para cada fase del análisis
├── tests/             # Pruebas unitarias
├── visuals/           # Módulos para la generación de gráficos
├── .gitignore         # Archivos ignorados por Git
├── LICENSE            # Licencia del proyecto
├── main.py            # Script principal ejecutable
├── README.md          # Este archivo
└── requirements.txt   # Dependencias de Python
🧾 Documentación
La documentación técnica del código fuente ha sido generada automáticamente con pdoc a partir de los docstrings.

Para consultarla, abre el archivo doc/index.html en tu navegador web.

👨‍💻 Autor
Abdullah Fasih
Universitat Oberta de Catalunya (UOC) – 2025