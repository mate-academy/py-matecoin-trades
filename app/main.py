import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file_in, open("profit.json", "w") as file_out:
        trades = json.load(file_in)

        earned_money = 0
        matecoin_account = 0

        for trade in trades:
            if trade["bought"]:
                matecoin_account += Decimal(trade["bought"])
                earned_money -= Decimal(trade["bought"]) \
                    * Decimal(trade["matecoin_price"])
            if trade["sold"]:
                matecoin_account -= Decimal(trade["sold"])
                earned_money += Decimal(trade["sold"]) \
                    * Decimal(trade["matecoin_price"])

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        json.dump(result, file_out, indent=2)
