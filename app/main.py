from json import dump, loads


def calculate_profit(file_name: str) -> None:
    with open(file_name) as json_file:
        object = loads(json_file.read())

print(object)
