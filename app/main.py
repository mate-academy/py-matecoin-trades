import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as start_file,\
            open("profit.json", "w") as result_file:
        start_data = json.load(start_file)
        earned_money = Decimal(0)
        matecoin_account = Decimal(0)
        for transaction in start_data:
            if not transaction["sold"]:
                transaction["sold"] = Decimal(0)
            elif not transaction["bought"]:
                transaction["bought"] = Decimal(0)
            earned_money += (Decimal(transaction["sold"])
                             * Decimal(transaction["matecoin_price"])
                             - Decimal(transaction["bought"])
                             * Decimal(transaction["matecoin_price"]))
            matecoin_account += (Decimal(transaction["bought"])
                                 - Decimal(transaction["sold"]))
        result = {"earned_money": str(earned_money),
                  "matecoin_account": str(matecoin_account)}
        json.dump(result, result_file, indent=2)
