import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        data = json.load(file)

    with open("profit.json", "w") as file:
        earned_money = Decimal(0)
        matecoin_account = Decimal(0)

        for transaction in data:
            if transaction["bought"]:
                matecoin_account += Decimal(transaction["bought"])
                earned_money -= Decimal(transaction["bought"]) * Decimal(
                    transaction["matecoin_price"]
                )
            if transaction["sold"]:
                matecoin_account -= Decimal(transaction["sold"])
                earned_money += Decimal(transaction["sold"]) * Decimal(
                    transaction["matecoin_price"]
                )

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }

        json.dump(result, file, indent=2)
