import json
from decimal import Decimal


def calculate_profit(source_filename: str) -> None:
    profit, amount = Decimal("0"), Decimal("0")

    with open(source_filename) as trades:
        trades_dict = json.load(trades)

    for trade in trades_dict:

        if trade["bought"]:
            profit -= (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )
            amount += Decimal(trade["bought"])

        if trade["sold"]:
            profit += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )
            amount -= Decimal(trade["sold"])

    with open("profit.json", "w") as profit_file:
        json.dump(
            {"earned_money": str(profit), "matecoin_account": str(amount)},
            profit_file,
            indent=2
        )
