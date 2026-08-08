import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as trades:
        data = json.load(trades)
        earned_money = Decimal("0")
        matecoin_account = Decimal("0")
        for transaction in data:
            if transaction["bought"] is not None:
                earned_money -= (
                    Decimal(transaction["bought"])
                    * Decimal(transaction["matecoin_price"]))
                matecoin_account += Decimal(transaction["bought"])
            if transaction["sold"] is not None:
                earned_money += (
                    Decimal(transaction["sold"])
                    * Decimal(transaction["matecoin_price"]))
                matecoin_account -= Decimal(transaction["sold"])

        result = {
            "earned_money" : str(earned_money),
            "matecoin_account" : str(matecoin_account)
        }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
