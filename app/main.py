import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    with (open(file_name, "r") as file):
        data = json.load(file)

        for item in data:
            bought = item["bought"] and Decimal(item["bought"])
            sold = item["sold"] and Decimal(item["sold"])
            matecoin_price = (
                item["matecoin_price"] and Decimal(item["matecoin_price"])
            )

            if bought:
                matecoin_account += bought
                earned_money -= bought * matecoin_price

            if sold:
                matecoin_account -= Decimal(sold)
                earned_money += sold * matecoin_price

    earned_money = str(earned_money)
    matecoin_account = str(matecoin_account)

    with open("profit.json", "w") as file:
        json.dump(
            {
                "earned_money": earned_money,
                "matecoin_account": matecoin_account
            },
            file,
            indent=2
        )
