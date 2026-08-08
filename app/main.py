import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            volume = Decimal(trade["bought"])
            matecoin_account += volume
            earned_money -= volume * price

        if trade["sold"] is not None:
            volume = Decimal(trade["sold"])
            matecoin_account -= volume
            earned_money += volume * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
