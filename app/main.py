import json
from decimal import Decimal, getcontext

getcontext().prec = 28


def calculate_profit(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as f:
        trades = json.load(f)

    total_bought = Decimal("0")
    total_sold = Decimal("0")
    earned_money = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            total_bought += bought
            earned_money -= bought * price

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            total_sold += sold
            earned_money += sold * price

    balance = total_bought - total_sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(balance)
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
