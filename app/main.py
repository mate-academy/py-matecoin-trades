import json

from decimal import Decimal


def calculate_profit(name: str):
    result = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    with open(name, "r") as f:
        trades_data = json.load(f)
        for trade in trades_data:
            if trade["sold"]:
                result["earned_money"] += Decimal(
                    trade["sold"]) * Decimal(trade["matecoin_price"])
                result["matecoin_account"] += Decimal(trade["sold"])
            if trade["bought"]:
                result["earned_money"] -= Decimal(
                    trade["bought"]) * Decimal(trade["matecoin_price"])
                result["matecoin_account"] -= Decimal(trade["bought"])
        result["earned_money"] = str(result["earned_money"])
        result["matecoin_account"] = str(result["matecoin_account"])

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)


calculate_profit("trades.json")
