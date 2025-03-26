import os
import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    profit_file = '/Users/dimon/projects/py-matecoin-trades/profit.json'

    os.makedirs(os.path.dirname(profit_file), exist_ok=True)

    with open(file_path, "r") as file:
        info = json.load(file)

    spent_money = Decimal("0.0")
    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0"

    for trade in info:
        bought = Decimal(trade.get("bought", "0") or "0")
        sold = Decimal(trade.get("sold", "0") or "0")
        price = Decimal(trade.get("matecoin_price", "0") or "0")

        if bought > 0:
            spent_money += bought * price
            matecoin_account += bought

        if sold > 0:
            earned_money += sold * price
            matecoin_account -= sold

    profit_data = {
        "earned_money": str(earned_money - spent_money),
        "matecoin_account": str(matecoin_account),
    }

    with open(profit_file, "w") as file:
        json.dump(profit_data, file, indent=2)