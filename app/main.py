import json
from decimal import Decimal


def _to_str(dec: Decimal) -> str:
    return format(dec.normalize(), 'f') if dec != 0 else "0"


def calculate_profit(name: str) -> None:
    with open(name, "r", encoding="utf-8") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for deal in trades:
        bought = deal.get("bought")
        sold = deal.get("sold")
        price = deal.get("matecoin_price")

        if bought is not None:
            amount = Decimal(bought)
            money = Decimal(price)
            matecoin_account += amount
            earned_money -= amount * money
        elif sold is not None:
            amount = Decimal(sold)
            money = Decimal(price)
            matecoin_account -= amount
            earned_money += amount * money

    result = {
        "earned_money": _to_str(earned_money),
        "matecoin_account": _to_str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f)
