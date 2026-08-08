import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:

    profit = Decimal("0")
    account = Decimal("0")

    with open(trades_file, "r") as file:
        trades = json.load(file)

    for trade in trades:

        if trade.get("bought"):
            bought_amount = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            profit -= bought_amount * matecoin_price
            account += bought_amount

        if trade.get("sold"):
            sold_amount = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            profit += sold_amount * matecoin_price
            account -= sold_amount

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(account),
    }

    with open("profit.json", "a") as file:
        json.dump(result, file, indent=2)
