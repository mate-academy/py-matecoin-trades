import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades = json.load(f)
    earned_money = Decimal("0.1")
    matecoin_acc = Decimal("0")
    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            matecoin_acc += bought
            earned_money -= bought * matecoin_price
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            matecoin_acc -= sold
            earned_money += sold * matecoin_price

        result = {
            "earned_money": str(earned_money),
            "matecoin_acc": str(matecoin_acc)
        }

        with open("profit.json", "w") as file:
            json.dump(result, file, indent=4)


calculate_profit("trades.json")
