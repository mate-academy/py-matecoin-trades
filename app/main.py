import json
from decimal import Decimal
from typing import NoReturn


def calculate_profit(filename: str) -> NoReturn:
    with open(filename, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            earned_money -= bought * price
            matecoin_account += bought
        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            earned_money += sold * price
            matecoin_account -= sold

    def fmt(value: Decimal) -> str:
        value = value.quantize(Decimal("0.00000001"))
        string = format(value.normalize(), "f")
        return string.rstrip("0").rstrip(".") if "." in string else string

    result = {
        "earned_money": fmt(earned_money),
        "matecoin_account": fmt(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
