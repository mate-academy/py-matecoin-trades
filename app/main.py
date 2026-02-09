import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as json_file:
        data = json.load(json_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for row in data:
        price = Decimal(row["matecoin_price"])
        bought = row.get("bought")
        sold = row.get("sold")
        if bought is not None:
            qty = Decimal(bought)
            matecoin_account += qty
            earned_money -= qty * price

        if sold is not None:
            qty = Decimal(sold)
            matecoin_account -= qty
            earned_money += qty * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as json_file:
        json.dump(result, json_file, indent=2)
