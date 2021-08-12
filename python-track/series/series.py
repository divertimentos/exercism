import random

def generate_series(length):
    series_list = list()
    while len(series_list) < length:
        series_list.append(random.randint(0, 9))
    return ''.join(map(str, series_list))

def slices(series, length):
    pass


