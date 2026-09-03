import json
from decimal import Decimal
from pathlib import Path


def calculate_profit(filename: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(filename) as file:
        trades = json.load(file)

    for trade in trades:
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * Decimal(trade["matecoin_price"])

        if trade["sold"]:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * Decimal(trade["matecoin_price"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    profit_path = Path(filename).parent.parent / "profit.json"

    with open(profit_path, "w") as file:
        json.dump(profit, file, indent=2)
