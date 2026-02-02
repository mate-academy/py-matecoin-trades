import json
from decimal import Decimal


def calculate_profit() -> dict:
    with open("trades.json", encoding="utf-8") as f:
        trades = json.load(f)

    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    for trade in trades:
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

    with open("profit.json", "w") as f:
        json.dump(result, f)

    return result

result = calculate_profit()
print(result)