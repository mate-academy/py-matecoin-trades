import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(file_name) as data_file:
        data = json.load(data_file)

        for trade in data:
            price = Decimal(trade["matecoin_price"])

            if trade["bought"] is not None:
                amount = Decimal(trade["bought"])
                matecoin_account += amount
                earned_money -= amount * price

            if trade["sold"] is not None:
                amount = Decimal(trade["sold"])
                matecoin_account -= amount
                earned_money += amount * price

        result_dictionary = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as output_file:
            json.dump(result_dictionary, output_file, indent=2)
