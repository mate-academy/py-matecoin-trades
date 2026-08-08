import json
import os
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            volume = Decimal(trade["bought"])
            matecoin_account += volume
            earned_money -= volume * price

        if trade["sold"]:
            volume = Decimal(trade["sold"])
            matecoin_account -= volume
            earned_money += volume * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    project_root = os.path.dirname(os.path.dirname(file_name))
    output_path = os.path.join(project_root, "profit.json")

    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
