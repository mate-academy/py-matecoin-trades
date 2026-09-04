import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(name_file, "r") as file:
        transactions = json.load(file)
        for transaction in transactions:
            price = Decimal(transaction["matecoin_price"])

            if transaction["bought"]:
                bought = Decimal(transaction["bought"])
                matecoin_account += bought
                earned_money -= bought * price

            if transaction["sold"]:
                sold = Decimal(transaction["sold"])
                matecoin_account -= sold
                earned_money += sold * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
