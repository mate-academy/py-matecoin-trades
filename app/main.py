import os
import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    # Отримуємо шлях до поточного скрипта та будуємо шлях до файлу
    file_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(file_dir, trades_file)

    # Перевірка наявності файлу
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            trades = json.load(file)
    else:
        print(f"File {file_path} not found!")
        return

    # Обробка даних з файлу
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

    # Підготовка результату
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    # Запис результату у файл profit.json
    with open("profit.json", "w") as output_file:
        json.dump(result, output_file, indent=2)


calculate_profit("trades.json")
