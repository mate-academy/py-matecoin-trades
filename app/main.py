import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal()
    matecoin_balance = Decimal()

    with open(file_name, "r") as import_file, \
            open("profit.json", "w") as result_file:
        transactions = json.load(import_file)

        for transaction in transactions:
            if transaction["bought"]:
                earned_money -= Decimal(transaction["bought"]) * \
                    Decimal(transaction["matecoin_price"])
                matecoin_balance += Decimal(transaction["bought"])

                if transaction["sold"]:
                    earned_money += Decimal(transaction["sold"]) * \
                        Decimal(transaction["matecoin_price"])
                    matecoin_balance -= Decimal(transaction["sold"])

            else:
                earned_money += Decimal(transaction["sold"]) * \
                    Decimal(transaction["matecoin_price"])
                matecoin_balance -= Decimal(transaction["sold"])

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_balance)
        }

        json.dump(result, result_file, indent=2)
