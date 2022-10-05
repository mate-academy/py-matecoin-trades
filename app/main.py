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
                "earned_money": sold - bought * coin_price,
                "matecoin_account": sold - bought
            }
        )

        total_profit = {
            "earned_money": str(sum([
                el["earned_money"] for el in profit
            ])),
            "matecoin_account": str(sum([
                el["matecoin_account"] for el in profit
            ])),
        }
        with open("profit.json", "w") as file:
            json.dump(total_profit, file)
