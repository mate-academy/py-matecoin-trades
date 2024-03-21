import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    result = {"earned_money": Decimal("0"), "matecoin_account": Decimal("0")}

    with open(file_name, "r") as file:
        trades = json.load(file)

    for trade in trades:
        if trade.get("bought"):
            result["matecoin_account"] += Decimal(trade["bought"])
            result["earned_money"] -= Decimal(trade["bought"]) * Decimal(
                trade["matecoin_price"]
            )
        if trade.get("sold"):
            result["matecoin_account"] -= Decimal(trade["sold"])
            result["earned_money"] += Decimal(trade["sold"]) * Decimal(
                trade["matecoin_price"]
            )

    result["earned_money"] = str(result["earned_money"])
    result["matecoin_account"] = str(result["matecoin_account"])

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
