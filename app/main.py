import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    def transform_dectimal_json(data: dict) -> dict:
        return {key: str(value) for key, value in data.items()}

    with open(file_name, "r") as f:
        data = json.load(f)

        profit = {
            "earned_money": Decimal("0"),
            "matecoin_account": Decimal("0"),
        }

        for item in data:
            price = Decimal(item.get("matecoin_price"))

            if item.get("bought"):
                amount = Decimal(item.get("bought"))
                profit["earned_money"] += -amount * price
                profit["matecoin_account"] += amount

            if item.get("sold"):
                amount = Decimal(item.get("sold"))
                profit["earned_money"] += amount * price
                profit["matecoin_account"] -= amount

        with open("profit.json", "w") as f:
            json.dump(transform_dectimal_json(profit), f, indent=2)
