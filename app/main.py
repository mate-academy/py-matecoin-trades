import decimal
import json


def calculate_profit(file_name: str) -> None:
    earned_money = 0
    matecoin_account = 0
    dict_to_write = {}
    with open(file_name, "r") as data_file:
        data = json.load(data_file)
    for operation in data:
        if operation.get("bought"):
            earned_money -= decimal.Decimal(
                operation.get("bought")) * decimal.Decimal(
                operation.get("matecoin_price"))
            matecoin_account += decimal.Decimal(operation.get("bought"))
        if operation.get("sold"):
            earned_money += decimal.Decimal(
                operation.get("sold")) * decimal.Decimal(
                operation.get("matecoin_price"))
            matecoin_account -= decimal.Decimal(operation.get("sold"))

    dict_to_write["earned_money"] = str(earned_money)
    dict_to_write["matecoin_account"] = str(matecoin_account)

    with open("../profit.json", "w") as profit_file:
        json.dump(dict_to_write, profit_file, indent=2)
