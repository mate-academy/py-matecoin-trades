import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    trades = []
    with open(file_name, "r") as json_file:
        trades = json.load(json_file)
    coins = Decimal("0.0000000")
    dollars = Decimal("0.0000000")
    for i in trades:
        if i["bought"] is not None:
            coins += Decimal(i["bought"])
            dollars -= Decimal(i["matecoin_price"]) * Decimal(i["bought"])
        if i["sold"] is not None:
            coins -= Decimal(i["sold"])
            dollars += Decimal(i["matecoin_price"]) * Decimal(i["sold"])
    with open("profit.json", "w") as json_file:
        json_dict = {}
        json_dict["earned_money"] = str(dollars)
        json_dict["matecoin_account"] = str(coins)
        json.dump(json_dict, json_file)
    return None
