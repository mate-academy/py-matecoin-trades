import os
from decimal import Decimal
import json


def calculate_profit(file_path: str) -> None:
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return

    with open(file_path, "r") as f:
        trades = json.load(f)

    earned_money = 0
    matecoin_account = 0

    for trade_entry in trades:
        if trade_entry["sold"]:
            matecoin_account -= Decimal(trade_entry["sold"])
            earned_money += (
                Decimal(trade_entry["matecoin_price"])
                * Decimal(trade_entry["sold"]))
        if trade_entry["bought"]:
            matecoin_account += Decimal(trade_entry["bought"])
            earned_money -= (
                Decimal(trade_entry["matecoin_price"])
                * Decimal(trade_entry["bought"]))

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2, sort_keys=True)
