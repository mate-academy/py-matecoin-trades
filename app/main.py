import json
from decimal import Decimal
import os


def calculate_profit(filename: str) -> None:
    if not os.path.exists(filename):
        print(f"Ошибка: файл '{filename}' не найден.")
        return

    # Инициализация переменных для хранения прибыли и баланса
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    # Чтение данных из файла
    with open(filename, "r") as file:
        trades = json.load(file)

    # Обработка каждой сделки
    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        price = Decimal(trade["matecoin_price"])

        # Обновление баланса и прибыли
        matecoin_account += bought - sold
        earned_money += (sold - bought) * price

    # Сохранение результатов в файл
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)


# Пример использования функции
calculate_profit("trades.json")
