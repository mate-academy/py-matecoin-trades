import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        data = json.load(file)

    profit = []
    null = 0

    for el in data:
        sold = Decimal(el["sold"])
        bought = Decimal(el["bought"])
        coin_price = Decimal(el["matecoin_price"])

        profit.append(
            {
                "earned_money": str(sold - bought * coin_price),
                "matecoin_account": str(sold - bought)
            }
        )

    with open("profit.json", "w") as file:
        json.dump(profit, file)
