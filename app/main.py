import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        data = json.load(file)

    bought = sum(
        Decimal(i.get("bought"))
        for i in data if i.get("bought") is not None
    )
    sold = sum(
        Decimal(i.get("sold"))
        for i in data if i.get("sold") is not None
    )
    bought_matecoin = sum(
        Decimal(i.get("bought")) * Decimal(i.get("matecoin_price"))
        for i in data if i.get("bought") is not None
    )
    sold_matecoin = sum(
        Decimal(i.get("sold")) * Decimal(i.get("matecoin_price"))
        for i in data if i.get("sold") is not None
    )

    profit = {
        "earned_money": str(sold_matecoin - bought_matecoin),
        "matecoin_account": str(bought - sold)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
