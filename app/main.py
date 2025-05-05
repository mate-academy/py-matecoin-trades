import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r", encoding="utf-8") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            earned_money -= bought * price
            matecoin_account += bought

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            earned_money += sold * price
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
