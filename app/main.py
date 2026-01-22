import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        data = json.load(f)

    result = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    for trade in data:
        if trade["bought"] is not None:
            result["earned_money"] -= \
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            result["matecoin_account"] += Decimal(trade["bought"])

        if trade["sold"] is not None:
            result["earned_money"] += \
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            result["matecoin_account"] -= Decimal(trade["sold"])

    result_for_json = {
        "earned_money": str(result["earned_money"]),
        "matecoin_account": str(result["matecoin_account"])
    }

    with open("profit.json", "w") as profit:
        json.dump(result_for_json, profit, indent=2)
