import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    with open(file_name) as source_file:
        trades_info = json.load(source_file)

        for transaction in trades_info:
            if transaction["bought"] is not None:
                amount = Decimal(transaction["bought"])
                earned_money -= amount * Decimal(transaction["matecoin_price"])
                matecoin_account += amount

            if transaction["sold"] is not None:
                amount = Decimal(transaction["sold"])
                earned_money += amount * Decimal(transaction["matecoin_price"])
                matecoin_account -= amount

        with open("profit.json", "w") as profit_file:

            output = {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account),
            }

            json.dump(output, profit_file, indent=2)
