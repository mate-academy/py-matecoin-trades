import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as transaction_file, \
            open("profit.json", "w") as profit_file:
        transactions = json.load(transaction_file)
        earned_money = Decimal("0")
        coin_account = Decimal("0")
        for transaction in transactions:
            if transaction["bought"]:
                earned_money -= Decimal(transaction["bought"]) * \
                    Decimal(transaction["matecoin_price"])
                coin_account += Decimal(transaction["bought"])

            if transaction["sold"]:
                earned_money += Decimal(transaction["sold"]) * \
                    Decimal(transaction["matecoin_price"])
                coin_account -= Decimal(transaction["sold"])
        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(coin_account),
        }
        json.dump(profit, profit_file, indent=2)
