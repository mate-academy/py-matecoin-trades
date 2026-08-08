from decimal import Decimal
import json


def calculate_profit(file_name: str) -> dict:
    with open(file_name, "r") as file:
        trades = json.load(file)

        earned_money = Decimal(0)
        matecoin_account = Decimal(0)

        for trade in trades:
            bought = (
                Decimal(trade["bought"])
                if trade["bought"]
                else Decimal(0)
            )
            sold = Decimal(trade["sold"]) if trade["sold"] else Decimal(0)
            matecoin_price = Decimal(trade["matecoin_price"])

            earned_money += (sold - bought) * matecoin_price
            matecoin_account += bought - sold

            with open("profit.json", "w") as file:
                json.dump({
                    "earned_money": str(earned_money),
                    "matecoin_account": str(matecoin_account),
                }, file, indent=2)
