import datetime as dt

def get_date():
    now = dt.datetime.now()

    if now.day < 10:
        day = f'0{now.day}'
    else:
        day = now.day

    if now.month < 10:
        month = f'0{now.month}'
    else:
        month = now.month

    return [f'{day}.{month}.{now.year}', f'{now.year}-{month}-{day}']
