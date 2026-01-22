import json

from decimal import Decimal


def calculate_profit(trades: json) -> None:
    with open(trades, "r") as trades:
        data = json.load(trades)
        new_data = {
            "earned_money": Decimal("0"),
            "matecoin_account": Decimal("0")
        }
        for trade in data:
            if not trade["bought"] is None:
                new_data["matecoin_account"] += Decimal(trade["bought"])
                new_data["earned_money"] -= (
                    Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
                )
            if not trade["sold"] is None:
                new_data["matecoin_account"] -= Decimal(trade["sold"])
                new_data["earned_money"] += (
                    Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
                )
    new_data["matecoin_account"] = str(new_data["matecoin_account"])
    new_data["earned_money"] = str(new_data["earned_money"])
    with open("profit.json", "w") as profit:
        json.dump(new_data, profit, indent=2)

# calculate_profit("trades.json")
