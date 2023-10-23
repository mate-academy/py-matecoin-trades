import json
from decimal import Decimal


def calculate_profit(filename: str) -> dict:
    with open(filename, "r") as file:
        trades = json.load(file)

    result = {
        "earned_money": Decimal(0),
        "matecoin_account": Decimal(0)
    }

    for trade in trades:
        bought = Decimal(trade["bought"]) \
            if trade["bought"] is not None else Decimal(0)
        sold = Decimal(trade["sold"]) \
            if trade["sold"] is not None else Decimal(0)

        result["matecoin_account"] += (bought - sold)
        result["earned_money"] -= (bought * Decimal(trade["matecoin_price"]))
        result["earned_money"] += (sold * Decimal(trade["matecoin_price"]))

    result["earned_money"] = str(result["earned_money"])
    result["matecoin_account"] = str(result["matecoin_account"])

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
