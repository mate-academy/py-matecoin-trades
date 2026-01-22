import json

from decimal import Decimal


def calculate_profit(trades_file: json) -> None:
    with open(trades_file, "r") as f:
        trades = json.load(f)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            cost = bought * matecoin_price
            matecoin_account += bought
            earned_money -= cost

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            revenue = sold * matecoin_price
            matecoin_account -= sold
            earned_money += revenue

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
