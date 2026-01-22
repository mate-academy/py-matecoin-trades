import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as outfile:
        balance = 0
        matecoin = 0
        for trade in json.load(outfile):
            if trade["bought"]:
                matecoin += Decimal(trade["bought"])
                balance -= (
                    Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
                )
            if trade["sold"]:
                matecoin -= Decimal(trade["sold"])
                balance += (
                    Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
                )

        result = {
            "earned_money": str(balance), "matecoin_account": str(matecoin)
        }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2, sort_keys=True)
