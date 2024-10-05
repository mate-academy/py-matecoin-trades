import json
from decimal import Decimal
from types import NoneType


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as data:
        trades = json.load(data)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal("0")
        sold = Decimal("0")
        if not isinstance(trade["bought"], NoneType):
            bought = Decimal(trade["bought"])
        if not isinstance(trade["sold"], NoneType):
            sold = Decimal(trade["sold"])

        matecoin_price = Decimal(trade["matecoin_price"])

        if bought > 0:
            matecoin_account += bought
            earned_money -= bought * matecoin_price
        if sold > 0:
            matecoin_account -= sold
            earned_money += sold * matecoin_price

    data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit:
        json.dump(data, profit, indent=2)
