import json
import os
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(str(trade["matecoin_price"]))

        if trade.get("bought") is not None:
            volume = Decimal(str(trade["bought"]))
            earned_money -= volume * price
            matecoin_account += volume

        if trade.get("sold") is not None:
            volume = Decimal(str(trade["sold"]))
            earned_money += volume * price
            matecoin_account -= volume

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)
    profit_path = os.path.join(root_dir, "profit.json")

    with open(profit_path, "w") as file:
        json.dump(result, file, indent=2)
