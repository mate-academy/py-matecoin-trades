import json
import decimal


def prepare_js_file_after_read(js_file: str) -> str:
    for transaction in js_file:
        if transaction["bought"] is not None:
            transaction["bought"] = float_to_decimal(transaction["bought"])
        elif transaction["sold"] is not None:
            transaction["sold"] = float_to_decimal(transaction["sold"])
    return js_file


def float_to_decimal(value: str) -> decimal:
    return decimal.Decimal(value)


def read_js_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        mentors = json.load(file)
        return mentors


def calculate_profit(file_name: str) -> None:
    js_file_as_list = read_js_file(file_name)
    js_float_as_decimal = prepare_js_file_after_read(js_file_as_list)
    print(js_float_as_decimal)


if __name__ == "__main__":
    calculate_profit("trades.json")
