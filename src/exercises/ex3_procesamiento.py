import pandas as pd
from eda.utils import toYearFraction

def procesa_fechas(df):
    """
    Convierte la columna 'dia' a formato datetime, ordena el DataFrame cronológicamente 
    y añade una columna con la fecha en formato decimal (año fraccionario).

    Usa la función `toYearFraction` para calcular el año como número decimal.

    Args:
        df (pandas.DataFrame): DataFrame con una columna 'dia' en formato string.

    Returns:
        pandas.DataFrame: DataFrame con la columna 'dia' convertida a datetime,
                          ordenado por fecha y con una nueva columna 'dia_decimal'.
    """
    df["dia"] = pd.to_datetime(df["dia"], dayfirst=True)
    df = df.sort_values("dia")
    df["dia_decimal"] = df["dia"].apply(toYearFraction)
    return df
