import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        python_dict = json.load(f)
    sum_of_b = 0
    sum_of_s = 0
    buy = 0
    sold = 0
    for trade in python_dict:
        if trade["bought"]:
            buy += Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            sum_of_b += Decimal(trade["bought"])
        if trade["sold"]:
            sold += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            sum_of_s += Decimal(trade["sold"])
    prof = {
        "earned_money": str(sold - buy),
        "matecoin_account": str(sum_of_b - sum_of_s)
    }
    with open("profit.json", "w") as profit:
        json.dump(prof, profit, indent=2)
