from datetime import datetime, timedelta


def is_future(days=0):
    date = datetime.now() + timedelta(days=days)
    return date.strftime("%d-%m-%Y %H:%M:%S")
