import json
import os
from decimal import Decimal

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def calculate_profit(file_name: str) -> None:
    trades_path = os.path.join(BASE_DIR, file_name)

    with open(trades_path, "r") as open_file:
        trades = json.load(open_file)
    sold = 0
    sold_coins = 0
    bought = 0
    bought_coins = 0
    for item in trades:
        if item["sold"]:
            sold += Decimal(item["sold"]) * Decimal(item["matecoin_price"])
            sold_coins += Decimal(item["sold"])
        if item["bought"]:
            bought += Decimal(item["bought"]) * Decimal(item["matecoin_price"])
            bought_coins += Decimal(item["bought"])
    earned_money = str(sold - bought)
    matecoin_account = str(bought_coins - sold_coins)
    output = {
        "earned_money": earned_money,
        "matecoin_account": matecoin_account,
    }

    output_path = os.path.join(ROOT_DIR, "profit.json")
    with open(output_path, "w") as output_file:
        json.dump(output, output_file, indent=2)
