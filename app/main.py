import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r") as file:
        transactions = json.load(file)
        earned_money = Decimal("0")
        account = Decimal("0")

        for transaction in transactions:
            if transaction.get("bought"):
                earned_money -= (Decimal(transaction.get("bought"))
                                 * Decimal(transaction.get("matecoin_price")))
                account += Decimal(transaction.get("bought"))

            if transaction.get("sold"):
                earned_money += (Decimal(transaction.get("sold"))
                                 * Decimal(transaction.get("matecoin_price")))
                account -= Decimal(transaction.get("sold"))

        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(account)
        }

        with open("profit.json", "w") as profit_file:
            json.dump(
                profit,
                profit_file,
                indent=2,
            )
