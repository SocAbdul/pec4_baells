import pandas as pd

def carga_y_explora(path_csv: str) -> pd.DataFrame:
    """
    Carga un archivo CSV en un DataFrame y muestra una exploración básica.

    Muestra por pantalla:
      - Las primeras filas del DataFrame.
      - La lista de columnas.
      - Información general del DataFrame (tipos, nulos, etc.).

    Args:
        path_csv (str): Ruta al archivo CSV.

    Returns:
        pandas.DataFrame: DataFrame cargado desde el archivo CSV.
    """
    df = pd.read_csv(path_csv, sep=",", encoding="utf-8")
    print("\n--- Primeras filas ---\n", df.head())
    print("\n--- Columnas ---\n", df.columns.tolist())
    print("\n--- Información general ---\n", df.info())
    return df
