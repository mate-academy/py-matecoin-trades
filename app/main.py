import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        data = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in data:
        price = Decimal(trade["matecoin_price"])

        if trade.get("bought"):
            amount = Decimal(trade["bought"])
            earned_money -= amount * price
            matecoin_account += amount

        if trade.get("sold"):
            amount = Decimal(trade["sold"])
            earned_money += amount * price
            matecoin_account -= amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
