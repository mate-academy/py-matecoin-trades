import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        transactions = json.load(file)
        matecoin_account = 0
        earned_money = 0
        for transaction in transactions:
            if transaction["bought"] is not None:
                earned_money -= Decimal(transaction["bought"]) * Decimal(
                    transaction["matecoin_price"])
                matecoin_account += Decimal(transaction["bought"])
            if transaction["sold"] is not None:
                earned_money += Decimal(transaction["sold"]) * Decimal(
                    transaction["matecoin_price"])
                matecoin_account -= Decimal(transaction["sold"])

    with open("profit.json", "w") as file:
        json.dump(
            {"earned_money": str(earned_money),
             "matecoin_account": str(matecoin_account)},
            file, indent=2
        )
