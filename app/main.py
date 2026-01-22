import json
import os
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            price = Decimal(trade["matecoin_price"])
            total = bought * price
            earned_money -= total
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            price = Decimal(trade["matecoin_price"])
            total = sold * price
            earned_money += total

    result = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    print(result)
    output_path = os.path.join(os.path.dirname(__file__), "..", "profit.json")
    with open(output_path, "w") as new_file:
        json.dump(result, new_file, indent=2)

# calculate_profit("trades.json")
