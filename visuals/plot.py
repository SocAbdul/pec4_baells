import matplotlib.pyplot as plt

def plot_volumen_vs_tiempo(df, alumno):
    plt.figure(figsize=(10, 6))
    plt.plot(df["dia"], df["nivell_perc"], label="Porcentaje de volumen")
    plt.xlabel("Fecha")
    plt.ylabel("Volumen embassat (%)")
    plt.title("Evolución del volumen en La Baells")
    plt.suptitle(f"Alumno: {alumno}", fontsize=10)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"img/labaells_{alumno.replace(' ', '_').lower()}.png")
    plt.show()
