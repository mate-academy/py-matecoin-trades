import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    balance = {"earned_money": Decimal("0"), "matecoin_account": Decimal("0")}

    for trade in trades:

        if trade["bought"] is None:
            decimal_bought = Decimal("0")
        else:
            decimal_bought = Decimal(trade["bought"])

        if trade["sold"] is None:
            decimal_sold = Decimal("0")
        else:
            decimal_sold = Decimal(trade["sold"])

        bought_in_dollars = - decimal_bought * Decimal(trade["matecoin_price"])
        sold_in_dollars = decimal_sold * Decimal(trade["matecoin_price"])
        matecoins = decimal_bought - decimal_sold

        balance["earned_money"] += bought_in_dollars + sold_in_dollars
        balance["matecoin_account"] += matecoins

    balance["earned_money"] = str(balance["earned_money"])
    balance["matecoin_account"] = str(balance["matecoin_account"])

    with open("profit.json", "w") as profit_file:
        json.dump(balance, profit_file, indent=2)
