import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    # Відкриваю файл з угодами і завантажую його в пам'ять
    with open(trades_file) as f:
        trades_data = json.load(f)

    earned_money = 0
    new_account = 0

    # Прохожусь по кожній угоді і обчислюю прибуток
    for trade in trades_data:
        if trade["bought"] is not None:
            # Обчислити вартість придбаних монет
            earned_money -= Decimal(trade["bought"]) * Decimal(
                trade["matecoin_price"])
            new_account += Decimal(trade["bought"])

        if trade["sold"] is not None:
            # Обчислити вартість проданих монет
            earned_money += Decimal(trade["sold"]) * Decimal(
                trade["matecoin_price"])
            new_account -= Decimal(trade["sold"])

    # Зберігаю результат у файлі profit.json
    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(new_account),
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
