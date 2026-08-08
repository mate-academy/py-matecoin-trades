import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        transactions = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for transaction in transactions:
        if transaction["bought"]:
            spent_money = (
                Decimal(transaction["bought"])
                * Decimal(transaction["matecoin_price"])
            )
            earned_money -= spent_money
            matecoin_account += Decimal(transaction["bought"])

        if transaction["sold"]:
            income_money = (
                Decimal(transaction["sold"])
                * Decimal(transaction["matecoin_price"])
            )
            earned_money += income_money
            matecoin_account -= Decimal(transaction["sold"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
