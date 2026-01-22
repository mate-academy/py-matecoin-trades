import json
from decimal import Decimal


def calculate_profit(filename: json) -> None:
    result = {
        "earned_money": 0,
        "matecoin_account": 0
    }
    with open(filename, "r") as file_data:
        trades = json.load(file_data)

        for trade in trades:
            if trade["bought"] is not None:
                result["earned_money"] -= Decimal(
                    trade["bought"]) * Decimal(trade["matecoin_price"])
                result["matecoin_account"] += Decimal(trade["bought"])

            if trade["sold"] is not None:
                result["earned_money"] += Decimal(
                    trade["sold"]) * Decimal(trade["matecoin_price"])
                result["matecoin_account"] -= Decimal(trade["sold"])

    result = {key: str(value) for key, value in result.items()}
    with open("profit.json", "w") as new_file:
        json.dump(result, new_file, indent=2)
