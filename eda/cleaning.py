import re

def renombrar_columnas(df):
    """
    Renombra las columnas del DataFrame para usar nombres en minúsculas y sin caracteres especiales.

    Args:
        df (pandas.DataFrame): DataFrame con las columnas originales.

    Returns:
        pandas.DataFrame: DataFrame con los nombres de columnas renombrados.
    """
    columnas = {
        'Dia': 'dia',
        'Estació': 'estacio',
        'Nivell absolut (msnm)': 'nivell_msnm',
        'Percentatge volum embassat (%)': 'nivell_perc',
        'Volum embassat (hm3)': 'volum'
    }
    return df.rename(columns=columnas)

def limpiar_nombre(nombre):
    """
    Limpia el nombre de una estación eliminando el prefijo 'Embassament de' y cualquier texto entre paréntesis.

    Args:
        nombre (str): Nombre original de la estación.

    Returns:
        str: Nombre limpio de la estación.
    """
    nombre = re.sub(r'^Embassament de ', '', nombre)
    nombre = re.sub(r'\s*\(.*?\)', '', nombre)
    return nombre.strip()

def limpiar_nombres_estaciones(df):
    """
    Aplica la limpieza de nombres a la columna 'estacio' del DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame con la columna 'estacio'.

    Returns:
        pandas.DataFrame: DataFrame con la columna 'estacio' limpia.
    """
    df['estacio'] = df['estacio'].apply(limpiar_nombre)
    return df

def filtrar_baells(df):
    """
    Filtra el DataFrame para conservar solo los registros relacionados con 'La Baells' (insensible a mayúsculas/minúsculas).

    Args:
        df (pandas.DataFrame): DataFrame completo con datos de varias estaciones.

    Returns:
        pandas.DataFrame: DataFrame filtrado solo con registros de La Baells.
    """
    df_baells = df[df['estacio'].str.lower().str.contains("baells")].copy()
    df_baells['estacio'] = 'La Baells'
    return df_baells

def limpiar_datos(df):
    """
    Aplica una serie de transformaciones para limpiar el DataFrame y dejar solo los datos de La Baells.

    Args:
        df (pandas.DataFrame): DataFrame original con todos los registros.

    Returns:
        pandas.DataFrame: DataFrame limpio y filtrado para La Baells.
    """
    df = renombrar_columnas(df)
    df = limpiar_nombres_estaciones(df)
    df_baells = filtrar_baells(df)
    return df_baells
