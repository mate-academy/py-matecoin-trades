import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        transactions = json.load(file)

    earned_money = 0
    matecoin_account = 0

    for transaction in transactions:
        if transaction["bought"]:
            earned_money -= (Decimal(transaction["bought"])
                             * Decimal(transaction["matecoin_price"]))
            matecoin_account += Decimal(transaction["bought"])
        if transaction["sold"]:
            earned_money += (Decimal(transaction["sold"])
                             * Decimal(transaction["matecoin_price"]))
            matecoin_account -= Decimal(transaction["sold"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
