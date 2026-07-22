from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for trade in data:
            if trade["bought"]:
                earned_money -= (
                    Decimal(trade["bought"])
                    * Decimal(trade["matecoin_price"])
                )
                matecoin_account += Decimal(trade["bought"])

            if trade["sold"]:
                earned_money += (
                    Decimal(trade["sold"])
                    * Decimal(trade["matecoin_price"])
                )
                matecoin_account -= Decimal(trade["sold"])

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as outfile:
        json.dump(result, outfile, indent=2)
