import json

from decimal import Decimal


def calculate_profit(trades_path: str) -> None:
    with open(trades_path, "r") as f:
        trades = json.load(f)

    result = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    for trade in trades:
        if trade["bought"]:
            result["earned_money"] -= Decimal(trade["bought"])\
                * Decimal(trade["matecoin_price"])
            result["matecoin_account"] += Decimal(trade["bought"])
        if trade["sold"]:
            result["earned_money"] += Decimal(trade["sold"])\
                * Decimal(trade["matecoin_price"])
            result["matecoin_account"] -= Decimal(trade["sold"])

    result["earned_money"] = str(result["earned_money"])
    result["matecoin_account"] = str(result["matecoin_account"])

    with open("./profit.json", "w") as f:
        json.dump(result, f, indent=2)
