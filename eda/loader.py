import pandas as pd

def load_dataset(filepath):
    """
    Carga un archivo CSV y lo convierte en un DataFrame de pandas.

    Args:
        filepath (str): Ruta al archivo CSV.

    Returns:
        pandas.DataFrame: DataFrame con los datos cargados desde el archivo.
    """
    return pd.read_csv(filepath)

def show_head(df, n=5):
    """
    Muestra las primeras 'n' filas del DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame del cual mostrar los datos.
        n (int, optional): Número de filas a mostrar. Por defecto es 5.

    Returns:
        None
    """
    print(df.head(n))

def show_columns(df):
    """
    Muestra la lista de nombres de columnas del DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame del cual obtener los nombres de columnas.

    Returns:
        None
    """
    print(df.columns.tolist())

def show_info(df):
    """
    Muestra información general del DataFrame, como el número de entradas, tipos de datos, etc.

    Args:
        df (pandas.DataFrame): DataFrame del cual mostrar la información.

    Returns:
        None
    """
    print(df.info())
