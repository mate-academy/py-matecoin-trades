import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as trades_file:
        trades = json.load(trades_file)

    total_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            bought = Decimal(str(trade["bought"]))
            price = Decimal(str(trade["matecoin_price"]))
            matecoin_account += bought
            total_money -= bought * price

        if trade["sold"] is not None:
            sold = Decimal(str(trade["sold"]))
            price = Decimal(str(trade["matecoin_price"]))
            matecoin_account -= sold
            total_money += sold * price

    with open("profit.json", "w") as profit_file:
        json.dump(
            {
                "earned_money": str(total_money),
                "matecoin_account": str(matecoin_account),
            },
            profit_file,
            indent=2,
        )
