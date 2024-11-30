import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        transactions = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for transaction in transactions:
        if transaction["bought"]:
            bought = Decimal(transaction["bought"])
            matecoin_price = Decimal(transaction["matecoin_price"])
            cost = bought * matecoin_price
            earned_money -= cost
            matecoin_account += bought

        if transaction["sold"]:
            sold = Decimal(transaction["sold"])
            matecoin_price = Decimal(transaction["matecoin_price"])
            revenue = sold * matecoin_price
            earned_money += revenue
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
