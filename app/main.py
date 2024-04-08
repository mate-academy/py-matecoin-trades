import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = 0
    matecoin_account = 0

    for trade in trades:
        if trade["bought"]:
            earned_money -= Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            matecoin_account += Decimal(trade["bought"])

        if trade["sold"]:
            earned_money += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            matecoin_account -= Decimal(trade["sold"])

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
