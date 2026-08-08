import json
import os
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            volume = Decimal(trade["bought"])
            earned_money -= price * volume
            matecoin_account += volume
        if trade["sold"]:
            volume = Decimal(trade["sold"])
            earned_money += price * volume
            matecoin_account -= volume

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    profit_file = os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)
        ), "profit.json"
    )
    with open(profit_file, "w") as f:
        json.dump(result, f, indent=2)
