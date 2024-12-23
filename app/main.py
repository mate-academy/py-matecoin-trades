import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades = json.load(f)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            matecoin_account += bought
            earned_money -= bought * price

        if trade["sold"]:
            sold = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            matecoin_account -= sold
            earned_money += sold * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # Save the result in the "profit.json" file
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
