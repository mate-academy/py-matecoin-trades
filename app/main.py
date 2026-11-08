import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as trades_file:
        trades = json.load(trades_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * price
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * price

    with open("profit.json", "w") as profit_file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account),
            },
            profit_file,
            indent=2,
        )
