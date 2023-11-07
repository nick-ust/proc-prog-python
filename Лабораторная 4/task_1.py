# TODO решите задачу
import json

FILE_NAME = 'input.json'


def task() -> float:
    with open(FILE_NAME, 'r') as f:
        data = json.load(f)
    summa = 0.
    for data_dict in data:
        summa += data_dict['score'] * data_dict['weight']
    return round(summa, 3)


print(task())
