import json
from decimal import Decimal, getcontext

getcontext().prec = 28


def calculate_profit(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as f:
        trades = json.load(f)

    total_bought_coins = Decimal("0")
    total_sold_coins = Decimal("0")
    earned_money = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            total_bought_coins += bought
            earned_money -= bought * price  # покупка = расход денег

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            total_sold_coins += sold
            earned_money += sold * price  # продажа = доход

    balance = total_bought_coins - total_sold_coins

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(balance)
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False)
