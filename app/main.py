import json
from decimal import Decimal
import os


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            bought_volume = Decimal(trade["bought"])
            matecoin_account += bought_volume
            earned_money -= bought_volume * matecoin_price

        if trade["sold"]:
            sold_volume = Decimal(trade["sold"])
            matecoin_account -= sold_volume
            earned_money += sold_volume * matecoin_price

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    profit_file_path = os.path.join(os.path.dirname(filename), "PROFIT.json")

    with open(profit_file_path, "w", encoding="utf-8") as file:
        json.dump(profit_data, file, indent=4)
