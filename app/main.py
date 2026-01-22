import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as f:
        trades = json.load(f)
        print(trades)
    profit = 0
    amount = 0
    for trade in trades:
        matecoin_price = trade["matecoin_price"]
        if trade["bought"] is not None:
            profit -= Decimal(matecoin_price) * Decimal(trade["bought"])
            amount += Decimal(trade["bought"])
        if trade["sold"] is not None:
            profit += Decimal(matecoin_price) * Decimal(trade["sold"])
            amount -= Decimal(trade["sold"])
    result = {
        "earned_money": str(profit),
        "matecoin_account": str(amount)
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
