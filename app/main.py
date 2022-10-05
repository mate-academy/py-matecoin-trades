import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        data = json.load(file)

    profit = []

    for el in data:
        sold = Decimal(el["sold"]) if el["sold"] else 0
        bought = Decimal(el["bought"]) if el["bought"] else 0
        coin_price = Decimal(el["matecoin_price"])

        profit.append(
            {
                "earned_money": str(sold - bought * coin_price),
                "matecoin_account": str(sold - bought)
            }
        )

    with open("profit.json", "w") as file:
        json.dump(profit, file)
