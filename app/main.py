import json
from decimal import Decimal


def calculate_profit(name_of_file: str) -> None:
    trades = json.load(open(name_of_file))
    current_amount = Decimal("0")
    profit = Decimal("0")
    for trade in trades:
        if trade["bought"]:
            current_amount += Decimal(trade["bought"])
            profit -= (Decimal(trade["bought"])
                       * Decimal(trade["matecoin_price"]))
        if trade["sold"]:
            current_amount -= Decimal(trade["sold"])
            profit += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
    with open("profit.json", "w") as file:
        json.dump({
            "earned_money": str(profit),
            "matecoin_account": str(current_amount),
        }, file, indent=2)
