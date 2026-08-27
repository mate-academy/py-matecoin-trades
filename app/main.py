from json import loads


def calculate_profit(file_name: str) -> None:
    with open(file_name) as json_file:
        result = loads(json_file.read())
        print(result)
