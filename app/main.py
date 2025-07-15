import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    with open(file_name, "r") as file:
        trades_information = json.load(file)

    for trade in trades_information:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            bought = Decimal(trade["bought"])
            earned_money -= bought * price
            matecoin_account += bought

        if trade["sold"]:
            sold = Decimal(trade["sold"])
            earned_money += sold * price
            matecoin_account -= sold

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
