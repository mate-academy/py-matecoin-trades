import json
from decimal import Decimal


def calculate_profit(trade_info: str):
    earned_money = Decimal()
    matecoin_account = Decimal()

    with open(trade_info, "r") as file, open("profit.json", "w") as json_file:
        transactions = json.load(file)

        for transaction in transactions:
            if transaction["bought"]:
                earned_money -= Decimal(transaction["bought"]) * \
                    Decimal(transaction["matecoin_price"])
                matecoin_account += Decimal(transaction["bought"])
            else:
                earned_money += Decimal(transaction["sold"]) * \
                    Decimal(transaction["matecoin_price"])
                matecoin_account -= Decimal(transaction["sold"])

        info = {"earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)}

        json.dump(info, json_file, indent=2)
