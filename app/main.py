import os
import json
import decimal


def prepare_decimal_dict_for_dump(dict_to_dump: dict) -> dict:
    for key, value in dict_to_dump.items():
        dict_to_dump[key] = str(value)
    return dict_to_dump


def write_js_file(file_name: str, data: dict) -> None:
    with open(file_name, "w") as file:
        json.dump(data, file, indent=2)


def creat_sold(amount: decimal, coin_price: decimal, profit: dict) -> None:
    profit["earned_money"] += amount * coin_price
    profit["matecoin_account"] -= amount


def creat_buy(amount: decimal, coin_price: decimal, profit: dict) -> None:
    profit["earned_money"] -= amount * coin_price
    profit["matecoin_account"] += amount


def create_transactions(actions: str, profit: dict) -> None:
    for action in actions:
        create_one_transaction(action, profit)


def create_one_transaction(action: str, profit: dict) -> None:
    if action["bought"] is not None:
        creat_buy(action["bought"], action["matecoin_price"], profit)

    if action["sold"] is not None:
        creat_sold(action["sold"], action["matecoin_price"], profit)


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


# def read_js_file(file_name: str) -> str:
#     with open(file_name, "r") as file:
#         mentors = json.load(file)
#         return mentors


def calculate_profit(file_name: str) -> None:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    profit = {
        "earned_money": decimal.Decimal(0),
        "matecoin_account": decimal.Decimal(0)
    }

    with open(file_name, "r") as file:
        js_file_as_list = json.load(file)

    js_str_as_decimal = prepare_js_file_after_read(js_file_as_list)
    create_transactions(js_str_as_decimal, profit)
    js_decimal_as_str = prepare_decimal_dict_for_dump(profit)
    write_js_file(file_name, js_decimal_as_str)
    return None
