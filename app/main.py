import json

from decimal import Decimal


def calculate_profit(filename: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(filename) as file:
        data = json.load(file)

        for act in data:

            if act["bought"]:
                earned_money -= (
                    Decimal(act["bought"]) * Decimal(act["matecoin_price"])
                )
                matecoin_account += Decimal(act["bought"])

            if act["sold"]:
                earned_money += (
                    Decimal(act["sold"]) * Decimal(act["matecoin_price"])
                )
                matecoin_account -= Decimal(act["sold"])

    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as f:
        json.dump(profit_dict, f, indent=2)
