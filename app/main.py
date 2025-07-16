import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as file:
        trade_info = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trade_info:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            earned_money -= bought * price
            matecoin_account += bought
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            earned_money += sold * price
            matecoin_account -= sold

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as file:
            json.dump(result, file, indent=2)
