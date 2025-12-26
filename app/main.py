import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        data = json.load(file)

    earned = Decimal("0")
    account = Decimal("0")

    for transaction in data:
        bought = Decimal(transaction.get("bought") or "0")
        sold = Decimal(transaction.get("sold") or "0")
        price = Decimal(transaction.get("matecoin_price"))

        earned += sold * price - bought * price

        account += bought - sold

    result = {
        "earned_money": str(earned),
        "matecoin_account": str(account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
