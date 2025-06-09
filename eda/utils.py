from datetime import datetime

def toYearFraction(date):
    """
    Convierte una fecha en su representación como fracción del año.

    Por ejemplo, si la fecha es el 1 de julio de 2023, la función devuelve aproximadamente 2023.5.

    Args:
        date (datetime.datetime): Objeto datetime que representa la fecha a convertir.

    Returns:
        float: Año en formato decimal (fracción del año).
    """
    def sinceEpoch(date):  # Devuelve los segundos desde el 1 de enero de 1970
        return (date - datetime(1970, 1, 1)).total_seconds()

    year = date.year
    start = datetime(year=year, month=1, day=1)
    end = datetime(year=year + 1, month=1, day=1)

    year_elapsed = sinceEpoch(date) - sinceEpoch(start)
    year_duration = sinceEpoch(end) - sinceEpoch(start)

    fraction = year_elapsed / year_duration
    return year + fraction
