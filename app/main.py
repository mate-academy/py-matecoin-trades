from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    with open("app/trades.json", "r") as f:
        data = json.load(f)

    earned_money = Decimal("0.00")
    matecoin_account = Decimal("0.00")

    for trade in data:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade.get("bought") is not None:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * matecoin_price

        if trade.get("sold") is not None:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * matecoin_price

    profit = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
