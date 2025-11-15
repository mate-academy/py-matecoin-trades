import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    balance = {"earned_money": Decimal("0"), "matecoin_account": Decimal("0")}

    for trade in trades:
        bought_in_dollars = - Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
        sold_in_dollars = Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
        matecoins = Decimal(trade["bought"]) - Decimal(trade["sold"])

        balance["earned_money"] += bought_in_dollars + sold_in_dollars
        balance["matecoin_account"] += matecoins

    with open("profit.json", "w") as profit_file:
        json.dump(balance, profit_file)


calculate_profit("trades_1.json")
