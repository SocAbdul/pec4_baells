from datetime import datetime

def toYearFraction(date):
    def sinceEpoch(date):  # returns seconds since epoch
        return (date - datetime(1970, 1, 1)).total_seconds()

    year = date.year
    start = datetime(year=year, month=1, day=1)
    end = datetime(year=year + 1, month=1, day=1)

    year_elapsed = sinceEpoch(date) - sinceEpoch(start)
    year_duration = sinceEpoch(end) - sinceEpoch(start)

    fraction = year_elapsed / year_duration
    return year + fraction
