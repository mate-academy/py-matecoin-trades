import json
from decimal import Decimal


def calculate_profit(name: json) -> None:
    with open(name, "r") as f:
        trades = json.load(f)

    decimal_money = Decimal("0")
    decimal_mat_account = Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            decimal_bought = Decimal(trade["bought"])
            decimal_mt_price = Decimal(trade["matecoin_price"])
            decimal_mat_account += decimal_bought
            decimal_money -= decimal_bought * decimal_mt_price
        if trade["sold"] is not None:
            decimal_sold = Decimal(trade["sold"])
            decimal_mt_price = Decimal(trade["matecoin_price"])
            decimal_mat_account -= decimal_sold
            decimal_money += decimal_sold * decimal_mt_price

    profit = {
        "earned_money": str(decimal_money),
        "matecoin_account": str(decimal_mat_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
