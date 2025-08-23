import json
from decimal import Decimal


def calculate_profit(trade_file: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(trade_file, "r") as f:
        trades = json.load(f)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")

        if bought > sold:
            bought -= sold
            earned_money -= bought * price
            matecoin_account += bought

        elif sold > bought:
            sold -= bought
            earned_money += sold * price
            matecoin_account -= sold

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
