import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)
        total_bought = 0
        total_sold = 0
        spend_money = 0
        income_money = 0
        for trade in trades:
            if trade["bought"] is not None:
                total_bought += Decimal(trade["bought"])
                spend_money += (
                    Decimal(trade["bought"])
                    * Decimal(trade["matecoin_price"])
                )
            if trade["sold"] is not None:
                total_sold += Decimal(trade["sold"])
                income_money += (
                    Decimal(trade["sold"])
                    * Decimal(trade["matecoin_price"])
                )
        profit = {
            "earned_money": str(income_money - spend_money),
            "matecoin_account": str(total_bought - total_sold)
        }
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
