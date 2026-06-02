import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file) as matecoin_file:
        trades = json.load(matecoin_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            earned_money -= bought * price
            matecoin_account += bought

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            earned_money += sold * price
            matecoin_account -= sold

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
