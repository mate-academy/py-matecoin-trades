import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        data = json.load(f)

    total_money = Decimal("0")
    total_coins = Decimal("0")

    for trade in data:
        if trade["bought"] is not None:
            total_coins += Decimal(trade["bought"])
            total_money -= (Decimal(trade["bought"])
                            * Decimal(trade["matecoin_price"]))

        if trade["sold"] is not None:
            total_coins -= Decimal(trade["sold"])
            total_money += (Decimal(trade["sold"])
                            * Decimal(trade["matecoin_price"]))

    result = {
        "earned_money": str(total_money),
        "matecoin_account": str(total_coins)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
