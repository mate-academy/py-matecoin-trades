import os
import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    file_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(file_dir, trades_file)

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            trades = json.load(file)
    else:
        print(f"File {file_path} not found!")
        return

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * matecoin_price
        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * matecoin_price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    # Збереження файлу у кореневій папці
    root_dir = os.path.dirname(file_dir)  # Отримуємо кореневу папку
    profit_file_path = os.path.join(root_dir, "profit.json")

    with open(profit_file_path, "w") as output_file:
        json.dump(result, output_file, indent=2)


calculate_profit("trades.json")
