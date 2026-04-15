import json
from decimal import Decimal
from pathlib import Path


def calculate_profit(filename: str) -> None:
    with open(filename) as trades_file:
        trades = json.load(trades_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        bought = trade["bought"]
        sold = trade["sold"]

        if bought is not None:
            bought_amount = Decimal(bought)
            matecoin_account += bought_amount
            earned_money -= bought_amount * price

        if sold is not None:
            sold_amount = Decimal(sold)
            matecoin_account -= sold_amount
            earned_money += sold_amount * price

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }
    profit_filename = Path(filename).resolve().parent.parent / "profit.json"

    with open(profit_filename, "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
