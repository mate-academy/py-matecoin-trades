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
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= price * bought

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += price * sold
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as saved_file:
        json.dump(result, saved_file, indent=2)
