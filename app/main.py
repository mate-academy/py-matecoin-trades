import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(file_name) as f:
        transactions_data = json.load(f)

    for transaction in transactions_data:
        if transaction["bought"]:
            earned_money -= (Decimal(transaction["bought"])
                             * Decimal(transaction["matecoin_price"]))
            matecoin_account += Decimal(transaction["bought"])
        if transaction["sold"]:
            earned_money += (Decimal(transaction["sold"])
                             * Decimal(transaction["matecoin_price"]))
            matecoin_account -= Decimal(transaction["sold"])

    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as f:
        json.dump(profit_dict, f, indent=2)
