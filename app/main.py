import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in data:
        price_matecoin = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            earned_money -= bought * price_matecoin
            matecoin_account += bought

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            earned_money += sold * price_matecoin
            matecoin_account -= sold

    result_profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as json_file:
        json.dump(result_profit, json_file, indent=4)
