import decimal
import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades_info = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_info:
        if trade["bought"]:
            earned_money -= (decimal.Decimal(trade["bought"])
                             * decimal.Decimal(trade["matecoin_price"]))
            matecoin_account += decimal.Decimal(trade["bought"])

        if trade["sold"]:
            earned_money += (decimal.Decimal(trade["sold"])
                             * decimal.Decimal(trade["matecoin_price"]))
            matecoin_account -= decimal.Decimal(trade["sold"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
