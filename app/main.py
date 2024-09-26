import json
from decimal import Decimal
import os


def calculate_profit(file_name: str) -> None:
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, file_name)

    if not os.path.exists(file_path):
        print(f"Error: The file '{file_name}' does not exist.")
        return

    with open(file_path, "r") as f:
        trades = json.load(f)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        if trade["bought"] is not None:
            bought_volume = Decimal(trade["bought"])
            matecoin_account += bought_volume
            earned_money -= bought_volume * Decimal(trade["matecoin_price"])
        if trade["sold"] is not None:
            sold_volume = Decimal(trade["sold"])
            matecoin_account -= sold_volume
            earned_money += sold_volume * Decimal(trade["matecoin_price"])

    profit_info = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    profit_file_path = os.path.join(current_dir, "profit.json")

    with open(profit_file_path, "w") as f:
        json.dump(profit_info, f, indent=4)


calculate_profit("trades.json")
