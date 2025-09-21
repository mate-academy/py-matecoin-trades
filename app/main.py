import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as json_file:
        transaction = json.load(json_file)
    matecoin_account = Decimal("0")
    spent = Decimal("0")
    received = Decimal("0")

    for trade in transaction:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            spent += bought * price
            matecoin_account += bought
        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            received += sold * price
            matecoin_account -= sold

    earned_money = received - spent

    report = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(report, profit_file, indent=2)
