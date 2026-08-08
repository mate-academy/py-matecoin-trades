import json
from decimal import Decimal


def calculate_profit(json_file: str) -> None:
    with open(json_file) as f:
        data = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in data:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            matecoin_account += amount
            earned_money -= amount * price

        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            matecoin_account -= amount
            earned_money += amount * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(result, profit_file, indent=2)
