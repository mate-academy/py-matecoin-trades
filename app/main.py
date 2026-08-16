import json
from decimal import Decimal


def calculate_profit(given_file: str) -> None:
    with open(given_file, "r") as file:
        data = json.load(file)

    earned = Decimal("0")
    account = Decimal("0")

    for deal in data:
        price = Decimal(deal["matecoin_price"])

        if bought := deal.get("bought"):
            amount = Decimal(bought)
            earned -= amount * price
            account += amount

        if sold := deal.get("sold"):
            amount = Decimal(sold)
            earned += amount * price
            account -= amount

    result = {
        "earned_money": str(earned),
        "matecoin_account": str(account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
