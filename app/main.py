import json
from decimal import Decimal


def calculate_profit(trade_file: str) -> None:

    with (open(trade_file, "r") as file):
        trades = json.load(file)

        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for trade in trades:

            matecoin_price = Decimal(trade["matecoin_price"])

            bought_qty = Decimal("0")

            if trade["bought"] is not None:
                bought_qty = Decimal(trade["bought"])

            matecoin_account += bought_qty
            earned_money -= bought_qty * matecoin_price

            sold_qty = Decimal("0")

            if trade["sold"] is not None:
                sold_qty = Decimal(trade["sold"])

            matecoin_account -= sold_qty
            earned_money += sold_qty * matecoin_price

    with open("profit.json", "w") as file:
        json.dump({
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }, file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
