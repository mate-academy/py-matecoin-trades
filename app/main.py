import json
from decimal import Decimal


def calculate_profit(trades: json) -> None:
    with open(trades) as f:
        trades_data = json.load(f)

    matecoin_account = Decimal(0)
    earned_money = Decimal(0)

    for trade in trades_data:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            earned_money -= bought * matecoin_price
            matecoin_account += bought
        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
