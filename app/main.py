import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        json_data = json.load(file)

    earned = Decimal("0")
    account = Decimal("0")
    for data in json_data:
        if data["bought"] is not None:
            amount = Decimal(data["bought"])
            price = Decimal(data["matecoin_price"])
            account += amount
            earned -= amount * price

        if data["sold"] is not None:
            amount = Decimal(data["sold"])
            price = Decimal(data["matecoin_price"])
            account -= amount
            earned += amount * price

    result = {
        "earned_money": str(earned),
        "matecoin_account": str(account),
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
