import os
import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    # Формування повного шляху до файлу з угодами
    trades_file_path = os.path.join("app", trades_file)

    with open(trades_file_path) as f:
        # with open("trades.json") as f:
        trades_data = json.load(f)

    # Ініціалізація змінних для розрахунку
    # прибутку та рахунку монет
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    # Проходження через кожну угоду і обчислення
    # прибутку та рахунку монет
    for trade in trades_data:
        if trade["bought"] is not None:
            bought_amount = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money -= bought_amount * matecoin_price
            matecoin_account += bought_amount
        if trade["sold"] is not None:
            sold_amount = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money += sold_amount * matecoin_price
            matecoin_account -= sold_amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # profit_file_path = os.path.join("tests", "profit.json")
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)

    # current_directory = os.getcwd()
    # print(current_directory)
