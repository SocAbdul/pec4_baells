import re

def renombrar_columnas(df):
    columnas = {
        'Dia': 'dia',
        'Estació': 'estacio',
        'Nivell absolut (msnm)': 'nivell_msnm',
        'Percentatge volum embassat (%)': 'nivell_perc',
        'Volum embassat (hm3)': 'volum'
    }
    return df.rename(columns=columnas)

def limpiar_nombre(nombre):
    # Elimina "Embassament de " y lo que está entre paréntesis
    nombre = re.sub(r'^Embassament de ', '', nombre)
    nombre = re.sub(r'\s*\(.*?\)', '', nombre)
    return nombre.strip()

def limpiar_nombres_estaciones(df):
    df['estacio'] = df['estacio'].apply(limpiar_nombre)
    return df

def filtrar_baells(df):
    # Filtra los registros que contengan "baells" en minúsculas
    df_baells = df[df['estacio'].str.lower().str.contains("baells")].copy()
    # Asigna el nombre limpio "La Baells" para homogeneidad
    df_baells['estacio'] = 'La Baells'
    return df_baells

def limpiar_datos(df):
    df = renombrar_columnas(df)
    df = limpiar_nombres_estaciones(df)
    df_baells = filtrar_baells(df)
    return df_baells
