import os
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

def suaviza_y_grafica(df, autor, filename):
    """
    Aplica un filtro de suavizado a la serie temporal de porcentaje de volumen embalsado
    y genera una gráfica que se guarda como imagen.

    - Aplica el filtro de Savitzky-Golay sobre la columna 'nivell_perc'.
    - Genera una figura con la serie original y la suavizada.
    - Guarda la imagen en la carpeta 'img/' con el nombre especificado.

    Args:
        df (pandas.DataFrame): DataFrame con columnas 'dia' y 'nivell_perc'.
        autor (str): Nombre del autor a mostrar como subtítulo del gráfico.
        filename (str): Nombre del archivo de imagen a guardar (por ejemplo, "grafica.png").

    Returns:
        numpy.ndarray: Serie suavizada correspondiente a 'nivell_perc'.
    """
    # Crear carpeta 'img' si no existe
    os.makedirs("img", exist_ok=True)
    save_path = os.path.join("img", filename)

    y = df["nivell_perc"].values
    y_smooth = savgol_filter(y, window_length=1500, polyorder=3)

    plt.figure(figsize=(10, 6))
    plt.plot(df["dia"], y, label="original")
    plt.plot(df["dia"], y_smooth, label="smoothed", linewidth=6, color='orange')
    plt.title("Embassament de La Baells")
    plt.suptitle(autor)
    plt.xlabel("temps")
    plt.ylabel("percentage (%)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path)
    # plt.show()  # Mostrar la gráfica
    plt.close()

    print(f"✅ Imagen suavizada guardada en: {save_path}")
    return y_smooth
