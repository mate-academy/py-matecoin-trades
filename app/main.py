import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)
        earned_money = Decimal("0")
        matecoin_account = Decimal("0")
        for trade in trades:
            price = Decimal(trade["matecoin_price"])
            if trade["bought"] is not None:
                amount = Decimal(trade["bought"])
                matecoin_account += amount
                earned_money -= price * amount
            if trade["sold"] is not None:
                amount = Decimal(trade["sold"])
                matecoin_account -= amount
                earned_money += price * amount
        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
