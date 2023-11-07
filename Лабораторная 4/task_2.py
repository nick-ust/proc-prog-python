# TODO импортировать необходимые молули
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []
    with open(INPUT_FILENAME, 'r') as f:  # TODO считать содержимое csv файла
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    with open(OUTPUT_FILENAME, 'w') as f:
        json.dump(data, f, indent=4)  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
