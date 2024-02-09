import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(file_name, "r") as source_file:
        source_data = json.load(source_file)
        for transaction in source_data:
            if transaction["bought"]:
                earned_money -= Decimal(transaction["bought"]) * Decimal(
                    transaction["matecoin_price"])
                matecoin_account += Decimal(transaction["bought"])
            if transaction["sold"]:
                earned_money += Decimal(transaction["sold"]) * Decimal(
                    transaction["matecoin_price"])
                matecoin_account -= Decimal(transaction["sold"])

    with open("profit.json", "w") as destination_file:
        result = {"earned_money": str(earned_money),
                  "matecoin_account": str(matecoin_account)}
        json.dump(result, destination_file, indent=2)
