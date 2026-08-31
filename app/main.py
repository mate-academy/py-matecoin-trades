import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    earned_money = Decimal("0")
    with open(filename) as file:
        trades = json.load(file)
        matecoin_account = Decimal("0")
        for trade in trades:
            if trade["bought"] is not None:
                price = Decimal(trade["matecoin_price"])
                bought = Decimal(trade["bought"])
                earned_money -= bought * price
                matecoin_account += bought
            if trade["sold"] is not None:
                price = Decimal(trade["matecoin_price"])
                sold = Decimal(trade["sold"])
                earned_money += sold * price
                matecoin_account -= sold
        res = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        with open("profit.json", "w") as file:
            json.dump(res, file, indent=2)
