import json
from decimal import Decimal


def _to_str(dec: Decimal) -> str:
    return "0" if dec == 0 else format(dec, "f")


def calculate_profit(name: str) -> None:
    with open(name, "r", encoding="utf-8") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for deal in trades:
        price = Decimal(deal["matecoin_price"])

        bought = deal.get("bought")
        if bought is not None:
            amount = Decimal(bought)
            matecoin_account += amount
            earned_money -= amount * price

        sold = deal.get("sold")
        if sold is not None:
            amount = Decimal(sold)
            matecoin_account -= amount
            earned_money += amount * price

    result = {
        "earned_money": _to_str(earned_money),
        "matecoin_account": _to_str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
