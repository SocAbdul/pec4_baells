import pandas as pd

def load_dataset(filepath):
    """Carga el dataset CSV en un DataFrame."""
    return pd.read_csv(filepath)

def show_head(df, n=5):
    """Muestra las primeras n filas."""
    print(df.head(n))

def show_columns(df):
    """Muestra los nombres de las columnas."""
    print(df.columns.tolist())

def show_info(df):
    """Muestra la info general del dataframe."""
    print(df.info())
