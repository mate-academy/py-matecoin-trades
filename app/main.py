import json
from decimal import Decimal


def calculate_profit(trade_file: str) -> None:
    with open(trade_file, "r") as file:
        trades = json.load(file)

    earned_amount = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            earned_amount -= (price * amount)
            matecoin_account += amount
        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            earned_amount += (price * amount)
            matecoin_account -= amount

    result = {
        "earned_money": str(earned_amount),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
