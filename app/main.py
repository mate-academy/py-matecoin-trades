import json
from decimal import Decimal


def calculate_profit(trades_filepath: str) -> None:
    with open(trades_filepath, "r", encoding="utf-8") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(str(trade["matecoin_price"]))

        if trade.get("bought"):
            bought = Decimal(str(trade["bought"]))
            matecoin_account += bought
            earned_money -= bought * price

        if trade.get("sold"):
            sold = Decimal(str(trade["sold"]))
            matecoin_account -= sold
            earned_money += sold * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
