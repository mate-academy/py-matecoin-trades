import json
from decimal import Decimal
from typing import Optional


def calculate_profit(filename: str) -> Optional[None]:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(filename, "r") as file:
        trades = json.load(file)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            volume = Decimal(trade["bought"])
            earned_money -= volume * price
            matecoin_account += volume
        if trade["sold"] is not None:
            volume = Decimal(trade["sold"])
            earned_money += volume * price
            matecoin_account -= volume

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)

    return None
