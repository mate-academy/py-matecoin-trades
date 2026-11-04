import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as f:
        trades = json.load(f)

    total_bought = Decimal("0")
    total_sold = Decimal("0")
    money_spent = Decimal("0")
    money_earned = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            total_bought += amount
            money_spent += amount * price

        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            total_sold += amount
            money_earned += amount * price

    earned_money = money_earned - money_spent
    matecoin_account = total_bought - total_sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
