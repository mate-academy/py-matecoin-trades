import json
from decimal import Decimal, getcontext

# Встановлюємо точність для Decimal (до 10 знаків після крапки)
getcontext().prec = 10


def calculate_profit(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            earned_money -= amount * price
            matecoin_account += amount

        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            earned_money += amount * price
            matecoin_account -= amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
