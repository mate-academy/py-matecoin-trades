import json
import decimal


profit = {
    "earned_money": decimal.Decimal(0),
    "matecoin_account": decimal.Decimal(0)
}


def prepare_decimal_dict_for_dump(dict_to_dump: dict) -> dict:
    for key, value in dict_to_dump.items():
        dict_to_dump[key] = str(value)
    return dict_to_dump


def write_js_file(file_name: str, data: dict) -> None:
    with open(file_name, "w") as file:
        json.dump(data, file, indent=2)


def creat_sold(amount: decimal, coin_price: decimal) -> None:
    profit["earned_money"] += amount * coin_price
    profit["matecoin_account"] -= amount


def creat_buy(amount: decimal, coin_price: decimal) -> None:
    profit["earned_money"] -= amount * coin_price
    profit["matecoin_account"] += amount


def create_transactions(actions: str) -> None:
    for action in actions:
        create_one_transaction(action)


def create_one_transaction(action: str) -> None:
    if action["bought"] is not None:
        creat_buy(action["bought"], action["matecoin_price"])

    if action["sold"] is not None:
        creat_sold(action["sold"], action["matecoin_price"])


def prepare_js_file_after_read(js_file: str) -> str:
    for transaction in js_file:
        if transaction["bought"] is not None:
            transaction["bought"] = float_to_decimal(transaction["bought"])
        if transaction["sold"] is not None:
            transaction["sold"] = float_to_decimal(transaction["sold"])
        transaction["matecoin_price"] = float_to_decimal(
            transaction["matecoin_price"])
    return js_file


def float_to_decimal(value: str) -> decimal:
    return decimal.Decimal(value)


def read_js_file(file_name: str) -> str:
    with open(file_name, "r") as file:
        mentors = json.load(file)
        return mentors


def calculate_profit(file_name: str) -> None:
    js_file_as_list = read_js_file(file_name)
    js_str_as_decimal = prepare_js_file_after_read(js_file_as_list)
    create_transactions(js_str_as_decimal)
    js_decimal_as_str = prepare_decimal_dict_for_dump(profit)
    write_js_file("profit.json", js_decimal_as_str)
