import json
from decimal import Decimal


def calculate_profit(filename: str = "trades.json") -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(filename, "r", encoding="utf-8") as f:
        trades = json.load(f)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * price

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
