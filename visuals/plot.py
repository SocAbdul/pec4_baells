import matplotlib.pyplot as plt

def plot_volumen_vs_tiempo(df, alumno):
    """
    Genera y guarda una gráfica de la evolución del porcentaje de volumen embalsado a lo largo del tiempo.

    Crea una figura que muestra la columna `nivell_perc` frente a la columna `dia`, 
    personaliza el título con el nombre del alumno y guarda el gráfico como imagen PNG 
    en la carpeta 'img/'.

    Args:
        df (pandas.DataFrame): DataFrame que debe contener las columnas 'dia' y 'nivell_perc'.
        alumno (str): Nombre del alumno que se mostrará en el subtítulo y se usará para nombrar el archivo.

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df["dia"], df["nivell_perc"], label="Porcentaje de volumen")
    plt.xlabel("Fecha")
    plt.ylabel("Volumen embassat (%)")
    plt.title("Evolución del volumen en La Baells")
    plt.suptitle(f"Alumno: {alumno}", fontsize=10)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"img/labaells_{alumno.replace(' ', '_').lower()}.png")
    # plt.show()
    plt.close()
    print(f"✅ Gráfica guardada en: img/labaells_{alumno.replace(' ', '_').lower()}.png")