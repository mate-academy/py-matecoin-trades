from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        data = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in data:
        if trade["bought"]:
            earned_money -= (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"]:
            earned_money += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )
            matecoin_account -= Decimal(trade["sold"])

    with open("profit.json", "w") as out_file:
        json.dump(
            {"earned_money": str(earned_money),
             "matecoin_account":
             str(matecoin_account)},
            out_file, indent=2)
