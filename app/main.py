import json
from decimal import Decimal


def calculate_profit(doc: str) -> None:
    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")
    with open(doc, "r") as file:
        transactions = json.load(file)
    for transaction in transactions:
        matecoin_price = Decimal(transaction["matecoin_price"])

        if transaction["bought"]:
            bought = Decimal(transaction["bought"])
            matecoin_account += bought
            earned_money -= bought * matecoin_price

        if transaction["sold"]:
            sold = Decimal(transaction["sold"])
            matecoin_account -= sold
            earned_money += sold * matecoin_price

    with open("../profit.json", "w") as file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            file,
            indent=2
        )
