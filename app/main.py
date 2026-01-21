import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        data = json.load(f)

    profit = {"earned_money": Decimal("0"), "matecoin_account": Decimal("0")}
    for trade in data:
        bought_amount = Decimal(trade.get("bought") or 0)
        sold_amount = Decimal(trade.get("sold") or 0)
        price = Decimal(trade["matecoin_price"])

        profit["earned_money"] += (sold_amount - bought_amount) * price
        profit["matecoin_account"] += bought_amount - sold_amount

    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
