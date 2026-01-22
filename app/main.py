import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as fn:
        data = json.load(fn)

    total_bought_amount = Decimal(0)
    total_sold_amount = Decimal(0)
    total_bought = Decimal(0)
    total_sold = Decimal(0)

    for entry in data:
        bought_qty = Decimal(entry.get("bought") or 0)
        sold_qty = Decimal(entry.get("sold") or 0)
        price = Decimal(entry["matecoin_price"])

        total_bought_amount += bought_qty * price
        total_sold_amount += sold_qty * price
        total_bought += bought_qty
        total_sold += sold_qty

    profit = str(total_sold_amount - total_bought_amount)
    account = str(total_bought - total_sold)

    with open("profit.json", "w") as out:
        json.dump({
            "earned_money": profit,
            "matecoin_account": account
        }, out, indent=2)
