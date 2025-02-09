import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)
    matecoin_account = Decimal("0")
    by = Decimal("0")
    sold = Decimal("0")
    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            by += (price * Decimal(trade["bought"]))
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"]:
            sold += (price * Decimal(trade["sold"]))
            matecoin_account -= Decimal(trade["sold"])
    profit = sold - by
    profit_file = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(profit_file, file, indent=2)
