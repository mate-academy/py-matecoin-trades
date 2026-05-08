import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        data = json.load(json_file)

    earned = Decimal("0.0")
    account = Decimal("0.0")

    for trade in data:
        price = Decimal(str(trade["matecoin_price"]))

        if trade.get("sold"):
            amount = Decimal(str(trade["sold"]))
            earned += price * amount
            account -= amount

        if trade.get("bought"):
            amount = Decimal(str(trade["bought"]))
            earned -= price * amount
            account += amount

    profit = {
        "earned_money": str(earned),
        "matecoin_account": str(account)
    }

    with open("profit.json", "w") as outfile:
        json.dump(profit, outfile, indent=2)
