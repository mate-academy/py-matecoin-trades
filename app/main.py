import json
from decimal import Decimal


def calculate_profit(trades_json: str) -> None:
    with open(trades_json, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            matecoin_account += bought
            earned_money -= bought * matecoin_price

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            matecoin_account -= sold
            earned_money += sold * matecoin_price

    current = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(current, file, indent=2)
