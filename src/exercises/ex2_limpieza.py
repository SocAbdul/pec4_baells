def limpia_datos(df):
    """
    Limpia un DataFrame renombrando columnas, limpiando nombres de estaciones y filtrando solo los datos de La Baells.

    Operaciones realizadas:
      - Renombra columnas para estandarizar nombres.
      - Elimina el prefijo "Embassament de " y cualquier texto entre paréntesis en la columna 'estacio'.
      - Filtra el DataFrame para conservar únicamente los registros de "La Baells".

    Args:
        df (pandas.DataFrame): DataFrame original con datos de embalses.

    Returns:
        pandas.DataFrame: DataFrame limpio y filtrado con registros solo de La Baells.
    """
    df = df.rename(columns={
        "Dia": "dia",
        "Estació": "estacio",
        "Nivell absolut (msnm)": "nivell_msnm",
        "Percentatge volum embassat (%)": "nivell_perc",
        "Volum embassat (hm3)": "volum"
    })
    df["estacio"] = df["estacio"].str.replace(r"Embassament de ", "", regex=True)
    df["estacio"] = df["estacio"].str.replace(r"\s*\(.*?\)", "", regex=True)
    return df[df["estacio"].str.lower() == "la baells"].copy()
