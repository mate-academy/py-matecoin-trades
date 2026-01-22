import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    """Load Matecoin trades, calculate profit and save results to JSON."""
    with open(filename, "r", encoding="utf-8") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        bought = trade.get("bought")
        if bought is not None:
            amount = Decimal(bought)
            matecoin_account += amount
            earned_money -= amount * price

        sold = trade.get("sold")
        if sold is not None:
            amount = Decimal(sold)
            matecoin_account -= amount
            earned_money += amount * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
