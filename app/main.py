import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        transactions = json.load(file)
    profit = Decimal("0.0")
    matecoin_balance = Decimal("0.0")
    for action in transactions:
        if action["bought"]:
            profit -= (
                Decimal(action["bought"])
                * Decimal(action["matecoin_price"])
            )
            matecoin_balance += Decimal(action["bought"])
        if action["sold"]:
            profit += (
                Decimal(action["sold"])
                * Decimal(action["matecoin_price"])
            )
            matecoin_balance -= Decimal(action["sold"])
    result = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_balance)
    }
    with open("profit.json", "w") as profit:
        json.dump(result, profit, indent=2)
