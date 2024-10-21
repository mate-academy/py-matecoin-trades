import json
import os
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    path = os.path.join("app", filename)
    with open(path, "r") as file:
        operations = json.load(file)
        earned = Decimal("0")
        account = Decimal("0")
        for operation in operations:
            matecoin_price = operation.get("matecoin_price")
            if bought := operation.get("bought"):
                earned = earned - Decimal(bought) * Decimal(matecoin_price)
                account = account + Decimal(bought)
            if sold := operation.get("sold"):
                earned = earned + Decimal(sold) * Decimal(matecoin_price)
                account = account - Decimal(sold)
        profit = {
            "earned_money": str(earned),
            "matecoin_account": str(account)
        }
        with open(path, "w") as file_to_write:
            json.dump(profit, "profit.json", indent=2)
