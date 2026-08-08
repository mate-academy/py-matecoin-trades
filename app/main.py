import json
from decimal import Decimal


def calculate_profit(filename: str) -> dict:
    with open(filename, "r") as f:
        trades = json.load(f)
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")
    for record in trades:
        if record["bought"] is not None:
            qty = Decimal(record["bought"])
            price = Decimal(record["matecoin_price"])
            matecoin_account += qty
            earned_money -= qty * price
        if record["sold"] is not None:
            qty = Decimal(record["sold"])
            price = Decimal(record["matecoin_price"])
            matecoin_account -= qty
            earned_money += qty * price
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
