import json
from decimal import Decimal


def calculate_profit(path: str) -> None:
    with open(path, "r") as data_file:
        data = json.load(data_file)

    result = {
        "earned_money": 0,
        "matecoin_account": 0
    }
    for trade in data:
        if trade["bought"]:
            result["matecoin_account"] += Decimal(trade["bought"])
            result["earned_money"] -= (Decimal(trade["bought"])
                                       * Decimal(trade["matecoin_price"]))
        if trade["sold"]:
            result["matecoin_account"] -= Decimal(trade["sold"])
            result["earned_money"] += (Decimal(trade["sold"])
                                       * Decimal(trade["matecoin_price"]))

    for key, value in result.items():
        result[key] = str(value)
    with open("profit.json", "w") as profit_file:
        json.dump(result, profit_file, indent=2)
