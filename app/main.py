import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    profit = 0
    matecoin_amount = 0
    with (open(filename) as file):
        data = json.load(file)
        for trade in data:
            if trade["bought"]:
                profit -= (Decimal(trade["bought"])
                           * Decimal(trade["matecoin_price"]))
                matecoin_amount += Decimal(trade["bought"])
            if trade["sold"]:
                profit += (Decimal(trade["sold"])
                           * Decimal(trade["matecoin_price"]))
                matecoin_amount -= Decimal(trade["sold"])

    with open(
            "D:/programming/mate/projects/py-matecoin-trades/profit.json",
            "w"
    ) as file:
        result_string = {
            "earned_money": str(profit),
            "matecoin_account": str(matecoin_amount)
        }
        json.dump(result_string, file, indent=2)
