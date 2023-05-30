import json
from decimal import Decimal


def calculate_profit(transactions: str) -> None:
    with open(transactions, "r") as data, open("profit.json", "w") as target:
        trades = json.load(data)
        earned = Decimal("0")
        account = Decimal("0")
        for operation in trades:
            if operation.get("bought"):
                amount = Decimal(operation.get("bought"))
                account += amount
                outcome = amount * Decimal(operation.get("matecoin_price"))
                earned -= outcome
            if operation.get("sold"):
                amount = Decimal(operation.get("sold"))
                account -= amount
                income = amount * Decimal(operation.get("matecoin_price"))
                earned += income

        profit = {
            "earned_money": str(earned),
            "matecoin_account": str(account)
        }
        json.dump(profit, target, indent=2)
