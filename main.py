import pandas as pd
from scipy.signal import savgol_filter
from eda.utils import toYearFraction
from visuals.plot import plot_volumen_vs_tiempo
import matplotlib.pyplot as plt
import os

# --- Ejercicio 1: Carga del dataset y EDA ---
print("\n--- Ejercicio 1: Exploración de datos ---")

df = pd.read_csv("data/baells.csv", sep=",", encoding="utf-8")

print("\n--- Primeras filas ---")
print(df.head())

print("\n--- Columnas ---")
print(df.columns.tolist())

print("\n--- Información general ---")
print(df.info())

# --- Ejercicio 2: Limpieza y filtrado ---
print("\n--- Ejercicio 2: Limpieza de datos ---")

# Renombrar columnas
columnas = {
    "Dia": "dia",
    "Estació": "estacio",
    "Nivell absolut (msnm)": "nivell_msnm",
    "Percentatge volum embassat (%)": "nivell_perc",
    "Volum embassat (hm3)": "volum"
}
df = df.rename(columns=columnas)

# Limpiar nombres de pantanos con regex
df["estacio"] = df["estacio"].str.replace(r"Embassament de ", "", regex=True)
df["estacio"] = df["estacio"].str.replace(r"\s*\(.*?\)", "", regex=True)

# Filtrar solo La Baells
df_baells = df[df["estacio"].str.lower() == "la baells"].copy()

print(df_baells.head())

# --- Ejercicio 3: Procesamiento temporal y visualización ---
print("\n--- Ejercicio 3: Fecha y gráfico ---")

# Convertir a datetime
df_baells["dia"] = pd.to_datetime(df_baells["dia"], dayfirst=True)

# Ordenar y mostrar fechas
df_baells = df_baells.sort_values("dia")
print(f"\nNúmero de registros: {len(df_baells)}")
print(f"Fecha más antigua: {df_baells['dia'].iloc[0].date()}")
print(f"Fecha más reciente: {df_baells['dia'].iloc[-1].date()}")

# Crear columna decimal
df_baells["dia_decimal"] = df_baells["dia"].apply(toYearFraction)

# Gráfico
plot_volumen_vs_tiempo(df_baells, "Abdullah Fasih")

#4 --- Ejercicio 4: Suavizado de la serie temporal ---
# Suavizado
y = df_baells["nivell_perc"].values
y_smooth = savgol_filter(y, window_length=1500, polyorder=3)


# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(df_baells["dia"], y, label="original")
plt.plot(df_baells["dia"], y_smooth, label="smoothed", linewidth=6, color='orange')
plt.title("Embassament de La Baells")
plt.suptitle("Abdullah Fasih")  # Cambia aquí por tu nombre real si hace falta
plt.xlabel("temps")
plt.ylabel("percentage (%)")
plt.legend()
plt.tight_layout()

# Guardar la imagen
plt.savefig("img/labaells_smoothed_abdullah_fasih.png")
plt.show()

# --- Ejercicio 5: Cálculo de periodos de sequía ---
print("\n--- Ejercicio 5: Cálculo de periodos de sequía ---")

def calcula_periodos(fechas_decimales, niveles_suavizados, umbral):
    """
    Identifica periodos en los que una serie temporal está por debajo de un umbral.

    Args:
        fechas_decimales (array): Array con las fechas en formato decimal.
        niveles_suavizados (array): Array con los valores de la serie temporal suavizada.
        umbral (float): El valor por debajo del cual se considera un periodo de interés.

    Returns:
        list: Una lista de listas, donde cada sublista contiene la fecha de inicio
              y fin de un periodo.
    """
    # 1. Determinar en qué puntos estamos por debajo del umbral de sequía
    en_sequia = niveles_suavizados < umbral
    
    periodos = []
    inicio_periodo_actual = None

    # 2. Tratar el caso de que la serie ya comience en un periodo de sequía
    if en_sequia[0]:
        inicio_periodo_actual = fechas_decimales.iloc[0]

    # 3. Iterar a lo largo de la serie para encontrar los inicios y finales
    # Empezamos en el segundo elemento para poder comparar con el anterior
    for i in range(1, len(en_sequia)):
        # INICIO de un periodo: Ocurre cuando pasamos de NO estar en sequía a SÍ estarlo.
        if en_sequia[i] and not en_sequia[i-1]:
            inicio_periodo_actual = fechas_decimales.iloc[i]
        
        # FIN de un periodo: Ocurre cuando pasamos de SÍ estar en sequía a NO estarlo.
        elif not en_sequia[i] and en_sequia[i-1]:
            # Nos aseguramos de que este periodo tuviera un inicio registrado
            if inicio_periodo_actual is not None:
                fin_periodo_actual = fechas_decimales.iloc[i]
                periodos.append([inicio_periodo_actual, fin_periodo_actual])
                # Reseteamos para buscar el siguiente periodo
                inicio_periodo_actual = None

    # 4. Tratar el caso de que la serie termine mientras todavía está en sequía
    if inicio_periodo_actual is not None:
        fin_periodo_actual = fechas_decimales.iloc[-1]
        periodos.append([inicio_periodo_actual, fin_periodo_actual])

    return periodos


# --- Ejecución ---

# Definimos el umbral de sequía
UMBRAL_SEQUIA = 60  # 60%

# Obtenemos los datos necesarios del DataFrame y de la serie suavizada
fechas_dec = df_baells["dia_decimal"]
niveles_smooth = y_smooth

# Llamamos a la función para obtener los periodos
periodos_sequia = calcula_periodos(fechas_dec, niveles_smooth, UMBRAL_SEQUIA)

# Mostramos los resultados
print(f"Se han detectado {len(periodos_sequia)} periodos de sequía (por debajo del {UMBRAL_SEQUIA}%):")
for i, periodo in enumerate(periodos_sequia):
    # Usamos :.2f para formatear el número a dos decimales, como en el ejemplo
    print(f"  Periodo {i+1}: [{periodo[0]:.2f}, {periodo[1]:.2f}]")
    