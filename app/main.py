import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        json_data = json.load(file)

    earned = Decimal("0")
    on_account = Decimal("0")

    for transaction in json_data:
        matecoin_price = Decimal(transaction["matecoin_price"])
        bought_amount = Decimal(transaction.get("bought") or "0")
        sold_amount = Decimal(transaction.get("sold") or "0")

        earned += (sold_amount - bought_amount) * matecoin_price
        on_account += bought_amount - sold_amount

    with open("profit.json", "w") as file:
        json.dump({
            "earned_money": str(earned),
            "matecoin_account": str(on_account)
        }, file, indent=2)
