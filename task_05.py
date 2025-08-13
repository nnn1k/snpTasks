from datetime import datetime, timedelta


def date_in_future(days=0):
    if not isinstance(days, int):
        date = datetime.now()
    else:
        date = datetime.now() + timedelta(days=days)
    new_date = date.strftime("%d-%m-%Y %H:%M:%S")
    return new_date

