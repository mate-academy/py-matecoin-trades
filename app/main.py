import os
import json
from decimal import Decimal


def calculate_profit(name: str,
                     output_file: str = "profit.json") -> None:
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)
    with open(name, "r") as file:
        data = json.load(file)
        for trade in data:
            matecoin_price = Decimal(trade["matecoin_price"])
            if trade["bought"] is not None:
                bought = Decimal(trade["bought"])
                matecoin_account += bought
                earned_money -= bought * matecoin_price
            if trade["sold"] is not None:
                sold = Decimal(trade["sold"])
                matecoin_account -= sold
                earned_money += sold * matecoin_price

    data_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    base_dir = os.path.dirname(os.path.dirname(__file__))
    output_path = os.path.join(base_dir, output_file)

    with open(output_path, "w") as file:
        json.dump(data_dict, file, indent=2)
