import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file_name:
        trades = json.load(file_name)
    result = {
        "earned_money": 0,
        "matecoin_account": 0
    }
    for trade in trades:
        if trade["bought"] is not None:
            result["earned_money"] -= (Decimal(trade["bought"])
                                       * Decimal(trade["matecoin_price"]))
            result["matecoin_account"] += Decimal(trade["bought"])
        if trade["sold"] is not None:
            result["earned_money"] += (Decimal(trade["sold"])
                                       * Decimal(trade["matecoin_price"]))
            result["matecoin_account"] -= Decimal(trade["sold"])

    for item in result:
        result[item] = str(result[item])

    with open("profit.json", "w") as new_file:
        json.dump(result, new_file, indent=2)
