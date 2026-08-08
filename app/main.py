import json
from decimal import Decimal
from pathlib import Path


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * price

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * price

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }
    base_dir = Path(__file__).resolve().parent.parent
    output_path = base_dir / "profit.json"

    with open(output_path, "w") as file:
        json.dump(profit, file, indent=2)
