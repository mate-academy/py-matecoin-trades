import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades = json.load(f)

    profit = {
        "earned_money": Decimal("0.0"),
        "matecoin_account": Decimal("0.0")
    }
    for trade in trades:
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            mate_price = Decimal(trade["matecoin_price"])

            profit["earned_money"] -= bought * mate_price
            profit["matecoin_account"] += bought

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            mate_price = Decimal(trade["matecoin_price"])

            profit["earned_money"] += sold * mate_price
            profit["matecoin_account"] -= sold

    print(profit)
    profit["earned_money"] = f"{profit['earned_money']}"
    profit["matecoin_account"] = f"{profit['matecoin_account']}"
    print(profit)
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
