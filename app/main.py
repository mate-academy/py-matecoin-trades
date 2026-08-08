import json
import os
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    with open(filename, "r") as f:
        trades = json.load(f)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade.get("bought") is not None:
            bought_volume = Decimal(trade["bought"])
            earned_money -= bought_volume * price
            matecoin_account += bought_volume

        if trade.get("sold") is not None:
            sold_volume = Decimal(trade["sold"])
            earned_money += sold_volume * price
            matecoin_account -= sold_volume

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(root_dir, "profit.json")

    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
