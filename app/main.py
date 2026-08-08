from decimal import Decimal
import json


def calculate_profit(filename: str) -> dict:
    with open(filename) as file:
        trades = json.load(file)
        earned_money = Decimal(0)
        matecoin_account = Decimal(0)

        for trade in trades:

            if trade["bought"] is not None:
                matecoin_account += Decimal(trade["bought"])
                earned_money -= (
                    Decimal(trade["matecoin_price"])
                    * Decimal(trade["bought"])
                )
            if trade["sold"] is not None:
                matecoin_account -= Decimal(trade["sold"])
                earned_money += (
                    Decimal(trade["matecoin_price"])
                    * Decimal(trade["sold"])
                )
        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }

        with open("profit.json", "w") as file:
            json.dump(result, file, indent=2)
