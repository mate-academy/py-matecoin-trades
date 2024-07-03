import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    total_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            total_money -= bought * price
            matecoin_account += bought
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            total_money += sold * price
            matecoin_account -= sold

    result = {
        "earned_money": str(total_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
