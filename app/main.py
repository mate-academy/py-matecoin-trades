from decimal import Decimal
import json


def calculate_profit(data: str) -> json:
    with open(data, "r") as file:
        date = json.load(file)
    result_profit = {
        "earned_money": 0,
        "matecoin_account": 0,
    }

    for coin in date:
        if coin["bought"]:
            result_profit["matecoin_account"] += Decimal(coin["bought"])
            result_profit["earned_money"] \
                -= Decimal(coin["bought"]) * Decimal(coin["matecoin_price"])
        if coin["sold"]:
            result_profit["matecoin_account"] -= Decimal(coin["sold"])
            result_profit["earned_money"] \
                += Decimal(coin["sold"]) * Decimal(coin["matecoin_price"])

    result_profit["earned_money"] = str(result_profit["earned_money"])
    result_profit["matecoin_account"] = str(result_profit["matecoin_account"])

    with open("profit.json", "w") as new:
        json.dump(result_profit, new, indent=2)
