import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        traders = json.load(file)

    result = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    for trade in traders:
        if trade["bought"] is not None:
            result["earned_money"] -= (
                Decimal(trade["bought"])
                * Decimal(trade["matecoin_price"])
            )
            result["matecoin_account"] += Decimal(trade["bought"])
        if trade["sold"] is not None:
            result["earned_money"] += (
                Decimal(trade["sold"])
                * Decimal(trade["matecoin_price"])
            )
            result["matecoin_account"] -= Decimal(trade["sold"])
    result = {key: str(value) for key, value in result.items()}
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
