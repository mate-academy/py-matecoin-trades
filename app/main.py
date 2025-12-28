import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    with open(filename) as f:
        data = json.load(f)
    for trade in data:
        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            earned_money -= amount * price
            matecoin_account += amount
        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            earned_money += amount * price
            matecoin_account -= amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
