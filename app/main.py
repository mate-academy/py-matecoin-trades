import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    """Calculate profit and Matecoin account balance from trades JSON file."""
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(filename, "r", encoding="utf-8") as file:
        trades = json.load(file)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            amount = Decimal(trade["bought"])
            matecoin_account += amount
            earned_money -= amount * price
        if trade["sold"]:
            amount = Decimal(trade["sold"])
            matecoin_account -= amount
            earned_money += amount * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
