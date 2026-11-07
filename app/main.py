import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

        money_gain = Decimal("0")
        matecoin_quantity = Decimal("0")

        for trade in trades:

            if trade["bought"] is not None:
                matecoin_quantity += Decimal(trade["bought"])
                money_gain -= Decimal(
                    trade["bought"]) * Decimal(
                    trade["matecoin_price"])

            if trade["sold"] is not None:
                matecoin_quantity -= Decimal(trade["sold"])
                money_gain += Decimal(
                    trade["sold"]) * Decimal(
                    trade["matecoin_price"])

        money_gain = Decimal(f"{money_gain}")
        matecoin_quantity = Decimal(f"{matecoin_quantity}")
        profit_info = {
            "earned_money": f"{money_gain}",
            "matecoin_account": f"{matecoin_quantity}"
        }

        with open("profit.json", "w") as file:
            json.dump(profit_info, file, indent=2)
