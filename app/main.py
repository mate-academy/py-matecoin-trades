import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        trades = json.load(f)
        for deal in trades:
            if deal["sold"] is None:
                deal["sold"] = 0
            if deal["bought"] is None:
                deal["bought"] = 0

        matecoin_account = 0
        earned_money = 0

        for deal in trades:
            matecoin_account += (
                Decimal((deal["bought"]))
                - Decimal((deal["sold"]))
            )
            earned_money += (
                Decimal(deal["sold"])
                * Decimal(deal["matecoin_price"])
            )
            matecoin_account -= Decimal(deal["sold"])
            earned_money -= (
                Decimal(deal["bought"])
                * Decimal(deal["matecoin_price"])
            )
            matecoin_account += Decimal(deal["sold"])

        balance = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        print(balance)
    with open("profit.json", "w") as f:
        json.dump(balance, f, indent=2)
