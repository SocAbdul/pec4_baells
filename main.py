import argparse
from src.exercises import (
    ex1_exploracion, ex2_limpieza, ex3_procesamiento, ex4_suavizado, ex5_sequias
)
from visuals.plot import plot_volumen_vs_tiempo
"""
Script de análisis del embalse de La Baells.

Este script permite ejecutar de forma modular un conjunto de análisis sobre el embalse
de La Baells, incluyendo desde la exploración inicial de los datos hasta la detección
de periodos de sequía.

Se ejecuta desde la línea de comandos con el parámetro `-ex` para indicar hasta qué 
ejercicio (del 1 al 5) se desea ejecutar. Si no se indica, se ejecutan todos los pasos.

Ejercicios disponibles:
1. Exploración del dataset (`data/baells.csv`): muestra cabecera, columnas e info.
2. Limpieza: renombrado de columnas, limpieza de nombres y filtrado de "La Baells".
3. Procesamiento temporal: conversión de fechas y cálculo decimal del año.
4. Suavizado y visualización: suavizado de la serie temporal y guardado de imagen.
5. Detección de sequías: identifica periodos donde el nivel embalsado < 60%.

Uso:
    python main.py -ex 3   # Ejecuta hasta el ejercicio 3

Requisitos:
    - Python 3.7+
    - pandas, matplotlib, scipy

Autor:
    Abdullah Fasih (2025)

Licencia:
    MIT License (ver archivo LICENSE)
"""

def main():
    parser = argparse.ArgumentParser(description="Análisis del embalse de La Baells")
    parser.add_argument("-ex", type=int, help="Ejecuta del ejercicio 1 al N (1-5)")
    args = parser.parse_args()

    max_ej = args.ex if args.ex else 5
    print(f"\n--- Ejecutando ejercicios 1 a {max_ej} ---\n")

    df = None
    df_baells = None
    y_smooth = None

    if max_ej >= 1:
        df = ex1_exploracion.carga_y_explora("data/baells.csv")
    if max_ej >= 2:
        df_baells = ex2_limpieza.limpia_datos(df)
    if max_ej >= 3:
        df_baells = ex3_procesamiento.procesa_fechas(df_baells)
        plot_volumen_vs_tiempo(df_baells, "Abdullah Fasih")
    if max_ej >= 4:
        y_smooth = ex4_suavizado.suaviza_y_grafica(
    df_baells,
    autor="Abdullah Fasih",
    filename="labaells_smoothed_abdullah_fasih.png"
)

    if max_ej >= 5:
        periodos = ex5_sequias.calcula_periodos(df_baells["dia_decimal"].values, y_smooth)
        print("\n--- Periodos de sequía ---")
        for i, p in enumerate(periodos, 1):
            print(f"Periodo {i}: de {p[0]} a {p[1]}")

if __name__ == "__main__":
    main()
