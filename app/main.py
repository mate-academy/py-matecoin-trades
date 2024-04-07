import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file) as file:
        data = json.load(file)
        earned_money, matecoin_account = 0, 0
        for transaction in data:
            if transaction["bought"]:
                amount = Decimal(transaction["bought"]) * \
                    Decimal(transaction["matecoin_price"])
                earned_money -= amount
                matecoin_account += Decimal(transaction["bought"])
            if transaction["sold"]:
                amount = Decimal(transaction["sold"]) * \
                    Decimal(transaction["matecoin_price"])
                earned_money += amount
                matecoin_account -= Decimal(transaction["sold"])

    result = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
