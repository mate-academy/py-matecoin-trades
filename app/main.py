import json
from decimal import Decimal


def calculate_profit(trades_filename: str) -> None:
    with open(trades_filename, "r") as file:
        trades = json.load(file)
    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")
    for trade in trades:
        if trade["bought"]:
            bought_amount = Decimal(trade["bought"])
            matecoin_account += bought_amount
            earned_money -= bought_amount * Decimal(trade["matecoin_price"])
        if trade["sold"]:
            sold_amount = Decimal(trade["sold"])
            matecoin_account -= sold_amount
            earned_money += sold_amount * Decimal(trade["matecoin_price"])
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
