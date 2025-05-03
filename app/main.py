import json
from decimal import Decimal


def calculate_profit(trades_file: str = "trades.json") -> None:
    with open(trades_file, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            amount = Decimal(trade["bought"])
            earned_money -= amount * price
            matecoin_account += amount
        if trade["sold"]:
            amount = Decimal(trade["sold"])
            earned_money += amount * price
            matecoin_account -= amount

    output = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(output, f, indent=2)
